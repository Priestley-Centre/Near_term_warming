import numpy as np
import matplotlib.cbook as cbook

def my_boxplot_stats(data,stats,label,fliers=True,whis=[5,95],percents=[17,83]):

    stats[label] = cbook.boxplot_stats(data,whis=whis)[0]
    stats[label]['q1'],stats[label]['q3'] = np.percentile(data,percents)
    if fliers == False:
        stats[label]['fliers'] = np.array([])
    stats[label]['cihi'] = []    
    stats[label]['cilo'] = []    
    stats[label]['iqr'] = []    

    return stats
