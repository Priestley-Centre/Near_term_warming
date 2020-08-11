import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

"""
Created on Tues Jan 28 11:59 2020

@author: Christine McKenna

=========================================================================
Purpose: Plots Figure 3 for near-term warming paper
=========================================================================
"""

# Required directories
loaddir_FAIR = 'Priestley-Centre/Near_term_warming/FaIR_data/temps'
loaddir_obs = 'Priestley-Centre/Near_term_warming/Figure3/saved_arrays'
loaddir_IV = loaddir_obs


### ------ Load in range of max obs trends ------

obs_upper = np.load(loaddir_obs+'/obs_max_Ny_trends_upper.npy')
obs_lower = np.load(loaddir_obs+'/obs_max_Ny_trends_lower.npy')
obs_BE = np.load(loaddir_obs+'/obs_max_Ny_trends_BE.npy')
obs_Ha = np.load(loaddir_obs+'/obs_max_Ny_trends_Ha.npy')
obs_GI = np.load(loaddir_obs+'/obs_max_Ny_trends_GI.npy')
obs_CW = np.load(loaddir_obs+'/obs_max_Ny_trends_CW.npy')
obs_mean = np.mean([obs_BE,obs_Ha,obs_GI,obs_CW],axis=0)


### ------ Load in FaIR data ------

gsat_19_f = np.loadtxt(loaddir_FAIR+'/ssp119_temps.csv',delimiter=',',\
                       dtype='str')[1:,1:].astype('float')
gsat_26_f = np.loadtxt(loaddir_FAIR+'/ssp126_temps.csv',delimiter=',',\
                       dtype='str')[1:,1:].astype('float')
gsat_70_f = np.loadtxt(loaddir_FAIR+'/ssp370_temps.csv',delimiter=',',\
                       dtype='str')[1:,1:].astype('float')
gsat_85_f = np.loadtxt(loaddir_FAIR+'/ssp585_temps.csv',delimiter=',',\
                       dtype='str')[1:,1:].astype('float')
years_f = np.loadtxt(loaddir_FAIR+'/ssp119_temps.csv',delimiter=',',\
                     dtype='str')[1:,0].astype('float')


### ------ Calculate FaIR trends and add internal variability ------

# Load in internal variability estimate
int_var = np.load(loaddir_IV+'/gsat_Nytrends_Haus_res_HadOST.npy')

# Find year 2021 (always the start point)
ind1 = np.where(years_f == 2021.)[0][0]

# To hold median, 17% and 83% percentiles
gsat_stats_f_19 = np.zeros([41,3])
gsat_stats_f_26 = np.zeros([41,3])
gsat_stats_f_70 = np.zeros([41,3])
gsat_stats_f_85 = np.zeros([41,3])

# To hold trends
gsat_trend_f_19 = np.zeros([500])
gsat_trend_f_26 = np.zeros([500])
gsat_trend_f_70 = np.zeros([500])
gsat_trend_f_85 = np.zeros([500])

# Calculate /year trends
nt_f = 500
for t_l in xrange(10,51):
    t = t_l - 10
    ind2 = ind1 + t_l
    nt_var = np.size(int_var,1)-t

    for mem in xrange(0,500):
        [m,c,r,p,SE] = stats.linregress(years_f[ind1:ind2],\
                                        gsat_19_f[ind1:ind2,mem])
        gsat_trend_f_19[mem] = m*10
        [m,c,r,p,SE] = stats.linregress(years_f[ind1:ind2],\
                                        gsat_26_f[ind1:ind2,mem])
        gsat_trend_f_26[mem] = m*10
        [m,c,r,p,SE] = stats.linregress(years_f[ind1:ind2],\
                                        gsat_70_f[ind1:ind2,mem])
        gsat_trend_f_70[mem] = m*10
        [m,c,r,p,SE] = stats.linregress(years_f[ind1:ind2],\
                                        gsat_85_f[ind1:ind2,mem])
        gsat_trend_f_85[mem] = m*10

    # Add int var
    gsat_trend_f_var_19 = np.expand_dims(gsat_trend_f_19,1) + \
                          np.expand_dims(int_var[t,:nt_var],0) 
    gsat_trend_f_var_26 = np.expand_dims(gsat_trend_f_26,1) + \
                          np.expand_dims(int_var[t,:nt_var],0) 
    gsat_trend_f_var_70 = np.expand_dims(gsat_trend_f_70,1) + \
                          np.expand_dims(int_var[t,:nt_var],0) 
    gsat_trend_f_var_85 = np.expand_dims(gsat_trend_f_85,1) + \
                          np.expand_dims(int_var[t,:nt_var],0) 
        
    # Collapse into 1d
    gsat_trend_f_var_19 = np.reshape(gsat_trend_f_var_19,nt_f*nt_var) 
    gsat_trend_f_var_26 = np.reshape(gsat_trend_f_var_26,nt_f*nt_var) 
    gsat_trend_f_var_70 = np.reshape(gsat_trend_f_var_70,nt_f*nt_var) 
    gsat_trend_f_var_85 = np.reshape(gsat_trend_f_var_85,nt_f*nt_var) 

    # Calculate percentiles
    gsat_stats_f_19[t,0] = np.percentile(gsat_trend_f_var_19,17)
    gsat_stats_f_26[t,0] = np.percentile(gsat_trend_f_var_26,17)
    gsat_stats_f_70[t,0] = np.percentile(gsat_trend_f_var_70,17)
    gsat_stats_f_85[t,0] = np.percentile(gsat_trend_f_var_85,17)
    gsat_stats_f_19[t,1] = np.median(gsat_trend_f_var_19)
    gsat_stats_f_26[t,1] = np.median(gsat_trend_f_var_26)
    gsat_stats_f_70[t,1] = np.median(gsat_trend_f_var_70)
    gsat_stats_f_85[t,1] = np.median(gsat_trend_f_var_85)
    gsat_stats_f_19[t,2] = np.percentile(gsat_trend_f_var_19,83)
    gsat_stats_f_26[t,2] = np.percentile(gsat_trend_f_var_26,83)
    gsat_stats_f_70[t,2] = np.percentile(gsat_trend_f_var_70,83)
    gsat_stats_f_85[t,2] = np.percentile(gsat_trend_f_var_85,83)


