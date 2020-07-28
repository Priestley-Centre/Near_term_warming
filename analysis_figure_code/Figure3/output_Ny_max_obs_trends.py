import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

"""
Created on Mon Feb 10 17:24 2020

@author: Christine McKenna

======================================================================
Purpose: Outputs max trends in gsat for a range of N year periods in
         each observational historical record, for use in Figure 3
======================================================================
"""

# Load in required directories
basedir = 'Priestley-Centre/Near_term_warming/observation_data'
savedir = 'Priestley-Centre/Near_term_warming/analysis_figure_code/'+\
          'Figure3/saved_arrays'

# Load in data and apply scaling factors
# to convert from GBST to GSAT
temp_BE = np.loadtxt(basedir+'/BE_Land_and_Ocean.csv',\
                     delimiter=',')[:,1]*1.087
years_BE = np.loadtxt(basedir+'/BE_Land_and_Ocean.csv',\
                      delimiter=',')[:,0]
nyear_BE = len(years_BE)

temp_GI = np.loadtxt(basedir+'/GISTEMPv4.csv',\
                     delimiter=',')[:,1]*1.087
years_GI = np.loadtxt(basedir+'/GISTEMPv4.csv',\
                      delimiter=',')[:,0]
nyear_GI = len(years_GI)

temp_Ha = np.loadtxt(basedir+'/HadCRUT4.6.csv',\
                     delimiter=',')[:,1]*1.19
years_Ha = np.loadtxt(basedir+'/HadCRUT4.6.csv',\
                      delimiter=',')[:,0]
nyear_Ha = len(years_Ha)

temp_CW = np.loadtxt(basedir+'/CWv2_had4sst3.csv',\
                     delimiter=',')[:,1]*1.087
years_CW = np.loadtxt(basedir+'/CWv2_had4sst3.csv',\
                      delimiter=',')[:,0]
nyear_CW = len(years_CW)


# Calculate maximum Ny trends
trend_lengths = np.linspace(10,50,41)
max_trends = np.zeros([41,4])

for t_l in xrange(10,51):

    t = t_l - 10

    temp_trends_BE = np.zeros(nyear_BE-t_l+1)
    for y in xrange(0,nyear_BE-t_l+1):
        [m,_,_,_,_] = stats.linregress(years_BE[y:y+t_l],temp_BE[y:y+t_l])
        temp_trends_BE[y] = m*10

    temp_trends_GI = np.zeros(nyear_GI-t_l+1)
    for y in xrange(0,nyear_GI-t_l+1):
        [m,_,_,_,_] = stats.linregress(years_GI[y:y+t_l],temp_GI[y:y+t_l])
        temp_trends_GI[y] = m*10

    temp_trends_Ha = np.zeros(nyear_Ha-t_l+1)
    for y in xrange(0,nyear_Ha-t_l+1):
        [m,_,_,_,_] = stats.linregress(years_Ha[y:y+t_l],temp_Ha[y:y+t_l])
        temp_trends_Ha[y] = m*10

    temp_trends_CW = np.zeros(nyear_CW-t_l+1)
    for y in xrange(0,nyear_CW-t_l+1):
        [m,_,_,_,_] = stats.linregress(years_CW[y:y+t_l],temp_CW[y:y+t_l])
        temp_trends_CW[y] = m*10

    max_trends[t,0] = np.max(temp_trends_BE)
    max_trends[t,1] = np.max(temp_trends_GI)
    max_trends[t,2] = np.max(temp_trends_Ha)
    max_trends[t,3] = np.max(temp_trends_CW)


# Save range of max trends
np.save(savedir+'/obs_max_Ny_trends_upper.npy',\
        np.max(max_trends,axis=1))
np.save(savedir+'/obs_max_Ny_trends_lower.npy',\
        np.min(max_trends,axis=1))
np.save(savedir+'/obs_max_Ny_trends_BE.npy',\
        max_trends[:,0])
np.save(savedir+'/obs_max_Ny_trends_GI.npy',\
        max_trends[:,1])
np.save(savedir+'/obs_max_Ny_trends_Ha.npy',\
        max_trends[:,2])
np.save(savedir+'/obs_max_Ny_trends_CW.npy',\
        max_trends[:,3])



