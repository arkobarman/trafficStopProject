There are multiple files present in this file, which are all in progress at the moment. 
1. [FinalNotebook_LR_inclfemale.ipynb](FinalNotebook_LR_inclfemale.ipynb) 
  - This notebook contains the same file as [FinalNotebook(LR).ipynb](trafficStopProject/FinalNotebook(LR).ipynb) present in main
  - The only difference is that it also additionally contains the odds ratio of females with white as the baseline for all the 3 models for Texas, **on top of** the odds ratio of the races against white as the baseline for all the 3 models for Texas.
2. [LogReg_FemaleOnly.ipynb](LogReg_FemaleOnly.ipynb) 
  - This notebook contains three similar Logistic Regression Models but it is focussed only on the odds ratio of females with white as the baseline for all the 3 models for Texas. 
  - It does not include the odds ratio of the races against white as the baseline for all the 3 models for Texas.
  - This is done in order to view the female odds ratio more clearly, and focus on just that one parameter.
3. [Florida_ExploratoryAnalysis.ipynb](Florida_ExploratoryAnalysis.ipynb)
  - This notebook performs exploratory analysis on the state of Florida.
  - It has basic visualizations and statistical analysis on different parameters on the Florida state patrol information.
4. [LR_searchconducted.ipynb](LR_searchconducted.ipynb)
  - This notebook performs the same analysis as the FinalNotebook present in the main page. 
  - However, the outcome variable is taken to be "search_conducted" instead of "citation_issued"
  - It also additionally contains the odds ratio of females with white as the baseline for all the 3 models for Texas, on top of the odds ratio of the races against white as the baseline for all the 3 models for Texas.
5. [LR_contrabandfound.ipynb](LR_contrabandfound.ipynb)
  - This notebook performs the same analysis as the FinalNotebook present in the main page. 
  - However, the outcome variable is taken to be "contraband_found" instead of "citation_issued". In order to do this, the dataframe is subsetted to contain only the columns which have "search_conducted" as True. This is to ensure that there are no empty values/NaN values in the necessary outcome variable column.
  - It also additionally contains the odds ratio of females with white as the baseline for all the 3 models for Texas, on top of the odds ratio of the races against white as the baseline for all the 3 models for Texas.
 
