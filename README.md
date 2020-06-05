
# SampleSizeCalculation.py 
It helps you decide the sample size of test and control groups while designing an experiment based on your choice of 
  1. Baseline Conversion Rate
  2. Minimum Detectable Effect
  3. Alpha
  4. Beta

# CheckingInvariants.py 
It helps you gain insight on wether the experiment ran as expected by checking the invariants across test and control group
  * Unit of diversion used is Event
  * Unit of analysis used is Event
  * Invariant: Event Count

# WelchTTest.py 
It helps you perform a student's t test on equal or unequal sample sizes and unequal variances to understand if the control and experiment groups are significantly different for the point estimate of the considered metric
