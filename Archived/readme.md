This folder contains some analysis for exploratory purpose that are not currently included in our manuscript.

In this Archived folder, two notebooks could be almost the same except changes in a few lines of code.

Not all results are presentable and a code review should be done before any outputs in this folder will be used.(Potential problems could be not dropping base levels for categorical variables, collinearity, etc.)

## The following comments are directly copied from the original readme.md file:

#### Structure of codebase: Races
- As explained in the notebooks, the parquet data is split based on the year, ranging from 2006 to 2017.
- A simple sanity check is performed on the data before entering into analysis.
- There are three logistic regression analyses that are performed:
  - Logistic Regression without considering the Violation Type
  - Logistic Regression considering the Violation Type
  - Logistic Regression for **speeding-only** records.
- In these logisic regression curves, the **_variable odds_** ratio is plotted against the year. **_Variable odds ratio_** is a parameter usually utilized in case control studies. It represents the odds given a particular condition against a baseline without that condition. In the case of this project, it is plotted as a particular minority race (Black, Hispanic, Asian/Pacific Islander) against baseline majority race (White). 
  - For more information on odds-ratio and how it is calculated, refer to this [site](https://psychscenehub.com/psychpedia/odds-ratio-2/).

#### Structure of codebase: Gender 
- As explained in the notebooks, the parquet data is split based on the year, ranging from 2006 to 2017.
- A simple sanity check is performed on the data before entering into analysis.
- There are three logistic regression analyses that are performed:
  - Logistic Regression without considering the Violation Type
  - Logistic Regression considering the Violation Type
  - Logistic Regression for **speeding-only** records.
- In these logisic regression curves, the **_variable odds_** ratio is plotted against the year. **_Variable odds ratio_** is a parameter usually utilized in case control studies. It represents the odds given a particular condition against a baseline without that condition. In the case of this project, it is plotted as females against baseline males. 
 - For more information on odds-ratio and how it is calculated, refer to this [site](https://psychscenehub.com/psychpedia/odds-ratio-2/).


#### Files present in the main branch
1a. [LR_citation_issued.ipynb](https://github.com/arkobarman/trafficStopProject/blob/main/Archived/older_iterations/LR_citation_issued.ipynb)
  - This notebook performs the same analysis as explained above in the "Structure of codebase: Races".
  - The outcome variable is taken to be "citation_issued".

1b. [LR_citation_issued_female.ipynb](https://github.com/arkobarman/trafficStopProject/blob/main/Archived/older_iterations/LR_citation_issued_female.ipynb)
  - This notebook performs the same analysis as explained above in the "Structure of codebase: Gender".
  - The outcome variable is taken to be "citation_issued".
  
2a. [LR_search_conducted.ipynb](https://github.com/arkobarman/trafficStopProject/blob/main/Archived/older_iterations/LR_search_conducted.ipynb)
  - This notebook performs the same analysis as explained above in the "Structure of codebase: Races".
  - The outcome variable is taken to be "search_conducted".

2b. [LR_search_conducted_female.ipynb](https://github.com/arkobarman/trafficStopProject/blob/main/Archived/older_iterations/LR_search_conducted_female.ipynb)
  - This notebook performs the same analysis as explained above in the "Structure of codebase: Gender".
  - The outcome variable is taken to be "search_conducted".

3a. [LR_contraband_found.ipynb](https://github.com/arkobarman/trafficStopProject/blob/main/Archived/older_iterations/LR_contraband_found.ipynb)
  - This notebook performs the same analysis as explained above in the "Structure of codebase: Races".
  - The outcome variable is taken to be "contraband_found". In order to do this, the dataframe is subsetted to contain only the columns which have "search_conducted" as True. This is to ensure that there are no empty values/NaN values in the necessary outcome variable column.

3b. [LR_contraband_found_female.ipynb](https://github.com/arkobarman/trafficStopProject/blob/main/Archived/older_iterations/LR_search_conducted_female.ipynb)
  - This notebook performs the same analysis as explained above in the "Structure of codebase: Gender".
  - The outcome variable is taken to be "contraband_found". In order to do this, the dataframe is subsetted to contain only the columns which have "search_conducted" as True. This is to ensure that there are no empty values/NaN values in the necessary outcome variable column.
  
### [Interaction_Terms](Interaction_Terms)
  - In this folder, the dataset has 8 extra columns. 
  - These columns are Boolean interaction terms between race and gender. 
    - Female, White
    - Female, Black
    - Female, Hispanic
    - Female, Asian/Pacific Islander
    - Male, White
    - Male, Black
    - Male, Hispanic
    - Male, Asian/Pacific Islander
   - The extended dataset is used for performing the same logistic regression analysis with the three key parameters as target variables.
    - Citation Issued
    - Search Conducted
    - Contraband Found
  - The baseline is White Male, and the rest of the 7 terms are plotted as odds ratio against this baseline. 

### [Time_of_Day](Time_of_Day)

  - In this folder, the dataset has an extra column which depicts whether it is daytime or night time. This is done in order to gauge whether the citations and searches of minority (non-baseline) races are significantly different in the daytime when their races are apparent. 
  - The same plots are calculated, but there are two plots for every variable (Citation Issued, Search Conducted, Contraband Found) for the day and night time respectively. 


### Under Construction
- The analysis is being extended to different states to strengthen the claims of racial bias by increasing the size of the data under consideration. Presently, the data for Florida is being studied.
- Other tangents for research in Texas is also being conducted with different target variables. View the [in_progress/README.md](in_progress/README.md) file within the [in_progress](in_progress) folder for more information regarding these.

