# Runs Test for testing randomness of data.
'''
Runs test of randomness is a statistical test that is used to check the randomness in data. 
It is a nonparametric test and uses runs of data to decide whether the presented data is random or tends to follow a pattern.

Step-1:
The first step in applying this test is to formulate the null and alternate hypothesis.
Hnull : The sequence was produced in a random manner
Halt  : The sequence was not produced in a random manner

Step-2:
Calculate the test statistic, Z as:
Z = R - Rbar / Sr
Where, 
R = The number of observed runs
Rbar = The number of expected runs, given as

Rbar = (2n1n2 / (n1 + n2)) + 1
Sr = Standard Deviation of the number of runs

Sr^2 = (2n1n2(2n1n2 - n1 - n2)) / ((n1 + n2)^2(n1 + n2 - 1))
With n1 and n2 = the number of positive and 
negative values in the series

Step-3:
Compare the value of the calculated Z-statistic with Zcritical  for a given level of confidence 
(Zcritical =1.96 for confidence level of 95%) . The null hypothesis is rejected i.e. the numbers are declared 
not to be random, if |Z|>Zcritical . 
'''

import math
import statistics
from RandomClass import Mersenne
  
def runsTest(l, l_median):
    runs, n1, n2 = 0, 0, 0
    # Checking for start of new run
    for i in range(len(l)):
        # no. of runs
        if (l[i] >= l_median and l[i-1] < l_median) or (l[i] < l_median and l[i-1] >= l_median):
            runs += 1  
          
        # no. of positive values
        if(l[i]) >= l_median:
            n1 += 1   
        # no. of negative values
        else:
            n2 += 1   
  
    runs_exp = ((2 * n1 * n2) / (n1 + n2)) + 1
    stan_dev = math.sqrt((2 * n1 * n2 * (2 * n1 * n2 - n1 - n2))/ (((n1 + n2) ** 2) * (n1 + n2 - 1)))
    return (runs - runs_exp) / stan_dev
    
def main():
    print("---------RUNS_TEST-----------")
    l = []
    Z_critical_95_confidence = 1.96
    Seed = 0
    NUMBER_OF_SAMPLES = 10**4
    Rand = Mersenne(Seed)
    for i in range(NUMBER_OF_SAMPLES):
        l.append(Rand.random())
          
    l_median= statistics.median(l)
    Z = abs(runsTest(l, l_median))
    print("Z_critical: ", Z_critical_95_confidence)
    print("Z-statistic: ", Z)

    if(Z < Z_critical_95_confidence):
        print("Fail To Reject null hypothesis")
    else:
        print("Reject null hypothesis")


if __name__ == '__main__':
    main()