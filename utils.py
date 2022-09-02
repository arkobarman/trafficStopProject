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


def remove_empty_rows(df, colName):
	df = df[df[colName] != 'unknown']
	df = df[df[colName].notna()]
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

def plot_ROC_confidence_intervals(y_true, y_pred, n_bootstraps=100, rng_seed=2021, conf_interv = 0.9):
    

    print("Original ROC area: {:0.3f}".format(roc_auc_score(y_true, y_pred)))

    bootstrapped_scores = []
    bootRocLst = []

    rng = np.random.RandomState(rng_seed)
    
    # create fpr grid for interpolation
    fprGridVec = np.linspace(0, 1, 100, endpoint=True)
    # matrix containing all tpr corresponding to fprGridVec
    tprGridMat = np.zeros((len(fprGridVec), n_bootstraps))
    
    for i in range(n_bootstraps):
        # bootstrap by sampling with replacement on the prediction indices
        indices = rng.randint(0, len(y_pred), len(y_pred))
        if len(np.unique(y_true[indices])) < 2:
            # We need at least one positive and one negative sample for ROC AUC
            # to be defined: reject the sample
            continue

        score = roc_auc_score(y_true[indices], y_pred[indices])
        tmpFpr, tmpTpr, _ = roc_curve(y_true[indices], y_pred[indices])
        tmpFpr = np.concatenate(([0], tmpFpr, [1]))
        tmpTpr = np.concatenate(([0], tmpTpr, [1]))

        # interpolate for comparable ROCs
        fInter = scipy.interpolate.interp1d(tmpFpr, tmpTpr, kind='nearest')
        tprGridMat[:, i] = fInter(fprGridVec)

        bootstrapped_scores.append(score)
        bootRocLst.append([tmpFpr, tmpTpr])
    #     print("Bootstrap #{} ROC area: {:0.3f}".format(i + 1, score))

    sorted_scores = np.array(bootstrapped_scores)
    sorted_scores.sort()

    # Computing the lower and upper bound of the 90% confidence interval
    # You can change the bounds percentiles to 0.025 and 0.975 to get
    # a 95% confidence interval instead.
    confidence_lower = sorted_scores[int((1 - conf_interv)/2 * len(sorted_scores))]
    confidence_upper = sorted_scores[int((1 - (1 - conf_interv)/2) * len(sorted_scores))]
    print("Confidence interval for the score: [{:0.3f} - {:0.3}]".format(confidence_lower, confidence_upper))
    
    # confidence interval for ROC
    tprGridMatS = np.sort(tprGridMat, axis=1)
    tprLow025 = tprGridMatS[:, int(0.025 * n_bootstraps)]
    tprTop975 = tprGridMatS[:, int(0.975 * n_bootstraps)]
    tprMean = np.mean(tprGridMat, axis=1)

    # plt.hold(True)
    ax = plt.gca()  # kwargs.pop('ax', plt.gca())
    base_line, = ax.plot(fprGridVec, tprMean, '-', linewidth=4)
    ax.fill_between(fprGridVec, tprLow025, tprTop975, facecolor=base_line.get_color(), alpha=0.2)

    

