# Traffic Stop Project

This project focuses on inherent racial biases displayed by the police force, in different states of the U.S. So far, the data that has been examined is for Texas. 

## Data
- The data can be extracted from [this website](https://openpolicing.stanford.edu/data/), in the form of a CSV or an RDS file. 
- For the purpose of this project, the *Texas State Patrol data* has been downloaded as an RDS file, and then converted into a parquet file. 
- The parquet file conversion is done on RStudio and the code for that is present in the repository, as a .R file named [Conversion_parquet_file.R](Conversion_parquet_file.R)

## Repository Structure
> This repository is currently under reconstruction. Archived folders can be found in the [replicated folder](replicated).
> New updated files can be found in the main repository. 

## Project Objective

### Key parameters of the dataset
Some of the main parameters present in the data are:
1. Date, Time
2. Location, Lattitude, Longitude
3. Precinct
4. Region, District
5. Subject race, Subject sex
6. Violation type
7. Citation Issued (T/F)
8. Warning Issued (T/F)
9. Contraband (Weapons, Drugs) found (T/F)
10. Search Conducted (T/F)
11. Vehicle Details (Color, Make etc)

#### FinalNotebook(LR)
- As explained in the [python notebook](FinalNotebook(LR).ipynb), the parquet data is split based on the year, ranging from 2006 to 2017.
- A simple sanity check is performed on the data before entering into analysis.
- There are three logistic regression analyses that are performed:
  - Logistic Regression without considering the Violation Type
  - Logistic Regression considering the Violation Type
  - Logistic Regression for **speeding-only** records.
- In these logisic regression curves, the **_variable odds_** ratio is plotted against the year. **_Variable odds ratio_** is a parameter usually utilized in case control studies. It represents the odds given a particular condition against a baseline without that condition. In the case of this project, it is plotted as a particular minority race (Black, Hispanic, Asian/Pacific Islander) against baseline majority race (White). 
  - For more information on odds-ratio and how it is calculated, refer to this [site](https://psychscenehub.com/psychpedia/odds-ratio-2/).
  
