import os
import glob
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

def load_data(dataFolder, state, policeDept, dtypeDict=None, colNames=None):
	'''
	TODO: auto generate dtypeDict -- can't just read top rows because NAs, maybe 
			set every dtype to object and change it later?
	'''
	if len(state) > 2:
		print("Use 2 letter state name")
		return
	csvFilepath = glob.glob(os.path.join(dataFolder, state, '{}_{}*.csv'.format(state.lower(), policeDept)))[0]
	allColNames = get_col_names(dataFolder, state, policeDept)
	if not colNames:
		colNames = allColNames
	else:
		for name in colNames:
			if name not in allColNames:
				print("Invalid column name: " + name)
				return
	chunk = pd.read_csv(csvFilepath,chunksize=1000000, dtype=dtypeDict, usecols=colNames)
	df = pd.concat(chunk)
	return(df)


def get_col_names(dataFolder, state, policeDept):
	csvFilepath = glob.glob(os.path.join(dataFolder, state, '{}_{}*.csv'.format(state.lower(), policeDept)))[0]
	with open(csvFilepath) as csvFile:
		csvReader = csv.reader(csvFile, delimiter=',')
		colNames = []
		for row in csvReader:
			colNames.extend(row)
			break
	return(colNames)


def autolabel(rects, ax, format_str):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate(format_str.format(height/100),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=16)



