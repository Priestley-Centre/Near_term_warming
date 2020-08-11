import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

"""
Created on Tues Jan 28 16:05 2020

@author: Christine McKenna

======================================================================
Purpose: Plots Supplementary Fig 1: trends in gsat for all 20 year 
         periods in 4 different observational records
======================================================================
"""

# Load in required directories
basedir = 'Priestley-Centre/Near_term_warming/observation_data'

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
temp_trends_BE = np.zeros(nyear_BE-19)
for y in xrange(0,nyear_BE-19):
    [m,_,_,_,_] = stats.linregress(years_BE[y:y+20],temp_BE[y:y+20])
    temp_trends_BE[y] = m*10

temp_trends_GI = np.zeros(nyear_GI-19)
for y in xrange(0,nyear_GI-19):
    [m,_,_,_,_] = stats.linregress(years_GI[y:y+20],temp_GI[y:y+20])
    temp_trends_GI[y] = m*10

temp_trends_Ha = np.zeros(nyear_Ha-19)
for y in xrange(0,nyear_Ha-19):
    [m,_,_,_,_] = stats.linregress(years_Ha[y:y+20],temp_Ha[y:y+20])
    temp_trends_Ha[y] = m*10

temp_trends_CW = np.zeros(nyear_CW-19)
for y in xrange(0,nyear_CW-19):
    [m,_,_,_,_] = stats.linregress(years_CW[y:y+20],temp_CW[y:y+20])
    temp_trends_CW[y] = m*10

# Find max
max_trend = np.max(temp_trends_BE)
ind_max = np.where(temp_trends_BE == max_trend)[0][0]
max_yr = years_BE[10:-9][ind_max].astype('int')
max_per = str(max_yr-10)+'-'+str(max_yr+9)
max_str_BE = 'max = '+'{:.2f}'.format(max_trend)+' ('+max_per+')'

max_trend = np.max(temp_trends_GI)
ind_max = np.where(temp_trends_GI == max_trend)[0][0]
max_yr = years_GI[10:-9][ind_max].astype('int')
max_per = str(max_yr-10)+'-'+str(max_yr+9)
max_str_GI = 'max = '+'{:.2f}'.format(max_trend)+' ('+max_per+')'

max_trend = np.max(temp_trends_Ha)
ind_max = np.where(temp_trends_Ha == max_trend)[0][0]
max_yr = years_Ha[10:-9][ind_max].astype('int')
max_per = str(max_yr-10)+'-'+str(max_yr+9)
max_str_Ha = 'max = '+'{:.2f}'.format(max_trend)+' ('+max_per+')'

max_trend = np.max(temp_trends_CW)
ind_max = np.where(temp_trends_CW == max_trend)[0][0]
max_yr = years_CW[10:-9][ind_max].astype('int')
max_per = str(max_yr-10)+'-'+str(max_yr+9)
max_str_CW = 'max = '+'{:.2f}'.format(max_trend)+' ('+max_per+')'

# Plot running trend
plt.figure(1,figsize=(10,5))
plt.title('GSAT trends for rolling 20-year segments of observations',\
          fontsize=20,y=1.02)
plt.plot(years_Ha[10:-9].astype('int'),temp_trends_Ha,label=\
         'HadCRUT4.6, '+max_str_Ha,color='black')
plt.plot(years_BE[10:-9].astype('int'),temp_trends_BE,label=\
         'BE, '+max_str_BE,color='#1f77b4')
plt.plot(years_CW[10:-9].astype('int'),temp_trends_CW,label=\
         'CWv2, '+max_str_CW,color='#d62728')
plt.plot(years_GI[10:-9].astype('int'),temp_trends_GI,label=\
         'GISTEMPv4, '+max_str_GI,color='orange')
plt.plot(years_CW,np.zeros([nyear_CW]),'k--',linewidth=1.0)
plt.xlabel('Year',fontsize=18)
plt.xlim([1858,2012])
plt.ylabel('$^{\circ}$C / decade',fontsize=18)
plt.ylim([-0.4,0.3])
plt.legend(loc='best',fontsize=14)
plt.tick_params(labelsize=16)
plt.tight_layout()
plt.show()

