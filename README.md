# trafficStopProject
This repository contains the code and results for the traffic stop project.

utils.py - Functions to help with loading data and plotting

data_utils.py - Contains TrafficStopData class, which loads and preprocesses data, filtering on a violation type



TrafficStop_ExploratoryAnalysis.ipynb - exploratory analysis plots for grant

analyzeViolation.ipynb - explore types of violations in dataset

logisticRegression.ipynb - trying different types of sklearn logistic regression just on one-hot-encoded subject race

logisticGAM.ipynb - logistic GAM on one-hot-encoded races, by year (because the dataset is too big)

SpeedingViolations.ipynb - sklearn logistic regression using more features than in logisticRegression.ipynb. Date converted into fraction of year, time converted into fraction of day, and counties grouped into 3 categories by population

LogitSpeeding.ipynb - data processed the same way as in SpeedingViolations.ipynb, but using TrafficStopData class. Trained using statsmodels logistic regression
