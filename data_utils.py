import pandas as pd
import numpy as np
import os
import time
import utils
import datetime as dt
from PyAstronomy import pyasl
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split

class TrafficStopData:
	def __init__(self, dataFolder, state, policeDept, colNamesList, dtypeDict):
		start = time.time()
		df = utils.load_data(dataFolder, state, policeDept, dtypeDict=dtypeDict, colNames=colNamesList)
		df = utils.remove_empty_rows(df, 'county_name')
		df = utils.remove_empty_rows(df, 'violation')
		df['violation'] = [s.lower() for s in df['violation']]
		self.df = utils.remove_empty_rows(df, 'subject_race')
		print('loading time: %d'%(time.time()-start))
        # Load county categories downloaded from US OMB website
		county_df = pd.read_csv(os.path.join('data', state, '2014-2018.csv'))
		county_df = county_df[county_df['State']=='Texas']
		self.county_df = county_df.filter(items=['Metropolitan Status', 'County Name'])

	def preprocess(self, contains='speed'):
		"""
		preproccesses df in place
		"""
        
        # Convert date and time to a single column which indicates time elapsed yet in the year
        # This is scaled from 0-1
        # This gives us a continuous numeric column
		start = time.time()
		self.df = self.df[self.df['violation'].str.contains('speed', regex=False)]
		self.df.drop('violation', 1, inplace=True)
		self.df['year'] = pd.to_datetime(self.df['date']).dt.year
		self.df['yearfrac'] = [pyasl.decimalYear(d) for d in pd.to_datetime(self.df['date'])]
		self.df['yearfrac'] = self.df['yearfrac'] - self.df['year']
		self.df['minute'] = pd.to_datetime(self.df['time']).dt.minute
		self.df['hour'] = pd.to_datetime(self.df['time']).dt.hour
		self.df['time'] = self.df['hour'] + self.df['minute'] / 60

		scaler = MinMaxScaler()
		scaler.fit(np.array(self.df['time']).reshape(-1,1))
		self.df['time'] = scaler.transform(np.array(self.df['time']).reshape(-1,1))
		self.df.drop(['hour', 'minute', 'date'], 1, inplace=True)
        
        # County names are converted to county type - metropolitan, micropolitan or non-core
        # For definitions, see US OMB website
		self.df['county_name'] = [name[:-7] for name in self.df['county_name']]
		self.df = self.df.join(self.county_df.set_index('County Name'), on='county_name')
		self.df.drop('county_name', 1, inplace=True)
		self.df.rename(columns={'Metropolitan Status':'county_type'}, inplace=True)

        # Convert citation issued and warning issued columns to integer
		self.df = self.df.astype({'citation_issued': 'int64', 'warning_issued': 'int64'})
		self.df = pd.get_dummies(self.df, dummy_na=True)
		print('preprocessing time: %d'%(time.time()-start))

		return(self.df)

	def get_train_test_sets(self, test_size=0.15):
		X = self.df.drop(['citation_issued', 'subject_race_white'], 1)
		y = self.df['citation_issued']
		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
		return(X_train,y_train,X_test,y_test)