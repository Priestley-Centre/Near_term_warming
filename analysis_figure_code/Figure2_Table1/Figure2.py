import numpy as np
import matplotlib.pyplot as plt

"""
Created on Fri Mar 27 17:07 2020

@author: Christine McKenna

=========================================================================
Purpose: Plots shifts in distributions under mitigation compared to
         no mitigation (Figure 2), to accompany Table 1 a and b of 
         near-term warming paper
=========================================================================
"""

# Required directories
loaddir = 'Priestley-Centre/Near_term_warming/analysis_figure_code/'+\
          'Figure2_Table1/saved_arrays'

# Load in data for montecarlo probabilities (Table 1a data for alpha=0)
diff_19_70 = np.load(loaddir+'/gsat_trend_diff_19_70.npy')
diff_26_70 = np.load(loaddir+'/gsat_trend_diff_26_70.npy')
diff_NDC_70 = np.load(loaddir+'/gsat_trend_diff_NDC_70.npy')
diff_19_85 = np.load(loaddir+'/gsat_trend_diff_19_85.npy')
diff_26_85 = np.load(loaddir+'/gsat_trend_diff_26_85.npy')
diff_NDC_85 = np.load(loaddir+'/gsat_trend_diff_NDC_85.npy')

# Load in data for Pns probability (Table 1b data)
diff_obs_19 = np.load(loaddir+'/gsat_trend_diff_obs_19.npy')
diff_obs_26 = np.load(loaddir+'/gsat_trend_diff_obs_26.npy')
diff_obs_NDC = np.load(loaddir+'/gsat_trend_diff_obs_NDC.npy')
diff_obs_70 = np.load(loaddir+'/gsat_trend_diff_obs_70.npy')
diff_obs_85 = np.load(loaddir+'/gsat_trend_diff_obs_85.npy')

### ----------- Plot -----------

fig,[[ax1,ax2],[ax3,ax4]] = plt.subplots(2,2,figsize=(7.08,6.58))
fig.suptitle('2021-2040 GSAT trend distributions from FaIR plus IV',\
             fontsize=13)
plt.rcParams['axes.linewidth']=0.62

# Table 1a distributions for alpha=0
plt.gcf().text(0.03,0.894,r'$\bf{a}$',fontsize=12)
ax1.set_title('Mitigation minus average\nno mitigation',\
              fontsize=11,loc='left',y=1.02)
ax1.hist(diff_NDC_70,bins=50,color='grey',alpha=0.4,\ 
         histtype='stepfilled')
ax1.hist(diff_NDC_70,bins=50,color='k',alpha=0.5,linewidth=1.0,\
         histtype='step')
ax1.hist(diff_26_70,bins=50,color='dodgerblue',alpha=0.4,\
         histtype='stepfilled')
ax1.hist(diff_26_70,bins=50,color='dodgerblue',linewidth=1.0,\
         histtype='step')
ax1.hist(diff_19_70,bins=50,color='green',alpha=0.4,\
         histtype='stepfilled')
ax1.hist(diff_19_70,bins=50,color='green',linewidth=1.0,\
         histtype='step')
ax1.plot([0,0],[0,8700],'k--',linewidth=0.75)
ax1.tick_params(labelsize=10)
ax1.set_xlabel('$^{\circ}$C / decade',fontsize=10)
ax1.set_ylabel('Frequency',fontsize=10,labelpad=9)
ax1.set_xlim([-0.75,0.45])
ax1.set_ylim([0,8700])
ax1.set_xticks([-0.6,-0.4,-0.2,0,0.2,0.4])

plt.gcf().text(0.52,0.894,r'$\bf{b}$',fontsize=12)
ax2.set_title('Mitigation minus worst case\nno mitigation',\
              fontsize=11,loc='left',y=1.02)
ax2.hist(diff_NDC_85,bins=50,color='grey',alpha=0.4,\
         histtype='stepfilled')
ax2.hist(diff_NDC_85,bins=50,color='k',alpha=0.5,linewidth=1.0,\
         histtype='step')
ax2.hist(diff_26_85,bins=50,color='dodgerblue',alpha=0.4,\
         histtype='stepfilled')
ax2.hist(diff_26_85,bins=50,color='dodgerblue',linewidth=1.0,\
         histtype='step')
ax2.hist(diff_19_85,bins=50,color='green',alpha=0.4,\
         histtype='stepfilled')
ax2.hist(diff_19_85,bins=50,color='green',linewidth=1.0,\
         histtype='step')
ax2.plot([0,0],[0,8700],'k--',linewidth=0.75)
ax2.tick_params(labelsize=10)
ax2.set_xlabel('$^{\circ}$C / decade',fontsize=10)
ax2.set_ylabel('Frequency',fontsize=10,labelpad=9)
ax2.set_xlim([-0.75,0.45])
ax2.set_ylim([0,8700])
ax2.set_xticks([-0.6,-0.4,-0.2,0,0.2,0.4])


# Table 1b distributions
plt.gcf().text(0.03,0.438,r'$\bf{c}$',fontsize=12)
ax3.set_title('Change from observed\n2000-2019 trend',\
              fontsize=11,loc='left',y=1.02)
ax3.hist(diff_obs_85,bins=50,color='sienna',alpha=0.4,\
         label='Worst case no mitigation',histtype='stepfilled')
ax3.hist(diff_obs_85,bins=50,color='sienna',linewidth=1.0,\
         histtype='step')
ax3.hist(diff_obs_70,bins=50,color='orange',alpha=0.4,\
         label='Average no mitigation',histtype='stepfilled')
ax3.hist(diff_obs_70,bins=50,color='darkorange',linewidth=1.0,\
         histtype='step')
ax3.hist(diff_obs_NDC,bins=50,color='grey',alpha=0.4,\
         label='NDCs',histtype='stepfilled')
ax3.hist(diff_obs_NDC,bins=50,color='k',alpha=0.5,linewidth=1.0,\
         histtype='step')
ax3.hist(diff_obs_26,bins=50,color='dodgerblue',alpha=0.4,\
         label='Below 2$^{\circ}$C',histtype='stepfilled')
ax3.hist(diff_obs_26,bins=50,color='dodgerblue',linewidth=1.0,\
         histtype='step')
ax3.hist(diff_obs_19,bins=50,color='green',alpha=0.4,\
         label='Below 1.5$^{\circ}$C',histtype='stepfilled')
ax3.hist(diff_obs_19,bins=50,color='green',linewidth=1.0,\
         histtype='step')
ax3.plot([0,0],[0,8700],'k--',linewidth=0.75)
ax3.tick_params(labelsize=10)
ax3.set_xlabel('$^{\circ}$C / decade',fontsize=10)
ax3.set_ylabel('Frequency',fontsize=10,labelpad=9)
ax3.set_xlim([-0.45,0.65])
ax3.set_ylim([0,5900])
ax3.set_xticks([-0.4,-0.2,0,0.2,0.4,0.6])

# Plot parameters
ax3.legend(bbox_to_anchor=(1.34,0.73),loc='center left',\
           fontsize=10)
ax4.set_visible(False)
plt.subplots_adjust(top=0.85,bottom=0.1,left=0.13,right=0.97,\
                    wspace=0.38,hspace=0.55)

# Show
plt.show()
