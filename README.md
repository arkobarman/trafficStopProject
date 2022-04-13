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


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
<h2 id="updates"> Updates</h2>

Folder:

county_summary_stats - county-level summary statistics and visualization

logistic_regression_violation_types - Further examine top violation types, logistic regressions for selected violation types combined, and yearly citation rate visualization for violation types.

results_0206 - preprocessing (filter speeding only records and split data files for each year), yearly logistic regression for speeding only records, logistic regression for school zone violation (all year combined)

