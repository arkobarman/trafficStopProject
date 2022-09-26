There are multiple files present in this repo. Most of them are revised and present in the main branch. These are old iterations.
- As explained in the notebooks, the parquet data is split based on the year, ranging from 2006 to 2017.
- A simple sanity check is performed on the data before entering into analysis.
- There are three logistic regression analyses that are performed:
  - Logistic Regression without considering the Violation Type
  - Logistic Regression considering the Violation Type
  - Logistic Regression for **speeding-only** records.
- In these logisic regression curves, the **_variable odds_** ratio is plotted against the year. **_Variable odds ratio_** is a parameter usually utilized in case control studies. It represents the odds given a particular condition against a baseline without that condition. In the case of this project, it is plotted as a particular minority race (Black, Hispanic, Asian/Pacific Islander) against baseline majority race (White). 


1. [LR_search_conducted_v1.ipynb](LR_search_conducted_v1.ipynb)
  - This notebook performs the same analysis as explained above.
  - The outcome variable is taken to be "search_conducted".
  - It also additionally contains the odds ratio of females with white as the baseline for all the 3 models for Texas, on top of the odds ratio of the races against white as the baseline for all the 3 models for Texas.
2. [LR_contraband_found_v1.ipynb](LR_contraband_found_v1.ipynb)
  - This notebook performs the same analysis as explained above.
  - The outcome variable is taken to be "contraband_found". In order to do this, the dataframe is subsetted to contain only the columns which have "search_conducted" as True. This is to ensure that there are no empty values/NaN values in the necessary outcome variable column.
  - It also additionally contains the odds ratio of females with white as the baseline for all the 3 models for Texas, on top of the odds ratio of the races against white as the baseline for all the 3 models for Texas.
3. [LR_citation_issued_withoutfemales_v1.ipynb](LR_citation_issued_withoutfemales_v1.ipynb)
  - This notebook performs the same analysis as explained above.
  - The outcome variable is taken to be "citation_issued".
3. [LR_citation_issued_v1.ipynb](LR_citation_issued_v1.ipynb) 
  - This notebook contains the same file as [LR_citation_issued_withoutfemales_v1.ipynb](LR_citation_issued_withoutfemales_v1.ipynb) 
  - The only difference is that it also additionally contains the odds ratio of females with white as the baseline for all the 3 models for Texas, **on top of** the odds ratio of the races against white as the baseline for all the 3 models for Texas.
4. [LR_citation_issued_female_v1.ipynb](LR_citation_issued_female_v1.ipynb) 
  - This notebook contains three similar Logistic Regression Models but it is focussed only on the odds ratio of females with white as the baseline for all the 3       models for Texas. 
  - It does not include the odds ratio of the races against white as the baseline for all the 3 models for Texas.
  - This is done in order to view the female odds ratio more clearly, and focus on just that one parameter.
5. [Florida_ExploratoryAnalysis.ipynb](Florida_ExploratoryAnalysis.ipynb)
  - This notebook performs exploratory analysis on the state of Florida.
  - It has basic visualizations and statistical analysis on different parameters on the Florida state patrol information.

