import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

"""
Created on Tues Jan 28 11:59 2020

@author: Christine McKenna

=========================================================================
Purpose: Plots Figure 1 for near-term warming paper, showing that while
         near-term GSAT anomaly is not different between SSP's, the
         near-term GSAT trend is. 
 
         LHS plot shows GSAT trend for 2021-2040, for FaIR plus IV
         estimated from HadOST residuals in Haustein et al. 2019, and 
         constrained CMIP6 (from Tokarska et al. 2020).  

         RHS plot shows GSAT anomaly for 2021-2040 wrt 1995-2014, for 
         FaIR plus IV and constrained CMIP6.

         Compares trend to max in observations; 0.265 deg C / decade
         based on HadCRUT4.6, GISTEMPv4, HadOST, CWv2.  
=========================================================================
"""

# Required functions
exec(open('Priestley-Centre/Near_term_warming/analysis_figure_code/'+\
          'my_boxplot.py').read())

# Required directories
loaddir_IV = 'Priestley-Centre/Near_term_warming/IV_data'
loaddir_FAIR = 'Priestley-Centre/Near_term_warming/FaIR_data/temps'
loaddir_CMIP = 'Priestley-Centre/Near_term_warming/constrained_CMIP6_data'


### ------ Load in FaIR data ------

gsat_NDC_f = np.loadtxt(loaddir_FAIR+'/NDC_temps.csv',delimiter=',',\
                         dtype='float')[:,1:]
gsat_19_f = np.loadtxt(loaddir_FAIR+'/ssp119_temps.csv',delimiter=',',\
                       dtype='float')[:,1:]
gsat_26_f = np.loadtxt(loaddir_FAIR+'/ssp126_temps.csv',delimiter=',',\
                       dtype='float')[:,1:]
gsat_70_f = np.loadtxt(loaddir_FAIR+'/ssp370_temps.csv',delimiter=',',\
                       dtype='float')[:,1:]
gsat_85_f = np.loadtxt(loaddir_FAIR+'/ssp585_temps.csv',delimiter=',',\
                       dtype='float')[:,1:]
years_f = np.loadtxt(loaddir_FAIR+'/NDC_temps.csv',delimiter=',',\
                     dtype='float')[:,0]


### ------ Calculate FaIR means for 1995-2014, 2021-2040 ------

# Find years 1995-2014 and 2021-2040
ind1995 = np.where(years_f == 1995.)[0][0]
ind2014 = np.where(years_f == 2014.)[0][0]
ind2021 = np.where(years_f == 2021.)[0][0]
ind2040 = np.where(years_f == 2040.)[0][0]

# Calculate
gsat_NDC_f_anom = np.mean(gsat_NDC_f[ind2021:ind2040+1],axis=0) - \
                  np.mean(gsat_NDC_f[ind1995:ind2014+1],axis=0)
gsat_19_f_anom  = np.mean(gsat_19_f[ind2021:ind2040+1],axis=0) - \
                  np.mean(gsat_19_f[ind1995:ind2014+1],axis=0)
gsat_26_f_anom  = np.mean(gsat_26_f[ind2021:ind2040+1],axis=0) - \
                  np.mean(gsat_26_f[ind1995:ind2014+1],axis=0)
gsat_70_f_anom  = np.mean(gsat_70_f[ind2021:ind2040+1],axis=0) - \
                  np.mean(gsat_70_f[ind1995:ind2014+1],axis=0)
gsat_85_f_anom  = np.mean(gsat_85_f[ind2021:ind2040+1],axis=0) - \
                  np.mean(gsat_85_f[ind1995:ind2014+1],axis=0)


### ------ Load in estimate of internal variability from ---------
### ------ Haustein et al 2019 residuals and add to --------------
### -------------------- FaIR anoms -----------------------------            

# Load in internal variability estimate
int_var_tmp = np.load(loaddir_IV+'/gsat_20ymeans_Haus_res_'+\
                      'HadOST.npy')
nt_var_tmp = len(int_var_tmp)

