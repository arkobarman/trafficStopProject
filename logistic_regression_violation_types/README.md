This sub-repository contains notebooks and generated outputs for specific violation types
<h2 id="folder-structure"> notebooks </h2>

    ├────── vio_LR.ipynb
            (logistic regression for several violation categories (separate and combined) having 5% < citation rate < 90%)
    ├────── traffic_stop_tableau_0226.ipynb
            (Change output files from trafficstop_county_summmarystat.ipynb to format suitable for Tableau visualization)
    ├────── lr_rates_diverse.ipynb
            (
             1. Logistic regression with only counties
             2. Speeding only and for all stops: [Rate of citation (normalize by # of stops or population) for each county; Rate of arrest (normalize by # of stops or population) fpr each county]
             3. Look at stop reasons (is there any other general category like speeding)
             4. diversity index
            )
            
<h2 id="folder-structure"> csv files </h2>  

    ├────── vio_LR
            (output of vio_LR.ipynb: csv, jpg and svg files)
    ├────── spd_other_pct,csv
            (output of trafficstop_county_summmarystat.ipynb)
    ├────── speeding_latlng.xlsx
            (total number of stops, geographic and population for each county)
    ├────── tableau_cite_rate_spd_cat.xlsx
            (output of traffic_stop_tableau_0226.ipynb)
    ├────── tableau_other_pct.xlsx
            (output of traffic_stop_tableau_0226.ipynb)            
    ├────── rate_geo_0314.xlsx
            (output of lr_rates_diverse.ipynb: rates, diversity index)
    ├────── LR_county_only.xlsx
            (output of lr_rates_diverse.ipynb: rates, diversity index)
            
<h2 id="folder-structure"> downloaded csv files </h2>  

    ├────── table_county.xlsx
            (downloaded csv file with longitude, latitude and population(2010) info for each county)

<h2 id="folder-structure"> tableau files </h2>  
    
    ├────── speeding_cat_cite.twb
            (tableau dashboard with filters for county)
    ├────── other_pct.twb
            (tableau dashboard with filters for county)
    ├────── geo_speeding_stops.twb
            (tableau dashboard of total # of stops for each county)
    ├────── 0314_2010 data.twb
            (tableau visualization of rate_geo_0314.xlsx. stops, citation rates, diversity index and their relationships)
            
* See notebooks for definitions of summary statistics and calculation details
