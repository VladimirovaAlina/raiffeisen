import numpy as np
import scipy as sp
from  scipy import stats 


info = {'R': {'client':set(), 'transac':[]}, 
       'AF': {'client':set(), 'transac':[]}}

with open('/usr/local/data/transactions.txt') as tr:
    for line in tr:
        line = line.strip().split(',')
        info[line[3]]['client'].add(line[1])
        info[line[3]]['transac'].append(int(line[2]))

n_R = len(info['R']['client'])
n_AF = len(info['AF']['client'])

print(n_R, 'number of clients in R')
print(n_AF,  'number of clients in AF')
 

# mean transaction for R
mean_tr_R = np.mean(info['R']['transac'])
# mean transaction for AF
mean_tr_AF = np.mean(info['AF']['transac'])

print(mean_tr_R, 'mean transaction for R')
print(mean_tr_AF, 'mean transaction for AF')


def mean_confidence_interval(data, confidence=0.90):
    n = len(data)
    mean = np.mean(data)
    se = stats.sem(data)
    gran = se * sp.stats.t._ppf((1+confidence)/2., n-1)
    if mean-gran>0:
        return mean-gran, mean+gran
    else:
        return 0, mean+gran

print(mean_confidence_interval(info['R']['transac']), 'confidence interval 90% for R')

print(mean_confidence_interval(info['AF']['transac']), 'confidence interval 90% for AF')