# Preserve autocorrelation when calculating IV in difference
# between 20 year means (i.e. same separation as (2021-2040)-
# (1995-2014))
sep = ind2021 - ind1995
int_var = np.zeros(nt_var_tmp-sep)
for i in xrange(0,nt_var_tmp-sep):
    int_var[i] = int_var_tmp[i+sep] - int_var_tmp[i]
nt_var = len(int_var)
nt_f = len(gsat_NDC_f_anom)

# Add internal variability to FaIR anoms 
gsat_NDC_f_anom_var = np.expand_dims(gsat_NDC_f_anom,1) + \
                      np.expand_dims(int_var,0) 
gsat_19_f_anom_var  = np.expand_dims(gsat_19_f_anom,1) + \
                      np.expand_dims(int_var,0) 
gsat_26_f_anom_var = np.expand_dims(gsat_26_f_anom,1) + \
                     np.expand_dims(int_var,0) 
gsat_70_f_anom_var = np.expand_dims(gsat_70_f_anom,1) + \
                     np.expand_dims(int_var,0) 
gsat_85_f_anom_var = np.expand_dims(gsat_85_f_anom,1) + \
                     np.expand_dims(int_var,0) 
         
# Collapse into 1d
gsat_NDC_f_anom_var = np.reshape(gsat_NDC_f_anom_var,nt_f*nt_var) 
gsat_19_f_anom_var = np.reshape(gsat_19_f_anom_var,nt_f*nt_var) 
gsat_26_f_anom_var = np.reshape(gsat_26_f_anom_var,nt_f*nt_var) 
gsat_70_f_anom_var = np.reshape(gsat_70_f_anom_var,nt_f*nt_var) 
gsat_85_f_anom_var = np.reshape(gsat_85_f_anom_var,nt_f*nt_var) 

# Calculate statistics for boxplot 
stats_anom_f = {}
stats_anom_f = my_boxplot_stats(gsat_NDC_f_anom_var,stats_anom_f,\
                                'N',fliers=False)
stats_anom_f = my_boxplot_stats(gsat_19_f_anom_var,stats_anom_f,\
                                '19',fliers=False)
stats_anom_f = my_boxplot_stats(gsat_26_f_anom_var,stats_anom_f,\
                                '26',fliers=False)
stats_anom_f = my_boxplot_stats(gsat_70_f_anom_var,stats_anom_f,\
                                '70',fliers=False)
stats_anom_f = my_boxplot_stats(gsat_85_f_anom_var,stats_anom_f,\
                                '85',fliers=False)


### ------ Calculate FaIR trends ------

# Find years 2021-2040
ind1 = np.where(years_f == 2021.)[0][0]
ind2 = np.where(years_f == 2040.)[0][0]

# Calculate /year trends
gsat_trend_f_NDC = np.zeros(500)
gsat_trend_f_19 = np.zeros(500)
gsat_trend_f_26 = np.zeros(500)
gsat_trend_f_70 = np.zeros(500)
gsat_trend_f_85 = np.zeros(500)

for mem in xrange(0,500):
    [m,c,r,p,SE] = stats.linregress(years_f[ind1:ind2+1],\
                                    gsat_NDC_f[ind1:ind2+1,mem])
    gsat_trend_f_NDC[mem] = m    
    [m,c,r,p,SE] = stats.linregress(years_f[ind1:ind2+1],\
                                    gsat_19_f[ind1:ind2+1,mem])
    gsat_trend_f_19[mem] = m    
    [m,c,r,p,SE] = stats.linregress(years_f[ind1:ind2+1],\
                                    gsat_26_f[ind1:ind2+1,mem])
    gsat_trend_f_26[mem] = m    
    [m,c,r,p,SE] = stats.linregress(years_f[ind1:ind2+1],\
                                    gsat_70_f[ind1:ind2+1,mem])
    gsat_trend_f_70[mem] = m    
    [m,c,r,p,SE] = stats.linregress(years_f[ind1:ind2+1],\
                                    gsat_85_f[ind1:ind2+1,mem])
    gsat_trend_f_85[mem] = m    

