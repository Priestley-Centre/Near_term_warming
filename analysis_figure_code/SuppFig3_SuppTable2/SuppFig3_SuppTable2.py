import numpy as np
import matplotlib.pyplot as plt

"""
Created on 20 Jul 2020

@author: Christine McKenna

=========================================================================
Purpose: Plots Supp Fig 3. Global warming index (GWI) downloaded from:
         https://www.globalwarmingindex.org/AWI/info_page.html.
         Also outputs years of 1.5C crossing in Supp Table 2.
=========================================================================
"""

# Required directories
loaddir_FAIR = 'Priestley-Centre/Near_term_warming/FaIR_data/temps'
loaddir_obs = 'Priestley-Centre/Near_term_warming/analysis_figure_code/'+\
              'SuppFig3_SuppTable2' 


### --------- Load in obs data ---------------

# Note no conversion from GBST to GSAT, since Paris targets
# concern the former and not the latter
years_obs = np.loadtxt(loaddir_obs+'/Haustein_AWI_obs.csv',delimiter=',',\
                       dtype='float')[:,0]
temp_AWI_tmp = np.loadtxt(loaddir_obs+'/Haustein_AWI_obs.csv',\
                          delimiter=',',dtype='float')[:,1]
temp_obs_tmp = np.loadtxt(loaddir_obs+'/Haustein_AWI_obs.csv',\
                          delimiter=',',dtype='float')[:,2]

# Calculate annual means
years_obs = np.linspace(1850.,2019,170)
temp_AWI = np.zeros_like(years_obs)
temp_obs = np.zeros_like(years_obs)
for i in range(len(years_obs)):
    temp_AWI[i] = np.mean(temp_AWI_tmp[i*12:i*12+12])
    temp_obs[i] = np.mean(temp_obs_tmp[i*12:i*12+12])

# Find anomaly from 2000-2019
ind1 = np.where(years_obs == 2000.)[0][0]
ind2 = np.where(years_obs == 2019.)[0][0]+1
temp_obs_a = temp_obs - np.mean(temp_obs[ind1:ind2])
temp_AWI_a = temp_AWI - np.mean(temp_AWI[ind1:ind2])

# Average obs and find offset from 1850-1900
ind3 = np.where(years_obs == 1850.)[0][0]
ind4 = np.where(years_obs == 1900.)[0][0]+1
offset_obs = np.mean(temp_obs_a[ind1:ind2]) - np.mean(temp_obs_a[ind3:ind4])
temp_obs_a = temp_obs_a
offset_AWI = np.mean(temp_AWI_a[ind1:ind2]) - np.mean(temp_AWI_a[ind3:ind4])
temp_AWI_a = temp_AWI_a


### ------ Load in FaIR data ------

# Load and convert FaIR GSAT anomalies to GBST
# (since Paris 1.5C target concerns GBST)
gbst_NDC_f = np.loadtxt(loaddir_FAIR+'/NDC_temps.csv',delimiter=',',\
                        dtype='str')[1:,1:].astype('float')/1.087
gbst_19_f = np.loadtxt(loaddir_FAIR+'/ssp119_temps.csv',delimiter=',',\
                       dtype='str')[1:,1:].astype('float')/1.087
gbst_26_f = np.loadtxt(loaddir_FAIR+'/ssp126_temps.csv',delimiter=',',\
                       dtype='str')[1:,1:].astype('float')/1.087
gbst_70_f = np.loadtxt(loaddir_FAIR+'/ssp370_temps.csv',delimiter=',',\
                       dtype='str')[1:,1:].astype('float')/1.087
gbst_85_f = np.loadtxt(loaddir_FAIR+'/ssp585_temps.csv',delimiter=',',\
                       dtype='str')[1:,1:].astype('float')/1.087
years_f = np.loadtxt(loaddir_FAIR+'/NDC_temps.csv',delimiter=',',\
                     dtype='str')[1:,0].astype('float')

