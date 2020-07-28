from __future__ import division
import numpy as np
import numpy.random as npr

def montecarlo(arr_mit,arr_nomit,n_resamp=100000,alpha=0):
    # Calculates the probability that a realisation in 
    # arr_mit is less than in arr_nomit by a given
    # proportion alpha. Essentially tells us the likelihood that 
    # observed future trend will be smaller under mitigation 
    # than under no mitigation by the proportion alpha.

    n_samp = len(arr_mit)
    resamp_diffs = np.zeros(n_resamp)

    # Reduce arr_nomit by proportion alpha, so ask
    # whether trend under arr_mit is less than
    # under arr_nomit by this amount 
    arr_nomit = arr_nomit - alpha*arr_nomit

    # Now resample differences
    for i in xrange(n_resamp):
        # define arrays of random indices (for time dim)
        idx1 = npr.randint(0,n_samp)
        idx2 = npr.randint(0,n_samp)
        # calculate resampled differences
        resamp_diffs[i] = arr_mit[idx1] - arr_nomit[idx2] 

    # rank order the differences
    resamp_diffs = np.sort(resamp_diffs,0)

    # calculate p-value
    n_lt_0 = np.shape(np.where(resamp_diffs < 0))[1]
    p = n_lt_0/n_resamp

    return p, resamp_diffs


