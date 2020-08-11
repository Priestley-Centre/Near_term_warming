from __future__ import division
import numpy as np
from scipy import stats
from sklearn.utils import shuffle
import numpy.random as npr

"""
Created on Thurs 13 Feb 2020

@author: Christine McKenna

=========================================================================
Purpose: Computes results for Table 1b.

         Calculates the probability that mitigation is necessary and
         sufficient to cause a trend reduction in FaIR projections 
         for 2021-2040 as compared to the obs trend over 2000-2019.
         Method is similar to Marotzke 2019. 

         Also saves distributions for plotting Figure 2c..
=========================================================================
"""

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
nt_f = len(gsat_trend_f_19)

# Add internal variability to FaIR trends 
gsat_trend_f_var_NDC  = np.expand_dims(gsat_trend_f_NDC,1) + \
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


### ------ Find trend difference between 2021-2040 in --------
### -------------- FaIR and 2000-2019 in obs -----------------

# Create obs array to minus from FaIR trends
obs = np.array([0.224,0.254,0.192,0.207]) # BE, GI, HadCRUT, CW 
obs_re1 = np.zeros(nt_f*nt_var)
obs_re2 = np.zeros(nt_f*nt_var)
obs_re3 = np.zeros(nt_f*nt_var)
obs_re4 = np.zeros(nt_f*nt_var)

# Randomly select obs
for i in xrange(nt_f*nt_var):
    idx1 = npr.randint(0,4)
    idx2 = npr.randint(0,4)
    idx3 = npr.randint(0,4)
    idx4 = npr.randint(0,4)
    obs_re1[i] = obs[idx1]
    obs_re2[i] = obs[idx2]
    obs_re3[i] = obs[idx3]
    obs_re4[i] = obs[idx4]

# For each FaIR realisation, randomly subtract one of the
# four observational estimates of the 2000-2019 trend
gsat_trend_f_var_NDC_diff = shuffle(gsat_trend_f_var_NDC) - \
                            obs_re1
gsat_trend_f_var_19_diff = shuffle(gsat_trend_f_var_19) - \
                           obs_re1
gsat_trend_f_var_26_diff = shuffle(gsat_trend_f_var_26) - \
                           obs_re2
gsat_trend_f_var_70_diff = shuffle(gsat_trend_f_var_70) - \
                           obs_re3
gsat_trend_f_var_85_diff = shuffle(gsat_trend_f_var_85) - \
                           obs_re4


### ------ Calculate probabilities -------

# Probability of a trend reduction
PNDC = len(np.where(gsat_trend_f_var_NDC_diff < 0)[0])/\
       len(gsat_trend_f_var_NDC_diff)
P19 = len(np.where(gsat_trend_f_var_19_diff < 0)[0])/\
      len(gsat_trend_f_var_19_diff)
P26 = len(np.where(gsat_trend_f_var_26_diff < 0)[0])/\
      len(gsat_trend_f_var_26_diff)
P70 = len(np.where(gsat_trend_f_var_70_diff < 0)[0])/\
      len(gsat_trend_f_var_70_diff)
P85 = len(np.where(gsat_trend_f_var_85_diff < 0)[0])/\
      len(gsat_trend_f_var_85_diff)

# Probability that mitigation is both sufficient and 
# necessary to cause a trend reduction
Pns_NDC_85 = PNDC - P85
Pns_19_85 = P19 - P85
Pns_26_85 = P26 - P85
Pns_NDC_70 = PNDC - P70
Pns_19_70 = P19 - P70
Pns_26_70 = P26 - P70

# Save distributions for plotting Figure 2c
np.save(savedir+'/gsat_trend_diff_obs_19.npy',gsat_trend_f_var_19_diff)
np.save(savedir+'/gsat_trend_diff_obs_26.npy',gsat_trend_f_var_26_diff)
np.save(savedir+'/gsat_trend_diff_obs_NDC.npy',gsat_trend_f_var_NDC_diff)
np.save(savedir+'/gsat_trend_diff_obs_70.npy',gsat_trend_f_var_70_diff)
np.save(savedir+'/gsat_trend_diff_obs_85.npy',gsat_trend_f_var_85_diff)