# Find anomaly from 2000-2019
ind1 = np.where(years_f == 2000.)[0][0]
ind2 = np.where(years_f == 2019.)[0][0]+1
gbst_NDC_f_a = gbst_NDC_f - np.mean(gbst_NDC_f[ind1:ind2],axis=0)
gbst_19_f_a = gbst_19_f - np.mean(gbst_19_f[ind1:ind2],axis=0)
gbst_26_f_a = gbst_26_f - np.mean(gbst_26_f[ind1:ind2],axis=0)
gbst_70_f_a = gbst_70_f - np.mean(gbst_70_f[ind1:ind2],axis=0)
gbst_85_f_a = gbst_85_f - np.mean(gbst_85_f[ind1:ind2],axis=0)

# Only take FaIR simuls from 2019 onwards
years_f = years_f[254:]
gbst_NDC_f_a = gbst_NDC_f_a[254:]
gbst_19_f_a = gbst_19_f_a[254:]
gbst_26_f_a = gbst_26_f_a[254:]
gbst_70_f_a = gbst_70_f_a[254:]
gbst_85_f_a = gbst_85_f_a[254:]

# Find percentiles
gbst_NDC_f_a_low = np.percentile(gbst_NDC_f_a,17,axis=1)
gbst_NDC_f_a_lowu = np.percentile(gbst_NDC_f_a,33,axis=1)
gbst_NDC_f_a_uppl = np.percentile(gbst_NDC_f_a,67,axis=1)
gbst_NDC_f_a_upp = np.percentile(gbst_NDC_f_a,83,axis=1)
gbst_NDC_f_a_med = np.median(gbst_NDC_f_a,axis=1)
gbst_19_f_a_low = np.percentile(gbst_19_f_a,17,axis=1)
gbst_19_f_a_lowu = np.percentile(gbst_19_f_a,33,axis=1)
gbst_19_f_a_uppl = np.percentile(gbst_19_f_a,67,axis=1)
gbst_19_f_a_upp = np.percentile(gbst_19_f_a,83,axis=1)
gbst_19_f_a_med = np.median(gbst_19_f_a,axis=1)
gbst_26_f_a_low = np.percentile(gbst_26_f_a,17,axis=1)
gbst_26_f_a_lowu = np.percentile(gbst_26_f_a,33,axis=1)
gbst_26_f_a_uppl = np.percentile(gbst_26_f_a,67,axis=1)
gbst_26_f_a_upp = np.percentile(gbst_26_f_a,83,axis=1)
gbst_26_f_a_med = np.median(gbst_26_f_a,axis=1)
gbst_70_f_a_low = np.percentile(gbst_70_f_a,17,axis=1)
gbst_70_f_a_lowu = np.percentile(gbst_70_f_a,33,axis=1)
gbst_70_f_a_uppl = np.percentile(gbst_70_f_a,67,axis=1)
gbst_70_f_a_upp = np.percentile(gbst_70_f_a,83,axis=1)
gbst_70_f_a_med = np.median(gbst_70_f_a,axis=1)
gbst_85_f_a_low = np.percentile(gbst_85_f_a,17,axis=1)
gbst_85_f_a_lowu = np.percentile(gbst_85_f_a,33,axis=1)
gbst_85_f_a_uppl = np.percentile(gbst_85_f_a,67,axis=1)
gbst_85_f_a_upp = np.percentile(gbst_85_f_a,83,axis=1)
gbst_85_f_a_med = np.median(gbst_85_f_a,axis=1)


### ------- Plot results ----------

years = np.linspace(1850,2100,251)

plt.figure(figsize=(7,5.5))
plt.title('Global mean surface temperature change in\nobservations and '+\
          'projections from FaIR',y=1.03,fontsize=16)
plt.plot(years_f,gbst_85_f_a_med,color='sienna',\
         label='Worst case no mitigation')
