This sub-repository contains notebooks and generated outputs for specific violation types
<h2 id="folder-structure"> notebooks </h2>

    ├────── vio_LR.ipynb
            (logistic regression for several violation categories (separate and combined) having 5% < citation rate < 90%)
    ├────── raw_cnt_prelim_lr.ipynb
            (Generate raw counts for stops, citations/no citations for each race each year and preliminary logistic regression for high citation rate types combined and low citation rates combined)
    ├────── vio_type_rates_lr.ipynb
            (Further examine top violation types, calculation of citation rates for each race for several violation types, and logistic regression for high citation rate types and low citation rate types. Visualizations inside notebook.)
            
            
<h2 id="folder-structure"> csv files </h2>  

    ├────── vio_LR
            (output of vio_LR.ipynb: csv, jpg and svg files)
    ├────── raw_cnt_prelim_lr
            (output of raw_cnt_prelim_lr.ipynb, raw count csvs and preliminary logistic regression (needs modification))

            
* See notebooks for details
