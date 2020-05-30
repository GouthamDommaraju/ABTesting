# Let's say you ran the experiment and landed up with
# Count of events in control group as 15348 and
# Count of events in test group as 15312 and
# Say event count is an invariant in your experiment as you used Event as your unit of diversion.

# Is it ok to get these numbers given that the probability of assigning a event to either a test or a control group is 0.5?
# We are going to use hypothesis testing to answer that.

# Import required packages
from scipy import stats
import math

# Variables
eventCont = 15348
eventExp = 15312
eventTot = eventCont + eventExp

# Observed proportion in control
pCont = eventCont/eventTot

# Ideal proportion in control | Given an event being assigned to control or test is random
p = 0.5

StandardE = math.sqrt(p*(1-p)/eventTot) # Calculate standard error # Binomial approximated to Normal because of huge sample size

m = StandardE*-stats.norm.ppf(0.05/2) # Margin of Error considering alpha to be 5%
LeftCI = p - m # Left Confidence Interval
RightCI = p + m # Right Confidence Interval

if LeftCI <= pCont <= RightCI:
    print ('Sample size of control is Good.')
else:
    print ('Sample size of control is Bad, Check the way the experiment was run.')