# Calculate decadal trend
gsat_trend_f_NDC = gsat_trend_f_NDC*10
gsat_trend_f_19 = gsat_trend_f_19*10
gsat_trend_f_26 = gsat_trend_f_26*10
gsat_trend_f_70 = gsat_trend_f_70*10
gsat_trend_f_85 = gsat_trend_f_85*10


### ------ Load in estimate of internal variability from ---------
### ------ Haustein et al 2019 residuals and add to --------------
### -------------------- FaIR trends -----------------------------            

# Load in internal variability estimate
int_var = np.load(loaddir_IV+'/gsat_20ytrends_Haus_res_HadOST.npy')
nt_var = len(int_var)
nt_f = len(gsat_trend_f_NDC)

# Add internal variability to FaIR trends 
gsat_trend_f_var_NDC = np.expand_dims(gsat_trend_f_NDC,1) + \
                       np.expand_dims(int_var,0) 
gsat_trend_f_var_19  = np.expand_dims(gsat_trend_f_19,1) + \
                       np.expand_dims(int_var,0) 
gsat_trend_f_var_26  = np.expand_dims(gsat_trend_f_26,1) + \
                       np.expand_dims(int_var,0) 
gsat_trend_f_var_70  = np.expand_dims(gsat_trend_f_70,1) + \
                       np.expand_dims(int_var,0) 
gsat_trend_f_var_85  = np.expand_dims(gsat_trend_f_85,1) + \
                       np.expand_dims(int_var,0) 
         
# Collapse into 1d
gsat_trend_f_var_NDC = np.reshape(gsat_trend_f_var_NDC,nt_f*nt_var) 
gsat_trend_f_var_19  = np.reshape(gsat_trend_f_var_19,nt_f*nt_var) 
gsat_trend_f_var_26  = np.reshape(gsat_trend_f_var_26,nt_f*nt_var) 
gsat_trend_f_var_70  = np.reshape(gsat_trend_f_var_70,nt_f*nt_var) 
gsat_trend_f_var_85  = np.reshape(gsat_trend_f_var_85,nt_f*nt_var) 

# Calculate statistics for boxplot 
stats_trend_f = {}
stats_trend_f = my_boxplot_stats(gsat_trend_f_var_NDC,stats_trend_f,\
                                 'N',fliers=False)
stats_trend_f = my_boxplot_stats(gsat_trend_f_var_19,stats_trend_f,\
                                 '19',fliers=False)
stats_trend_f = my_boxplot_stats(gsat_trend_f_var_26,stats_trend_f,\
                                 '26',fliers=False)
stats_trend_f = my_boxplot_stats(gsat_trend_f_var_70,stats_trend_f,\
                                 '70',fliers=False)
stats_trend_f = my_boxplot_stats(gsat_trend_f_var_85,stats_trend_f,\
                                 '85',fliers=False)


### ------ Load in constrained CMIP6 anoms and trends ------

stats_anom_c = np.load(loaddir_CMIP+'/gsat_anom_CMIP6_con.npy',\
                       allow_pickle='TRUE').item()
stats_trend_c = np.load(loaddir_CMIP+'/gsat_trend_CMIP6_con.npy',\
                        allow_pickle='TRUE').item()


### ----------------------------------
###            Plot trends
### ----------------------------------

colors=['grey','green','dodgerblue','lightblue','orange',\
        'moccasin','sienna','rosybrown']
fig1,[ax1,ax2] = plt.subplots(1,2,figsize=(13,8))

# GSAT trend
ax1.set_title('(a) 2021-2040 GSAT trend',y=1.02,fontsize=20)
bplot1 = ax1.bxp([stats_trend_f['N'],stats_trend_f['19'],\
                 stats_trend_f['26'],stats_trend_c['26'],\
                 stats_trend_f['70'],stats_trend_c['70'],\
                 stats_trend_f['85'],stats_trend_c['85']],\
                 positions=[1.0,1.8,2.6,3.0,3.8,4.2,5.0,5.4],\
                 patch_artist=True,flierprops=dict(marker='.'),\
                 widths=np.ones([8])*0.25)
