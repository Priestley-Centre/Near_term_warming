import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

"""
Created on Weds Feb 19 13:22 2020

@author: Christine McKenna

=========================================================================
Purpose: Plots Supp Fig 5 (Fig 1 but with no IV). 
=========================================================================
"""

# Required functions
exec(open('Priestley-Centre/Near_term_warming/analysis_figure_code/'+\
          'my_boxplot.py').read())

# Required directories
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

# Calculate statistics for boxplot 
stats_trend_f = {}
stats_trend_f = my_boxplot_stats(gsat_trend_f_NDC,stats_trend_f,\
                                 'N',fliers=False)
stats_trend_f = my_boxplot_stats(gsat_trend_f_19,stats_trend_f,\
                                 '19',fliers=False)
stats_trend_f = my_boxplot_stats(gsat_trend_f_26,stats_trend_f,\
                                 '26',fliers=False)
stats_trend_f = my_boxplot_stats(gsat_trend_f_70,stats_trend_f,\
                                 '70',fliers=False)
stats_trend_f = my_boxplot_stats(gsat_trend_f_85,stats_trend_f,\
                                 '85',fliers=False)


### ------ Load in constrained CMIP6 trends ------

stats_trend_c = np.load(loaddir_CMIP+'/gsat_trend_CMIP6_con.npy',\
                        allow_pickle='TRUE').item()


### ----------------------------------
###            Plot trends
### ----------------------------------

colors=['grey','green','dodgerblue','lightblue','orange',\
        'moccasin','sienna','rosybrown']
fig1,ax1 = plt.subplots(1,1,figsize=(6,8))

ax1.set_title('2021-2040 GSAT trend',y=1.02,fontsize=20)
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
            gsat_trend_f_NDC),np.max(gsat_trend_f_NDC),\
            np.min(gsat_trend_f_19),np.max(gsat_trend_f_19),\
            np.min(gsat_trend_f_26),np.max(gsat_trend_f_26),\
            np.min(gsat_trend_f_70),np.max(gsat_trend_f_70),\
            np.min(gsat_trend_f_85),np.max(gsat_trend_f_85)],\
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

# Show (note this Figure is then edited in Inkscape to
# improve layout, add a legend, smarten up)
plt.subplots_adjust(top=0.93,bottom=0.08,left=0.2,right=0.95)
plt.show()


