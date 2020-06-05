# Load the required packages
import math
import numpy as np
from scipy import stats

# Sample data
# 1 - Control group
# 2 - Experiment group
# Trivia: Netflix pulls two cells out of population and make one control while the other test (n1 = n2)
s1 = 3.5586 # standard deviation
s2 = 4.7676
n1 = 1746 # sample size
n2 = 849
X1Bar = 2.669 # Point Estimate
X2Bar = 4.0754
# expected t statistic = 7.6245
# expected p value = 0

# Welch's t-test
# Hypothesis Testing when equal or unequal sample sizes and unequal variances

# Built using math
sDeltaBar = math.sqrt((s1**2/n1)+(s2**2/n2)) # Not the typical pooled variance
t = (X1Bar - X2Bar)/sDeltaBar # t statistic value

df = (((s1**2/n1)+(s2**2/n2))**2)/(((s1**2/n1)**2/(n1-1))+((s2**2/n2)**2/(n2-1))) # Degrees of freedom

pval = stats.t.sf(np.abs(t), round(df)-1)*2  # two-sided pvalue = Prob(abs(t)>tt)
print('t-statistic = %6.3f pvalue = %6.4f' % (t, pval))

# Reference
# https://en.wikipedia.org/wiki/Student's_t-test