plt.setp(bplot1['medians'], color='k')
x=0
for patch in bplot1['boxes']:
    patch.set_facecolor(colors[x])
    x += 1
ax1.scatter([1.0,1.0,1.8,1.8,2.6,2.6,3.8,3.8,5.0,5.0],[np.min(\
            gsat_trend_f_var_NDC),np.max(gsat_trend_f_var_NDC),\
            np.min(gsat_trend_f_var_19),np.max(gsat_trend_f_var_19),\
            np.min(gsat_trend_f_var_26),np.max(gsat_trend_f_var_26),\
            np.min(gsat_trend_f_var_70),np.max(gsat_trend_f_var_70),\
            np.min(gsat_trend_f_var_85),np.max(gsat_trend_f_var_85)],\
            marker='x',s=25,c='k')
ax1.fill_between([0.5,5.9],0.254,0.287,edgecolor='',facecolor='grey',\
                 alpha=0.3,zorder=0)
ax1.plot([0.5,5.9],[0.265,0.265],color='black',linewidth=1,zorder=0)
ax1.plot([0.5,5.9],[0,0],'--',color='black',linewidth=1,zorder=0)
ax1.set_xlim([0.5,5.9])
ax1.set_xticks([1.0,1.8,2.8,4.0,5.2])
ax1.xaxis.set_ticklabels(['NDCs','Below\n1.5$^{\circ}$C',\
                          'Below\n2$^{\circ}$C',\
                          'Aver-\nage',\
                          'Worst\ncase'])
ax1.set_ylim([-0.2,0.9])
ax1.set_yticks([-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])
ax1.set_ylabel('$^{\circ}$C / decade',fontsize=17)
ax1.tick_params(labelsize=17)

# GSAT anomaly
ax2.set_title('(b) 2021-2040 GSAT anomaly',y=1.02,fontsize=20)
bplot2 = ax2.bxp([stats_anom_f['N'],stats_anom_f['19'],\
                 stats_anom_f['26'],stats_anom_c['26'],\
                 stats_anom_f['70'],stats_anom_c['70'],\
                 stats_anom_f['85'],stats_anom_c['85']],\
                 positions=[1.0,1.8,2.6,3.0,3.8,4.2,5.0,5.4],\
                 patch_artist=True,flierprops=dict(marker='.'),\
                 widths=np.ones([8])*0.25)
plt.setp(bplot2['medians'], color='k')
x=0
for patch in bplot2['boxes']:
    patch.set_facecolor(colors[x])
    x += 1
ax2.scatter([1.0,1.0,1.8,1.8,2.6,2.6,3.8,3.8,5.0,5.0],[np.min(\
            gsat_NDC_f_anom_var),np.max(gsat_NDC_f_anom_var),\
            np.min(gsat_19_f_anom_var),np.max(gsat_19_f_anom_var),\
            np.min(gsat_26_f_anom_var),np.max(gsat_26_f_anom_var),\
            np.min(gsat_70_f_anom_var),np.max(gsat_70_f_anom_var),\
            np.min(gsat_85_f_anom_var),np.max(gsat_85_f_anom_var)],\
            marker='x',s=25,c='k')
ax2.plot([0.5,5.9],[0,0],'-',color='grey',linewidth=1,zorder=0)
ax2.set_xlim([0.5,5.9])
ax2.set_xticks([1.0,1.8,2.8,4.0,5.2])
ax2.xaxis.set_ticklabels(['NDCs','Below\n1.5$^{\circ}$C',\
                          'Below\n2$^{\circ}$C',\
                          'Aver-\nage',\
                          'Worst\ncase'])
ax2.set_ylim([0,1.83])
ax2.set_yticks([0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8])
ax2.set_ylabel('$^{\circ}$C',fontsize=17)
ax2.tick_params(labelsize=17)


# Show (note this Figure is then edited in Inkscape to
# improve layout, add a legend, smarten up)
plt.subplots_adjust(top=0.93,bottom=0.08,left=0.08,right=0.88,\
                    wspace=0.31)
plt.show()

