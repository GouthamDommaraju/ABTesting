# Load the required packages
from scipy import stats
import math

## Function to get z-critical value
# Inputs:
#   The desired alpha for a two-tailed test
# Returns: The z-critical value
def getZstar (alpha):
    return(-stats.norm.ppf(alpha/2)) # percentile point function

## Function to get beta values
# Inputs:
#   zStar: The z-critical value
#   s: The standard error of the metric at N=1
#   dMin: The practical significance level
#   N: The sample size of each group of the experiment
# Returns: The beta value of the two-tailed test    
def getBeta (zStar, s, dMin, N):
    SE = s/math.sqrt(N)
    return(stats.norm.cdf(zStar*SE, loc=dMin, scale=SE))

## Function to calculate the minimum sample size required to meet the desired alpha and beta
# Inputs:
#   s: The standard error of the metric with N=1 in each group
#   dMin: The practical significance level
#   Ns: The sample sizes to try
#   alpha: The desired alpha level of the test
#   beta: The desired beta level of the test
# Returns: The smallest N out of the given Ns that will achieve the desired
#          beta. There should be at least N samples in each group of the experiment.
#          If none of the given Ns will work, returns -1. N is the number of
#          samples in each group.
def getRequiredSize (s, dMin, Ns=range(1,20000), alpha=0.05, beta=0.2):
    for N in Ns:
        if (getBeta(getZstar(alpha), s, dMin, N) <= beta):
            return(N)
    else:
        return(-1)

## Example analytic usage
# User Inputs
p = 0.1 # Baseline Conversion Rate
dMinUser = 0.02 # Minimum Detectable Effect
alphaUser = 0.05 # Percent of the time a difference will be detected, assuming one does NOT exist
betaUser = 0.2 # Means 1-beta = 80% | Percent of the time the minimum effect size will be detected, assuming it exists

# Output
output = getRequiredSize(s=math.sqrt(p*(1-p)*2), dMin=dMinUser, alpha=alphaUser, beta=betaUser)
# s is the pooled standard error for N=1 in each group, which is sqrt(p*(1-p)*(1/1 + 1/1))

print ("The minimum sample size required in each group is",output)
