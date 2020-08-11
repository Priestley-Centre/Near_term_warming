import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

"""
Created on Fri Jan 17 11:44 2020

@author: Christine McKenna

======================================================================
Purpose: Plotting code for Supp Fig 6.

         Plots time series of gsat anomalies for three different sets
         of observations (HadOST, Cowtan-Way, Berkeley-Earth) and the
         forced IRM response in Haustein et al 2019. Also plots time
         series of the residuals (obs minus IRM response),
         time series of 20-year trends in residuals, and a PDF of 
         20-year trends in residuals.

         Outputs moving 20-year means and 20-year trends in residuals
         for adding to FaIR forced response in Figure 1 and various
         other figures.
======================================================================
"""


# Required directories
basedir = '...' # Data not supplied here - need to obtain from
                # Karsten Haustein
savedir = 'Priestley-Centre/Near_term_warming/IV_data'


### ------ Load in Haustein data ------

# Obs (also apply scaling factors to convert from GBST to GSAT)
obs = np.loadtxt(basedir+'/Observations_HadOST_CowtanWay_Berkeley'+\
                 '_All3.csv',dtype='str',delimiter=',')
obs_Had = obs[1:,2].astype('float')*1.087
obs_CW = obs[1:,3].astype('float')*1.087
obs_Be = obs[1:,4].astype('float')*1.087
years_obs = obs[1:,1].astype('float')

# Forced IRM response
IRM = np.loadtxt(basedir+'/ImpulseResponseModel_MEI_RAW_ObsAll3.csv',\
                 dtype='str',delimiter=',')[:,:6]
IRM_raw = IRM[1:,4].astype('float')
years_raw = IRM[1:,3].astype('float')

# Residuals 
res_Had = obs_Had - IRM_raw
res_CW = obs_CW - IRM_raw 
res_Be = obs_Be - IRM_raw
years = obs[1:,1].astype('int')
ny = len(years)


### -------- Calculate 20y trends in residuals -------

# Create arrays to hold trends 
trends_Had = np.zeros([ny-20])
trends_CW  = np.zeros([ny-20])
trends_Be  = np.zeros([ny-20])

## Calculate trends
for y in xrange(0,ny-20):
    [m,_,_,_,_] = stats.linregress(years[y:y+20],\
                                   res_Had[y:y+20])
    trends_Had[y] = m*10
    [m,_,_,_,_] = stats.linregress(years[y:y+20],\
                                   res_CW[y:y+20])
    trends_CW[y] = m*10
    [m,_,_,_,_] = stats.linregress(years[y:y+20],\
                                   res_Be[y:y+20])
    trends_Be[y] = m*10
       
## Save trends to add to FaIR GSAT forced trends
np.save(saveedir+'/gsat_20ytrends_Haus_res_HadOST.npy',trends_Had) 
np.save(savedir+'/gsat_20ytrends_Haus_res_CW.npy',trends_CW) 
np.save(savedir+'/gsat_20ytrends_Haus_res_Be.npy',trends_Be) 


### -------- Calculate 20y means in residuals -------

# Create arrays to hold means 
means_Had = np.zeros([ny-20])
means_CW  = np.zeros([ny-20])
means_Be  = np.zeros([ny-20])

## Calculate means
for y in xrange(0,ny-20):
    means_Had[y] = np.mean(res_Had[y:y+20])
    means_CW[y] = np.mean(res_CW[y:y+20])
    means_Be[y] = np.mean(res_Be[y:y+20])

## Save means to add to FaIR GSAT forced anomalies
np.save(savedir+'/gsat_20ymeans_Haus_res_HadOST.npy',means_Had) 
np.save(savedir+'/gsat_20ymeans_Haus_res_CW.npy',means_CW) 
np.save(savedir+'/gsat_20ymeans_Haus_res_Be.npy',means_Be) 


### ------ Plot results ------

