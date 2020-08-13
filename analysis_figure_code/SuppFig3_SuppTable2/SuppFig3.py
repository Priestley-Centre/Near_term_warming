import numpy as np
import iris
from scipy import stats
import matplotlib.pyplot as plt

"""
Created on Tues Jul 21 22:00 2020

@author: Christine McKenna

=========================================================================
Purpose: Plots time-series of main emission components for each scenario
         considered in near-term warming paper - Supp Fig 3
=========================================================================
"""


# Required directories
loaddir_FAIR = 'Priestley-Centre/Near_term_warming/FaIR_data/emissions'


### ------ Load in FaIR data ------

# Emissions timeseries
years = np.loadtxt(loaddir_FAIR+'/ssp119_emissions.csv',\
                   delimiter=',',dtype='str')[1:,0].astype('float')
emi_19 = np.loadtxt(loaddir_FAIR+'/ssp119_emissions.csv',\
                    delimiter=',',dtype='str')[1:,1:12].astype('float')
emi_26 = np.loadtxt(loaddir_FAIR+'/ssp126_emissions.csv',\
                    delimiter=',',dtype='str')[1:,1:12].astype('float')
emi_70 = np.loadtxt(loaddir_FAIR+'/ssp370_emissions.csv',\
                    delimiter=',',dtype='str')[1:,1:12].astype('float')
emi_85 = np.loadtxt(loaddir_FAIR+'/ssp585_emissions.csv',\
                    delimiter=',',dtype='str')[1:,1:12].astype('float')
emi_NDC = np.loadtxt(loaddir_FAIR+'/ndc_emissions.csv',\
                     delimiter=',',dtype='str')[1:,1:12].astype('float')

# Separate into historical and scenarios
years_hist = years[:252]
years_scen = years[250:]
emi_hist = emi_19[:252]
emi_NDC = emi_NDC[250:]
emi_19 = emi_19[250:]
emi_26 = emi_26[250:]
emi_70 = emi_70[250:]
emi_85 = emi_85[250:]


### ------ Plot data ------

colors=['black','green','dodgerblue','grey','orange','sienna']
labels_plt = ['$\\bf{a}$  Net CO$_{2}$','$\\bf{b}$  CH$_{4}$',\
              '$\\bf{c}$  N$_{2}$O','$\\bf{d}$  SO$_{2}$',\
              '$\\bf{e}$  CO','$\\bf{f}$  NMVOC','$\\bf{g}$  NO$_{x}$',\
              '$\\bf{h}$  BC','$\\bf{i}$  OC','$\\bf{j}$  NH$_{3}$']
ylbls = ['GtC / year','MtCH$_{4}$ / year','MtN$_{2}$ / year','MtS / year',\
         'MtCO / year','MtNMVOC / year','MtN / year','MtC / year',\
         'MtC / year','MtNH$_{3}$ / year']

fig,axs = plt.subplots(4,3,figsize=(9,9))
fig.suptitle('Emissions pathways used in FaIR simulations',fontsize=18)
axs = axs.ravel()

# Plot total
axs[0].set_title(labels_plt[0],fontsize=13,loc='left')
axs[0].plot(years_hist,emi_hist[:,0]+emi_hist[:,1],color=colors[0])
axs[0].plot(years_scen,emi_19[:,0]+emi_19[:,1],color=colors[1])
axs[0].plot(years_scen,emi_26[:,0]+emi_26[:,1],color=colors[2])
axs[0].plot(years_scen,emi_NDC[:,0]+emi_NDC[:,1],color=colors[3])
axs[0].plot(years_scen,emi_70[:,0]+emi_70[:,1],color=colors[4])
axs[0].plot(years_scen,emi_85[:,0]+emi_85[:,1],color=colors[5])
axs[0].plot([1995,2100],[0,0],'k--',linewidth=0.5)
axs[0].tick_params(axis='y',which='major',labelsize=10)
axs[0].tick_params(axis='x',labelbottom='False')
axs[0].set_xticks([2000,2040,2080],minor=False)
axs[0].set_xticks([2020,2060,2100],minor=True)
axs[0].set_xlim([1995,2100])
axs[0].set_ylabel(ylbls[0],fontsize=13)

# Plot components
for i in xrange(1,10):

    axs[i].set_title(labels_plt[i],fontsize=13,loc='left')
    if i != 9: 
        axs[i].plot(years_hist,emi_hist[:,i+1],color=colors[0])
        axs[i].plot(years_scen,emi_19[:,i+1],color=colors[1])
        axs[i].plot(years_scen,emi_26[:,i+1],color=colors[2])
        axs[i].plot(years_scen,emi_NDC[:,i+1],color=colors[3])
        axs[i].plot(years_scen,emi_70[:,i+1],color=colors[4])
        axs[i].plot(years_scen,emi_85[:,i+1],color=colors[5])
    else:
        axs[i].plot(years_hist,emi_hist[:,i+1],color=colors[0],\
                    label='Historical')             
        axs[i].plot(years_scen,emi_19[:,i+1],color=colors[1],\
                    label='Below 1.5$^{\circ}$C')
        axs[i].plot(years_scen,emi_26[:,i+1],color=colors[2],\
                    label='Below 2$^{\circ}$C')
        axs[i].plot(years_scen,emi_NDC[:,i+1],color=colors[3],\
                    label='NDCs')
        axs[i].plot(years_scen,emi_70[:,i+1],color=colors[4],\
                    label='Average no mitigation')
        axs[i].plot(years_scen,emi_85[:,i+1],color=colors[5],\
                    label='Worst case no mitigation')
    axs[i].tick_params(axis='y',which='major',labelsize=10)
    axs[i].tick_params(axis='x',labelbottom='False')
    axs[i].set_xticks([2000,2040,2080],minor=False)
    axs[i].set_xticks([2020,2060,2100],minor=True)
    axs[i].set_xlim([1995,2100])
    axs[i].set_ylim(ymin=0)
    axs[i].set_ylabel(ylbls[i],fontsize=13)

axs[i-2].set_xlabel('Year',fontsize=13)
axs[i-2].set_xticks([2000,2040,2080],minor=False)
axs[i-2].tick_params(axis='x',which='major',labelsize=10,\
                     labelbottom='True')
axs[i-1].set_xlabel('Year',fontsize=13)
axs[i-1].set_xticks([2000,2040,2080],minor=False)
axs[i-1].tick_params(axis='x',which='major',labelsize=10,\
                     labelbottom='True')
axs[i].set_xlabel('Year',fontsize=13)
axs[i].set_xticks([2000,2040,2080],minor=False)
axs[i].tick_params(axis='x',which='major',labelsize=10,\
                   labelbottom='True')
axs[i].legend(bbox_to_anchor=(1.36, 0.5),loc='center left',\
              ncol=2,fontsize=13)

axs[i+1].set_visible(False)
axs[i+2].set_visible(False)

plt.subplots_adjust(top=0.91,bottom=0.06,left=0.07,right=0.99,\
                    wspace=0.4,hspace=0.27)
plt.show()


