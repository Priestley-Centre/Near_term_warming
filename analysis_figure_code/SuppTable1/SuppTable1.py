import numpy as np
import iris
from scipy import stats
import matplotlib.pyplot as plt

"""
Created on Mon Jan 20 14:06 2020

@author: Christine McKenna

======================================================================
Purpose: Outputs results for Supplementary Table 1, i.e. historical
         (1995-2014) and near-term (2021-2040) trends in median ERF
         for each component for each emissions pathway used in the
         FaIR simulations.
         
         Components listed in order: 
         CO2, CH4, N20, other GHGs, O3 trop, O3 strat, 
         strat water vapour, aerosols, BC on snow, landuse, 
         volcanic, solar
======================================================================
"""

# Required directories
loaddir_FAIR = 'Priestley-Centre/Near_term_warming/'+\
               'FaIR_data/ECS_TCR_ERF'


### ------ Load in FaIR data ------

# Scaling factors to give ERF distributions
inds = [3,4,5,6,7,8,9,11,12,13,14,15]
erf_dist = np.loadtxt(loaddir_FAIR+'/parameters.csv',delimiter=',',\
                      dtype='str')[1:,inds].astype('float')

# ERF timeseries for each component
inds = [1,2,3,4,5,6,7,9,10,11,12,13]
years = np.loadtxt(loaddir_FAIR+'/ERF_SSP119.csv',delimiter=',',\
                   dtype='str')[1:,0].astype('float')
erf_NDC_t = np.loadtxt(loaddir_FAIR+'/ERF_NDC.csv',delimiter=',',\
                       dtype='str')[1:,inds].astype('float')
erf_19_t = np.loadtxt(loaddir_FAIR+'/ERF_SSP119.csv',delimiter=',',\
                      dtype='str')[1:,inds].astype('float')
erf_70_t = np.loadtxt(loaddir_FAIR+'/ERF_SSP370.csv',delimiter=',',\
                      dtype='str')[1:,inds].astype('float')
erf_26_t = np.loadtxt(loaddir_FAIR+'/ERF_SSP126.csv',delimiter=',',\
                      dtype='str')[1:,inds].astype('float')
erf_85_t = np.loadtxt(loaddir_FAIR+'/ERF_SSP585.csv',delimiter=',',\
                      dtype='str')[1:,inds].astype('float')

# Multiply ERF timeseries by distributions
erf_NDC_t_fac = np.expand_dims(erf_NDC_t,axis=0)*np.expand_dims(\
                erf_dist,axis=1)
erf_19_t_fac = np.expand_dims(erf_19_t,axis=0)*np.expand_dims(\
               erf_dist,axis=1)
erf_26_t_fac = np.expand_dims(erf_26_t,axis=0)*np.expand_dims(\
               erf_dist,axis=1)
erf_70_t_fac = np.expand_dims(erf_70_t,axis=0)*np.expand_dims(\
               erf_dist,axis=1)
erf_85_t_fac = np.expand_dims(erf_85_t,axis=0)*np.expand_dims(\
                  erf_dist,axis=1)

# Median ERF
erf_NDC = np.median(erf_NDC_t_fac,axis=0)
erf_19 = np.median(erf_19_t_fac,axis=0)
erf_26 = np.median(erf_26_t_fac,axis=0)
erf_70 = np.median(erf_70_t_fac,axis=0)
erf_85 = np.median(erf_85_t_fac,axis=0)

# Separate into historical and scenarios
years_hist = years[:252]
years_scen = years[251:]
erf_hist = erf_19[:252]
erf_NDC = erf_NDC[251:]
erf_19 = erf_19[251:]
erf_26 = erf_26[251:]
erf_70 = erf_70[251:]
erf_85 = erf_85[251:]

# Total ERF
erf_hist_sum = np.sum(erf_hist,axis=1)
erf_NDC_sum = np.sum(erf_NDC,axis=1)
erf_19_sum = np.sum(erf_19,axis=1)
erf_26_sum = np.sum(erf_26,axis=1)
erf_70_sum = np.sum(erf_70,axis=1)
erf_85_sum = np.sum(erf_85,axis=1)


### ------ Output trends ------

# Indices for 1995-2014 and 2021-2040
ind1 = np.where(years_hist == 1995)[0][0]
ind2 = np.where(years_hist == 2014)[0][0]+1
ind3 = np.where(years_scen == 2021)[0][0]
ind4 = np.where(years_scen == 2040)[0][0]+1

# Total ERF
[m,_,_,_,_] = stats.linregress(years_hist[ind1:ind2],\
                               erf_hist_sum[ind1:ind2])
erf_hist_sum_trend = m*10
[m,_,_,_,_] = stats.linregress(years_scen[ind3:ind4],\
                               erf_NDC_sum[ind3:ind4])
erf_NDC_sum_trend = m*10
[m,_,_,_,_] = stats.linregress(years_scen[ind3:ind4],\
                               erf_19_sum[ind3:ind4])
erf_19_sum_trend = m*10
[m,_,_,_,_] = stats.linregress(years_scen[ind3:ind4],\
                               erf_26_sum[ind3:ind4])
erf_26_sum_trend = m*10
[m,_,_,_,_] = stats.linregress(years_scen[ind3:ind4],\
                               erf_70_sum[ind3:ind4])
erf_70_sum_trend = m*10
[m,_,_,_,_] = stats.linregress(years_scen[ind3:ind4],\
                               erf_85_sum[ind3:ind4])
erf_85_sum_trend = m*10

# Individual components
erf_hist_trend = np.zeros([12])
erf_NDC_trend = np.zeros([12])
erf_19_trend = np.zeros([12])
erf_26_trend = np.zeros([12])
erf_70_trend = np.zeros([12])
erf_85_trend = np.zeros([12])
for i in range(12):
    [m,_,_,_,_] = stats.linregress(years_hist[ind1:ind2],\
                                   erf_hist[ind1:ind2,i])
    erf_hist_trend[i] = m*10
    [m,_,_,_,_] = stats.linregress(years_scen[ind3:ind4],\
                                   erf_NDC[ind3:ind4,i])
    erf_NDC_trend[i] = m*10
    [m,_,_,_,_] = stats.linregress(years_scen[ind3:ind4],\
                                   erf_19[ind3:ind4,i])
    erf_19_trend[i] = m*10
    [m,_,_,_,_] = stats.linregress(years_scen[ind3:ind4],\
                                   erf_26[ind3:ind4,i])
    erf_26_trend[i] = m*10
    [m,_,_,_,_] = stats.linregress(years_scen[ind3:ind4],\
                                   erf_70[ind3:ind4,i])
    erf_70_trend[i] = m*10
    [m,_,_,_,_] = stats.linregress(years_scen[ind3:ind4],\
                                   erf_85[ind3:ind4,i])
    erf_85_trend[i] = m*10