fig1,[[ax1,ax2],[ax3,ax4]] = plt.subplots(2,2,figsize=(10,8.5))
fig1.suptitle('Observation based estimates of internal\nvariability'+\
              ' in 20-year GSAT trends',fontsize=20)

ax1.set_title(r'$\bf{a}$'+'  GSAT anomaly',fontsize=16,loc='left')
ax1.plot(years_obs,obs_CW,label='CWv2',color='#d62728')
ax1.plot(years_obs,obs_Be,label='BE',color='#1f77b4')
ax1.plot(years_obs,obs_Had,label='HadOST',color='k')
ax1.plot(years_raw,IRM_raw,label='IRM',color='orange')
ax1.plot([1850,2020],[0,0],color='k',linestyle='--',linewidth=0.75)
ax1.set_xlim([1850,2020])
ax1.set_ylim([-0.37,1.51])
ax1.set_xlabel('Year',fontsize=14)
ax1.set_ylabel('$^{\circ}$C',fontsize=14)
ax1.tick_params(axis='both',labelsize=14)
ax1.legend(loc='best',fontsize=12)

ax2.set_title(r'$\bf{b}$'+'  Residual (obs - IRM)',fontsize=16,loc='left')
ax2.plot(years_C,res_C_CW,label='CWv2',color='#d62728')
ax2.plot(years_C,res_C_Be,label='BE',color='#1f77b4')
ax2.plot(years_C,res_C_Had,label='HadOST',color='k')
ax2.plot([1850,2020],[0,0],color='k',linestyle='--',linewidth=0.75)
ax2.set_xlim([1850,2020])
ax2.set_ylim([-0.44,0.44])
ax2.set_xlabel('Year',fontsize=14)
ax2.set_ylabel('$^{\circ}$C',fontsize=14)
ax2.tick_params(axis='both',labelsize=14)
ax2.legend(loc='best',fontsize=12)
   
ax3.set_title(r'$\bf{c}$'+'  Rolling trends for 20-year\n    segments of '+\
              'residuals',fontsize=16,loc='left')
ax3.plot(years_C[10:-10],trends_C_CW,label='CWv2',color='#d62728')
ax3.plot(years_C[10:-10],trends_C_Be,label='BE',color='#1f77b4')
ax3.plot(years_C[10:-10],trends_C_Had,label='HadOST',color='k')
ax3.plot([1850,2020],[0,0],color='k',linestyle='--',linewidth=0.75)
ax3.set_xlim([1850,2020])
ax3.set_ylim([-0.18,0.18])
ax3.set_xlabel('Year',fontsize=14)
ax3.set_ylabel('$^{\circ}$C / decade',fontsize=14)
ax3.tick_params(axis='both',labelsize=14)
ax3.legend(loc='best',fontsize=12)
   
ax4.set_title(r'$\bf{d}$'+'  Histogram of 20-year trends',fontsize=16,loc='left')
ax4.hist(trends_C_CW,bins=15,label='CWv2',color='#d62728',\
         histtype='stepfilled',alpha=0.3)
ax4.hist(trends_C_Be,bins=15,label='BE',color='#1f77b4',\
         histtype='stepfilled',alpha=0.3)
ax4.hist(trends_C_Had,bins=15,label='HadOST',color='k',\
         histtype='stepfilled',alpha=0.3)
ax4.plot([0,0],[0,35],color='k',linestyle='--',linewidth=0.75)
ax4.set_xlim([-0.18,0.18])
ax4.set_ylim([0,35])
ax4.set_xlabel('$^{\circ}$C / decade',fontsize=14)
ax4.set_ylabel('Frequency',fontsize=14)
ax4.tick_params(axis='both',labelsize=14)
ax4.legend(loc='best',fontsize=12)

plt.subplots_adjust(top=0.85,bottom=0.08,left=0.1,right=0.98,\
                    wspace=0.25,hspace=0.46)
plt.show()

