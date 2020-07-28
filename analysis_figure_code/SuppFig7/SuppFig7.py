import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

"""
Created on Weds Mar 11 18:35 2020

@author: Christine McKenna

=========================================================================
Purpose: Plots distributions of near-term warming trends for different
         emission scenarios in FaIR, with different estimates of IV
         added for comparison. Supp Fig 7.
=========================================================================
"""

# Required directories
loaddir = 'Priestley-Centre/Near_term_warming/analysis_figure_code/'+\
          'SuppFig7/saved_data'


### ------ Load in FaIR data ------

trends_Had = np.load(loaddir+'/stats_trend_f_HadOSTIV.npy',\
                     allow_pickle='TRUE').item()
trends_CW = np.load(loaddir+'/stats_trend_f_CWIV.npy',\
                    allow_pickle='TRUE').item()
trends_Be = np.load(loaddir+'/stats_trend_f_BeIV.npy',\
                    allow_pickle='TRUE').item()
trends_highC = np.load(loaddir+'/stats_trend_f_BCC-CSM2-MR_IV.npy',\
                       allow_pickle='TRUE').item()
trends_lowC = np.load(loaddir+'/stats_trend_f_MIROC-ES2L_IV.npy',\
                      allow_pickle='TRUE').item()
minmax_Had = np.load(loaddir+'/minmax_trend_f_HadOSTIV.npy')
minmax_CW = np.load(loaddir+'/minmax_trend_f_CWIV.npy')
minmax_Be = np.load(loaddir+'/minmax_trend_f_BeIV.npy')
minmax_highC = np.load(loaddir+'/minmax_trend_f_BCC-CSM2-MRIV.npy')
minmax_lowC = np.load(loaddir+'/minmax_trend_f_MIROC-ES2LIV.npy')



### ----------------------------------
###            Plot trends
### ----------------------------------

colors=['grey','green','dodgerblue','orange','sienna']


### Obs estimates

fig1,[ax1,ax2,ax3] = plt.subplots(1,3,figsize=(17,9),sharey=True)
plt.suptitle('2021-2040 GSAT trends from FaIR plus IV',fontsize=23)
plt.gcf().text(0.005,0.9,'(a) Observation based IV estimates',fontsize=22)

# HadOST
ax1.set_title('(i) HadOST',y=1.01,fontsize=20,loc='left')
bplot1 = ax1.bxp([trends_Had['N'],trends_Had['19'],\
                 trends_Had['26'],trends_Had['70'],\
                 trends_Had['85']],\
                 positions=[1.0,1.8,2.6,3.4,4.2],\
                 patch_artist=True,flierprops=dict(marker='.'),\
                 widths=np.ones([5])*0.25)
plt.setp(bplot1['medians'], color='k')
x=0
for patch in bplot1['boxes']:
    patch.set_facecolor(colors[x])
    x += 1
ax1.scatter([[1.0,1.0],[1.8,1.8],[2.6,2.6],[3.4,3.4],[4.2,4.2]],\
            minmax_Had,marker='x',s=25,c='k')
ax1.set_xlim([0.5,4.7])
ax1.set_xticks([1.0,1.8,2.6,3.4,4.2])
ax1.xaxis.set_ticklabels(['NDC-\nlike','Below\n1.5$^{\circ}$C',\
                          'Below\n2$^{\circ}$C',\
                          'Aver-\nage',\
                          'Worst\ncase'])
ax1.set_ylim([-0.36,1.05])
ax1.set_yticks([-0.2,0,0.2,0.4,0.6,0.8,1.0])
ax1.set_ylabel('$^{\circ}$C / decade',fontsize=19)
ax1.tick_params(labelsize=19)
ax1.fill_between([0.5,4.7],0.254,0.287,edgecolor='',facecolor='grey',\
                 alpha=0.3,zorder=0)
ax1.plot([0.5,4.7],[0.265,0.265],color='black',linewidth=1,zorder=0)
ax1.plot([0.5,4.7],[0,0],'--',color='black',linewidth=1,zorder=0)

# BE
ax2.set_title('(ii) Berkeley Earth',y=1.01,fontsize=20,loc='left')
bplot2 = ax2.bxp([trends_Be['N'],trends_Be['19'],\
                 trends_Be['26'],trends_Be['70'],\
                 trends_Be['85']],\
                 positions=[1.0,1.8,2.6,3.4,4.2],\
                 patch_artist=True,flierprops=dict(marker='.'),\
                 widths=np.ones([5])*0.25)
plt.setp(bplot2['medians'], color='k')
x=0
for patch in bplot2['boxes']:
    patch.set_facecolor(colors[x])
    x += 1
ax2.scatter([[1.0,1.0],[1.8,1.8],[2.6,2.6],[3.4,3.4],[4.2,4.2]],\
            minmax_Be,marker='x',s=25,c='k')
ax2.set_xlim([0.5,4.7])
ax2.set_xticks([1.0,1.8,2.6,3.4,4.2])
ax2.xaxis.set_ticklabels(['NDC-\nlike','Below\n1.5$^{\circ}$C',\
                          'Below\n2$^{\circ}$C',\
                          'Aver-\nage',\
                          'Worst\ncase'])
ax2.tick_params(labelsize=19)
ax2.fill_between([0.5,4.7],0.254,0.287,edgecolor='',facecolor='grey',\
                 alpha=0.3,zorder=0)
ax2.plot([0.5,4.7],[0.265,0.265],color='black',linewidth=1,zorder=0)
ax2.plot([0.5,4.7],[0,0],'--',color='black',linewidth=1,zorder=0)

