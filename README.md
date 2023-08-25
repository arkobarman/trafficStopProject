# Traffic Stop Project

This project focuses on inherent racial biases displayed by the police force, in different states of the U.S. So far, the data that has been examined is for Texas. 

## Data
- The data can be extracted from [this website](https://openpolicing.stanford.edu/data/), in the form of a CSV or an RDS file. 
- For the purpose of this project, the *Texas State Patrol data* has been downloaded as an RDS file, and then converted into a parquet file. 
- The parquet file conversion is done on RStudio and the code for that is present in the repository, as a .R file named [Conversion_parquet_file.R](Conversion_parquet_file.R)

## Repository Structure
1. Archived folders can be found in the [Archived](Archived).
2. [External Data](https://github.com/arkobarman/trafficStopProject/tree/main/External%20Data) has the data files used in the analysis besides the traffic stop data.
3. The results currently included in the manuscript can be found in [Main Results](https://github.com/arkobarman/trafficStopProject/tree/main/Main%20Results).
4. [Stanford Project Data Summary](https://github.com/arkobarman/trafficStopProject/tree/main/Stanford%20Project%20Data%20Summary) has excel files that summarize variables available in data from other states.
5. [Supplementary](https://github.com/arkobarman/trafficStopProject/tree/main/Supplementary) has some other analysis for exploratory purpose that are not included in the manuscript.
6. [Tableau Files](https://github.com/arkobarman/trafficStopProject/tree/main/Tableau%20Files) has some intermediate data files and Tableau workbooks for visualizing diversity indexes for different counties.


## Project Objective
Using administrative records for traffic stops made available by Texas State Patrol from 2006 through 2017, we test for racial disparities in the issuance of citations to black, Hispanic, and Asian drivers relative to white drivers. Search conducted and contraband found given searched are also analyzed for speeding-only stops.

## Key parameters of the dataset
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

## Analysis Conducted
There are three important outcome variables in our dataset: citation, search_conducted and contraband_found.
We have 4 logistic regression models currently included in our manuscript:
- For all traffic stops, citation ~ race + gender + county type
- For speeding-only stops, citation ~ race + gender + county type
- For speeding-only stops, search_conducted ~ race + gender + county type
- For speeding-only stops, given that search has been conducted, contraband_found ~ race + gender + county type

County type is a categorical variable mapped from county name and it has 3 levels: metropolitan, micropolitan, and non-core. The mapping from county name to county type can be found at [2014-2018.csv](2014-2018.csv).