plt.fill_between(years_f,gbst_85_f_a_low,gbst_85_f_a_upp,edgecolor='',\
                 facecolor='sienna',alpha=0.4)
plt.plot(years_f,gbst_70_f_a_med,color='orange',\
         label='Average no mitigation')
plt.fill_between(years_f,gbst_70_f_a_low,gbst_70_f_a_upp,edgecolor='',\
                 facecolor='orange',alpha=0.35)
plt.plot(years_f,gbst_NDC_f_a_med,color='darkgrey',\
         label='NDCs')
plt.fill_between(years_f,gbst_NDC_f_a_low,gbst_NDC_f_a_upp,edgecolor='',\
                 facecolor='silver',alpha=0.3)
plt.plot(years_f,gbst_26_f_a_med,color='dodgerblue',\
         label='Below 2$^{\circ}$C')
plt.fill_between(years_f,gbst_26_f_a_low,gbst_26_f_a_upp,edgecolor='',\
                 facecolor='dodgerblue',alpha=0.3)
plt.plot(years_f,gbst_19_f_a_med,color='green',\
         label='Below 1.5$^{\circ}$C')
plt.fill_between(years_f,gbst_19_f_a_low,gbst_19_f_a_upp,edgecolor='',\
                 facecolor='green',alpha=0.3)
plt.plot(years_obs,temp_obs_a,color='black',linestyle='-',\
         linewidth=1,label='Observed warming')
plt.plot(years_obs,temp_AWI_a,color='red',linestyle='-',\
         label='Anthropogenic warming')
plt.plot(years,np.ones(len(years))*(1.5-offset_AWI),'k--',\
         linewidth=1)
plt.plot(years,np.ones(len(years))*(2-offset_AWI),'k-.',\
         linewidth=1)
plt.text(1997,1.5-offset_AWI+0.05,'1.5$^{\circ}$C level',\
         fontsize=13,ha='left',va='bottom',color='k')
plt.text(1997,2.0-offset_AWI+0.05,'2.0$^{\circ}$C level',\
         fontsize=13,ha='left',va='bottom',color='k')
plt.xlabel('Year',fontsize=14)
plt.ylabel('Temperature relative to 2000-2019 ($^{\circ}$C)',\
           fontsize=14)
plt.xlim([1995,2100])
plt.ylim([-0.5,4.5])
plt.tick_params(labelsize=14)
plt.legend(loc='upper left',fontsize=12)
plt.tight_layout()
plt.show()


### --------- Print results for Supp Table 2 --------------

print('Timing of crossing 1.5C (17%, 33%, median, 67%, 83%)')
print('-----------------------------------------------')
print('SSP1-1.9 results:')
ind_ear = np.where(gbst_19_f_a_upp >= 1.5-offset_AWI)[0]
if len(ind_ear) > 0:
    print('earliest (17%) = ',years_f[ind_ear[0]])
ind_ear = np.where(gbst_19_f_a_uppl >= 1.5-offset_AWI)[0]
if len(ind_ear) > 0:
    print('33% = ',years_f[ind_ear[0]])
ind_med = np.where(gbst_19_f_a_med >= 1.5-offset_AWI)[0]
if len(ind_med) > 0:
    print('median = ',years_f[ind_med[0]])
ind_lat = np.where(gbst_19_f_a_lowu >= 1.5-offset_AWI)[0]
if len(ind_lat) > 0:
    print('67% = ',years_f[ind_lat[0]])
ind_lat = np.where(gbst_19_f_a_low >= 1.5-offset_AWI)[0]
if len(ind_lat) > 0:
    print('latest (83%) = ',years_f[ind_lat[0]])
print('--------------------------------------------')
print('SSP1-2.6 results:')
ind_ear = np.where(gbst_26_f_a_upp >= 1.5-offset_AWI)[0]
if len(ind_ear) > 0:
    print('earliest (17%) = ',years_f[ind_ear[0]])
