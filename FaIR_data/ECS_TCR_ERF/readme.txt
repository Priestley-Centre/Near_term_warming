Distributions of ECS, TCR, and ERF, used to generate each set of 500 simulations. Also contains time-series of the ERF, both for its total and for individual forcing agents. Both versions of the aerosol ERF time-series are given (the default CMIP6 aerosol ERF and the aerosol ERF from AR5).


In detail, each file contains:

'parameters.csv' 
- 500 values of ECS and TCR (degrees C)
- 500 scaling factors to apply to the ERF time series for each component (unitless)
- 500 values of three parameters used to account for uncertainty in the carbon cycle response. Parameters are: the pre-industrial sensitivity of land and ocean carbon sinks, r0 (years); and the sensitivity of these sinks to cumulative CO2 emissions, rC (years / GtC), and to the temperature change since pre-industrial, rT (years / degrees C). While carbon cycle uncertainty is included, it has very little effect on the distributions of near-term temperature trends in FaIR (in agreement with Smith et al. 2019; see Fig 4 in https://www.nature.com/articles/s41467-018-07999-w)

'ERF_*.csv'
- Time-series of ERF for each component (W/m2)

'*_forc.csv'
- Time-series of total ERF for each member of the 500 simulations (W/m2), where the default CMIP6 aerosol ERF is used

'*_forc_AR5aero.csv'
- Time-series of total ERF for each member of the 500 simulations (W/m2), where the aerosol ERF from AR5 is used

'*_forcaer_AR5aero.csv'
- Time-series of aerosol ERF for each member of the 500 simulations (W/m2), where the aerosol ERF from AR5 is used