### ----------------------------------
###            Plot trends
### ----------------------------------

trend_lengths = np.linspace(10,50,41)
end_years = trend_lengths + 2020

fig,ax1 = plt.subplots(1,1,figsize=(7.08,5))
ax1.set_title('GSAT trends from FaIR starting in 2021\nfor '+\
              'different end years or trend lengths',y=1.02,fontsize=13)
plt.rcParams['axes.linewidth']=0.62

# Ranges
ax1.fill_between(end_years,gsat_stats_f_85[:,0],gsat_stats_f_85[:,2],
                 edgecolor='',facecolor='sienna',alpha=0.3,zorder=0)
ax1.fill_between(end_years,gsat_stats_f_70[:,0],gsat_stats_f_70[:,2],
                 edgecolor='',facecolor='orange',alpha=0.3,zorder=0)
ax1.fill_between(end_years,gsat_stats_f_26[:,0],gsat_stats_f_26[:,2],
                 edgecolor='',facecolor='dodgerblue',alpha=0.3,zorder=0)
ax1.fill_between(end_years,gsat_stats_f_19[:,0],gsat_stats_f_19[:,2],
                 edgecolor='',facecolor='green',alpha=0.3,zorder=0)
ax1.fill_between(end_years,obs_lower,obs_upper,edgecolor='',\
                 facecolor='black',alpha=0.2,zorder=2)

# Medians
ax1.plot(end_years,gsat_stats_f_85[:,1],label='Worst case no\nmitigation',\
         color='sienna',zorder=1)
ax1.plot(end_years,gsat_stats_f_70[:,1],label='Average no\nmitigation',\
         color='orange',zorder=1)
ax1.plot(end_years,gsat_stats_f_26[:,1],label='Below 2$^{\circ}$C',\
         color='dodgerblue',zorder=1)
ax1.plot(end_years,gsat_stats_f_19[:,1],label='Below 1.5$^{\circ}$C',\
         color='green',zorder=1)
ax1.plot(end_years,obs_mean,color='black',label='Max trend in obs',\
         zorder=2)

# Plot params
ax1.plot([2040.,2040.],[-0.05,0.63],'-',color='grey',linewidth=0.75)
ax1.plot(end_years,np.zeros([41]),'--',color='black',linewidth=0.75)
ax1.set_xlabel('End year',fontsize=10)
ax1.set_ylabel('$^{\circ}$C / decade',fontsize=10,labelpad=9)
ax1.set_xlim([2030,2070])
ax1.set_ylim([-0.05,0.55])
ax1.set_xticks([2030,2040,2050,2060,2070])
ax1.set_xticklabels(['-2030','-2040','-2050','-2060','-2070'])
ax1.tick_params(labelsize=10)
ax1.legend(loc='center right',fontsize=10,labelspacing=0.7,\
           bbox_to_anchor=(1.465,0.5))

# Second x-axis
ax2 = ax1.twiny()
ax2.xaxis.set_ticks_position('bottom')
ax2.xaxis.set_label_position('bottom')
ax2.spines['bottom'].set_position(('axes',-0.18))
ax2.set_frame_on(True)
ax2.patch.set_visible(False)
for sp in ax2.spines.itervalues():
    sp.set_visible(False)
ax2.spines['bottom'].set_visible(True)
ax2.set_xlim([10,50])
ax2.set_xticks([10,20,30,40,50])
ax2.set_xticklabels([10,20,30,40,50])
ax2.set_xlabel('Trend length (years)',fontsize=10)

# Adjust spacing and show
plt.subplots_adjust(top=0.88,bottom=0.22,left=0.1,right=0.7)
plt.show()

