import numpy as np
from scipy import stats

"""
Created on Thurs 13 Feb 2020

@author: Christine McKenna

=========================================================================
Purpose: Computes results for Table 1a.

         Calculates the probability that a realisation in 
         arr_mit is less than in arr_nomit by a given
         proportion alpha. Essentially tells us the likelihood that the
         observed future trend will be smaller under mitigation 
         than under no mitigation by the given amount.

         Also saves distributions for plotting Figure 2a and 2b.
=========================================================================
"""

# Load in required functions
exec(open('Priestley-Centre/Near_term_warming/analysis_figure_code/'+\
          'Figure2_Table1/montecarlo.py').read())

# Required directories
loaddir_IV = 'Priestley-Centre/Near_term_warming/IV_data'
loaddir_FAIR = 'Priestley-Centre/Near_term_warming/FaIR_data/temps'
savedir = 'Priestley-Centre/Near_term_warming/analysis_figure_code/'+\
          'Figure2_Table1/saved_arrays'


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


### ------ Calculate 2021-2040 FaIR trends ------


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
gsat_trend_f_var_19 = np.reshape(gsat_trend_f_var_19,nt_f*nt_var) 
gsat_trend_f_var_26 = np.reshape(gsat_trend_f_var_26,nt_f*nt_var) 
gsat_trend_f_var_70 = np.reshape(gsat_trend_f_var_70,nt_f*nt_var) 
gsat_trend_f_var_85 = np.reshape(gsat_trend_f_var_85,nt_f*nt_var) 


### ------ Calculate probabilities -------

alpha = 0  # or 0.2, 0.4
[P_19_85,diffs_19_85] = montecarlo(gsat_trend_f_var_19,\
                        gsat_trend_f_var_85,alpha=alpha)
[P_26_85,diffs_26_85] = montecarlo(gsat_trend_f_var_26,\
                        gsat_trend_f_var_85,alpha=alpha)
[P_NDC_85,diffs_NDC_85] = montecarlo(gsat_trend_f_var_NDC,\
                          gsat_trend_f_var_85,alpha=alpha)
[P_19_70,diffs_19_70] = montecarlo(gsat_trend_f_var_19,\
                        gsat_trend_f_var_70,alpha=alpha)
[P_26_70,diffs_26_70] = montecarlo(gsat_trend_f_var_26,\
                        gsat_trend_f_var_70,alpha=alpha)
[P_NDC_70,diffs_NDC_70] = montecarlo(gsat_trend_f_var_NDC,\
                          gsat_trend_f_var_70,alpha=alpha)


### ------ Save distributions for Figure 2a and 2b -----

if alpha == 0:
    np.save(savedir+'/gsat_trend_diff_19_85.npy',diffs_19_85)
    np.save(savedir+'/gsat_trend_diff_26_85.npy',diffs_26_85)
    np.save(savedir+'/gsat_trend_diff_NDC_85.npy',diffs_NDC_85)
    np.save(savedir+'/gsat_trend_diff_19_70.npy',diffs_19_70)
    np.save(savedir+'/gsat_trend_diff_26_70.npy',diffs_26_70)
    np.save(savedir+'/gsat_trend_diff_NDC_70.npy',diffs_NDC_70)

