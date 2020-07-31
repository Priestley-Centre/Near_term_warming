import numpy as np
from scipy import stats

"""
Created on Tues Jan 28 11:59 2020

@author: Christine McKenna

=========================================================================
Purpose: Outputs FaIR trend + IV data required to plot Supp Fig 7
=========================================================================
"""

# Required functions
exec(open('Priestley-Centre/Near_term_warming/analysis_figure_code/'+\
          'my_boxplot.py').read())

# Required directories
loaddir_IV_CMIP = 'Priestley-Centre/Near_term_warming/analysis_figure_'+\
                  'code/SuppFig7/saved_data'
loaddir_IV_obs = 'Priestley-Centre/Near_term_warming/IV_data'
loaddir_FAIR = 'Priestley-Centre/Near_term_warming/FaIR_data/temps'
savedir = 'Priestley-Centre/Near_term_warming/analysis_figure_code/'+\
          'SuppFig7/saved_data'

# Choose output
IV = 'obs' # 'obs' or 'model'
obs = 'HadOST' # 'HadOST', 'Be' or 'CW'
model = 'BCC-CSM2-MR' # 'BCC-CSM2-MR' or 'MIROC-ES2L' 


### ------ Load in FaIR data ------

gsat_NDC_f = np.loadtxt(loaddir_FAIR+'/NDC_temps.csv',delimiter=',',\
                        dtype='str')[1:,1:].astype('float')
gsat_19_f = np.loadtxt(loaddir_FAIR+'/ssp119_temps.csv',delimiter=',',\
                       dtype='str')[1:,1:].astype('float')
gsat_26_f = np.loadtxt(loaddir_FAIR+'/ssp126_temps.csv',delimiter=',',\
                       dtype='str')[1:,1:].astype('float')
gsat_70_f = np.loadtxt(loaddir_FAIR+'/ssp370_temps.csv',delimiter=',',\
                       dtype='str')[1:,1:].astype('float')
gsat_85_f = np.loadtxt(loaddir_FAIR+'/ssp585_temps.csv',delimiter=',',\
                       dtype='str')[1:,1:].astype('float')
years_f = np.loadtxt(loaddir_FAIR+'/NDC_temps.csv',delimiter=',',\
                     dtype='str')[1:,0].astype('float')


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


### ------ Load in estimate of internal variability ---------

if IV == 'obs':
    int_var = np.load(loaddir_IV_obs+'/gsat_20ytrends_Haus_res_'+obs+'.npy')
elif IV == 'model':
    int_var = np.load(loaddir_IV_CMIP+'/gsat_20ytrends_CMIP6_piControl'+\
                      '_'+model+'.npy')
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

# Find min and max
minmax = np.array([[np.min(gsat_trend_f_var_NDC),\
                    np.max(gsat_trend_f_var_NDC)],\
                   [np.min(gsat_trend_f_var_19),\
                    np.max(gsat_trend_f_var_19)],\
                   [np.min(gsat_trend_f_var_26),\
                    np.max(gsat_trend_f_var_26)],\
                   [np.min(gsat_trend_f_var_70),\
                    np.max(gsat_trend_f_var_70)],\
                   [np.min(gsat_trend_f_var_85),\
                    np.max(gsat_trend_f_var_85)]])


### -------- Save for plotting IV estimate comparison -------

if IV == 'obs':
    np.save(savedir+'/stats_trend_f_'+obs+'IV.npy',stats_trend_f)
    np.save(savedir+'/minmax_trend_f_'+obs+'IV.npy',minmax)
elif IV == 'model':
    np.save(savedir+'/stats_trend_f_'+model+'_IV.npy',stats_trend_f)
    np.save(savedir+'/minmax_trend_f_'+model+'IV.npy',minmax)


