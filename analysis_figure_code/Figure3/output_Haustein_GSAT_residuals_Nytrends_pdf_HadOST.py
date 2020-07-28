import numpy as np
from scipy import stats

"""
Created on Fri Jan 17 11:44 2020

@author: Christine McKenna

======================================================================
Purpose: Outputs time series of Ny trends in gsat residuals for HadOST 
         observations minus the forced IRM response in Haustein et al 
         2019. Does so to add internal variability to forced Ny trends 
         in FaIR, for Figure 3.
======================================================================
"""

# Required directories
basedir = '...' # Data not supplied here - need to obtain from
                # Karsten Haustein
savedir = 'Priestley-Centre/Near_term_warming/Figure3/saved_arrays'


### ------ Load in Haustein data ------

# Obs (also apply scaling factor to convert from GBST to GSAT) 
obs = np.loadtxt(basedir+'/Observations_HadOST_CowtanWay_Berkeley'+\
                 '_All3.csv',dtype='str',delimiter=',')
obs_Had = obs[1:,2].astype('float')*1.087
years_obs = obs[1:,1].astype('float')

# Forced IRM response
IRM = np.loadtxt(basedir+'/ImpulseResponseModel_MEI_RAW_ObsAll3.csv',\
                 dtype='str',delimiter=',')[:,:6]
IRM_raw = IRM[1:,4].astype('float')
years_raw = IRM[1:,3].astype('float')

# Residuals (calculated here)
res_Had = obs_Had - IRM_raw
years = obs[1:,1].astype('int')
ny = len(years)


### -------- Calculate trends in residuals -------

# Create arrays to hold trends 
trends_Had = np.zeros([41,ny-10])

# Calculate trends (t_l is trend length)
for t_l in xrange(10,51):
    t = t_l-10
    for y in xrange(0,ny-t_l):
        [m,_,_,_,_] = stats.linregress(years[y:y+t_l],\
                                       res_Had[y:y+t_l])
        trends_Had[t,y] =m*10
       

## Save trends to add to FaIR GSAT forced trends
np.save(savedir+'/gsat_Nytrends_Haus_res_HadOST.npy',trends_Had) 