ind_ear = np.where(gbst_26_f_a_uppl >= 1.5-offset_AWI)[0]
if len(ind_ear) > 0:
    print('33% = ',years_f[ind_ear[0]])
ind_med = np.where(gbst_26_f_a_med >= 1.5-offset_AWI)[0]
if len(ind_med) > 0:
    print('median = ',years_f[ind_med[0]])
ind_lat = np.where(gbst_26_f_a_lowu >= 1.5-offset_AWI)[0]
if len(ind_lat) > 0:
    print('67% = ',years_f[ind_lat[0]])
ind_lat = np.where(gbst_26_f_a_low >= 1.5-offset_AWI)[0]
if len(ind_lat) > 0:
    print('latest (83%) = ',years_f[ind_lat[0]])
print('--------------------------------------------')
print('NDCs results:')
ind_ear = np.where(gbst_NDC_f_a_upp >= 1.5-offset_AWI)[0]
if len(ind_ear) > 0:
    print('earliest (17%) = ',years_f[ind_ear[0]])
ind_ear = np.where(gbst_NDC_f_a_uppl >= 1.5-offset_AWI)[0]
if len(ind_ear) > 0:
    print('33% = ',years_f[ind_ear[0]])
ind_med = np.where(gbst_NDC_f_a_med >= 1.5-offset_AWI)[0]
if len(ind_med) > 0:
    print('median = ',years_f[ind_med[0]])
ind_lat = np.where(gbst_NDC_f_a_lowu >= 1.5-offset_AWI)[0]
if len(ind_lat) > 0:
    print('67% = ',years_f[ind_lat[0]])
ind_lat = np.where(gbst_NDC_f_a_low >= 1.5-offset_AWI)[0]
if len(ind_lat) > 0:
    print('latest (83%) = ',years_f[ind_lat[0]])
print('--------------------------------------------')
print('SSP3-7.0 results:')
ind_ear = np.where(gbst_70_f_a_upp >= 1.5-offset_AWI)[0]
if len(ind_ear) > 0:
    print('earliest (17%) = ',years_f[ind_ear[0]])
ind_ear = np.where(gbst_70_f_a_uppl >= 1.5-offset_AWI)[0]
if len(ind_ear) > 0:
    print('33% = ',years_f[ind_ear[0]])
ind_med = np.where(gbst_70_f_a_med >= 1.5-offset_AWI)[0]
if len(ind_med) > 0:
    print('median = ',years_f[ind_med[0]])
ind_lat = np.where(gbst_70_f_a_lowu >= 1.5-offset_AWI)[0]
if len(ind_lat) > 0:
    print('67% = ',years_f[ind_lat[0]])
ind_lat = np.where(gbst_70_f_a_low >= 1.5-offset_AWI)[0]
if len(ind_lat) > 0:
    print('latest (83%) = ',years_f[ind_lat[0]])
print('--------------------------------------------')
print('SSP5-8.5 results:')
ind_ear = np.where(gbst_85_f_a_upp >= 1.5-offset_AWI)[0]
if len(ind_ear) > 0:
    print('earliest (17%) = ',years_f[ind_ear[0]])
ind_ear = np.where(gbst_85_f_a_uppl >= 1.5-offset_AWI)[0]
if len(ind_ear) > 0:
    print('33% = ',years_f[ind_ear[0]])
ind_med = np.where(gbst_85_f_a_med >= 1.5-offset_AWI)[0]
if len(ind_med) > 0:
    print('median = ',years_f[ind_med[0]])
ind_lat = np.where(gbst_85_f_a_lowu >= 1.5-offset_AWI)[0]
if len(ind_lat) > 0:
    print('67% = ',years_f[ind_lat[0]])
ind_lat = np.where(gbst_85_f_a_low >= 1.5-offset_AWI)[0]
if len(ind_lat) > 0:
    print('latest (83%) = ',years_f[ind_lat[0]])
print('--------------------------------------------')