# CWv2
ax3.set_title('(iii) Cowtan-Way v2',y=1.01,fontsize=20,loc='left')
bplot3 = ax3.bxp([trends_CW['N'],trends_CW['19'],\
                 trends_CW['26'],trends_CW['70'],\
                 trends_CW['85']],\
                 positions=[1.0,1.8,2.6,3.4,4.2],\
                 patch_artist=True,flierprops=dict(marker='.'),\
                 widths=np.ones([5])*0.25)
plt.setp(bplot3['medians'], color='k')
x=0
for patch in bplot3['boxes']:
    patch.set_facecolor(colors[x])
    x += 1
ax3.scatter([[1.0,1.0],[1.8,1.8],[2.6,2.6],[3.4,3.4],[4.2,4.2]],\
            minmax_CW,marker='x',s=25,c='k')
ax3.set_xlim([0.5,4.7])
ax3.set_xticks([1.0,1.8,2.6,3.4,4.2])
ax3.xaxis.set_ticklabels(['NDC-\nlike','Below\n1.5$^{\circ}$C',\
                          'Below\n2$^{\circ}$C',\
                          'Aver-\nage',\
                          'Worst\ncase'])
ax3.tick_params(labelsize=19)
ax3.fill_between([0.5,4.7],0.254,0.287,edgecolor='',facecolor='grey',\
                 alpha=0.3,zorder=0)
ax3.plot([0.5,4.7],[0.265,0.265],color='black',linewidth=1,zorder=0)
ax3.plot([0.5,4.7],[0,0],'--',color='black',linewidth=1,zorder=0)

plt.subplots_adjust(top=0.83,bottom=0.08,left=0.06,right=0.9,wspace=0.1)


### CMIP6 estimates

fig2,[ax1,ax2,ax3] = plt.subplots(1,3,figsize=(17,9),sharey=True)
plt.suptitle('2021-2040 GSAT trends from FaIR plus IV',fontsize=23)
plt.gcf().text(0.005,0.9,'(b) CMIP6 piControl run IV estimates',fontsize=22)

# Low var
ax1.set_title('(i) MIROC-ES2L',y=1.01,fontsize=20,loc='left')
bplot1 = ax1.bxp([trends_lowC['N'],trends_lowC['19'],\
                 trends_lowC['26'],trends_lowC['70'],\
                 trends_lowC['85']],\
                 positions=[1.0,1.8,2.6,3.4,4.2],\
                 patch_artist=True,flierprops=dict(marker='.'),\
                 widths=np.ones([5])*0.25)
plt.setp(bplot1['medians'], color='k')
x=0
for patch in bplot1['boxes']:
    patch.set_facecolor(colors[x])
    x += 1
ax1.scatter([[1.0,1.0],[1.8,1.8],[2.6,2.6],[3.4,3.4],[4.2,4.2]],\
            minmax_lowC,marker='x',s=25,c='k')
ax1.set_xlim([0.5,4.7])
ax1.set_xticks([1.0,1.8,2.6,3.4,4.2])
ax1.xaxis.set_ticklabels(['NDC-\nlike','Below\n1.5$^{\circ}$C',\
                          'Below\n2$^{\circ}$C',\
                          'Aver-\nage',\
                          'Worst\ncase'])
ax1.set_ylim([-0.38,1.05])
ax1.set_yticks([-0.2,0,0.2,0.4,0.6,0.8,1.0])
ax1.set_ylabel('$^{\circ}$C / decade',fontsize=19)
ax1.tick_params(labelsize=19)
ax1.fill_between([0.5,4.7],0.254,0.287,edgecolor='',facecolor='grey',\
                 alpha=0.3,zorder=0)
ax1.plot([0.5,4.7],[0.265,0.265],color='black',linewidth=1,zorder=0)
ax1.plot([0.5,4.7],[0,0],'--',color='black',linewidth=1,zorder=0)

# High var
ax2.set_title('(ii) BCC-CSM2-MR',y=1.01,fontsize=20,loc='left')
bplot2 = ax2.bxp([trends_highC['N'],trends_highC['19'],\
                 trends_highC['26'],trends_highC['70'],\
                 trends_highC['85']],\
                 positions=[1.0,1.8,2.6,3.4,4.2],\
                 patch_artist=True,flierprops=dict(marker='.'),\
                 widths=np.ones([5])*0.25)
plt.setp(bplot2['medians'], color='k')
x=0
for patch in bplot2['boxes']:
    patch.set_facecolor(colors[x])
    x += 1
ax2.scatter([[1.0,1.0],[1.8,1.8],[2.6,2.6],[3.4,3.4],[4.2,4.2]],\
            minmax_highC,marker='x',s=25,c='k')
ax2.set_xlim([0.5,4.7])
ax2.set_xticks([1.0,1.8,2.6,3.4,4.2])
ax2.xaxis.set_ticklabels(['NDC-\nlike','Below\n1.5$^{\circ}$C',\
                          'Below\n2$^{\circ}$C',\
                          'Aver-\nage',\
                          'Worst\ncase'])
ax2.tick_params(labelsize=19)
ax2.fill_between([0.5,4.7],0.254,0.287,edgecolor='',facecolor='grey',\
                 alpha=0.3,zorder=0)
ax2.plot([0.5,4.7],[0.265,0.265],color='black',linewidth=1,zorder=0)
ax2.plot([0.5,4.7],[0,0],'--',color='black',linewidth=1,zorder=0)
ax3.set_visible(False)

plt.subplots_adjust(top=0.83,bottom=0.08,left=0.06,right=0.9,wspace=0.1)

# Show (note Inkscape is then used to combine these Figures into one,
# smarten them up, and to add a legend)
plt.show()


