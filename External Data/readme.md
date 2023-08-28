This folder contains external data files downloaded and used in this project besides the Stanford Open Policing Data.

1. 2014-2018.csv:county type info: metropolitan, micropolitan, and non-core

2. countyinfo.xlsx: county type info: 12 economic regions, including Alamo, Gulf Coast, Capital Region, Central Texas, High Plains, Metroplex Region, Northwest Texas, South Texas, Southeast Texas, Upper East Texas, West Texas and Upper Rio Grande Region

3. gini_2012_5year.csv: 5-year estimates of Gini indexes of Texas counties in 2012.

4. gini_2010_5year.csv: 5-year estimates of Gini indexes of Texas counties in 2010.

5. pop_Ishispanic_10.xlsx: Race compositions of Texas counties. Used for the calculation of population diversity index.

6. ACS2006_2010.xlsx: American Community Service 5 year estimates for racial composition of each county. In tx_county_race_pop.csv, the value in the year column for the file ACS2006_2010.xlsx will be 2010.

7. tx_county_race_pop.csv: A summary for all the ACS files from ACS2006_2010.xlsx to ACS2013_2017.xlsx. The diversity index is calculated as $D = 1-\frac{\sum n(n-1)}{N(N-1)}$, where n is the population count in each race group (for one county), N is the total number of population(for one county). The diversity_shannon index is calculated as -sum (p * math.log(p+0.000000001)), where p = n/N.
