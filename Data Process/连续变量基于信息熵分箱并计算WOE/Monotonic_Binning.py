# import packages
import pandas as pd
import numpy as np
import scipy.stats.stats as stats
 
# import data
data = pd.read_csv("/home/liuwensui/Documents/data/accepts.csv", sep = ",", header = 0)
 
# define a binning function
def mono_bin(Y, X, n = 20):
  # fill missings with median
  X2 = X.fillna(np.median(X))
  r = 0
  while np.abs(r) < 1:
    d1 = pd.DataFrame({"X": X2, "Y": Y, "Bucket": pd.qcut(X2, n)})
    d2 = d1.groupby('Bucket', as_index = True)
    r, p = stats.spearmanr(d2.mean().X, d2.mean().Y)
    n = n - 1
  d3 = pd.DataFrame(d2.min().X, columns = ['min_' + X.name])
  d3['max_' + X.name] = d2.max().X
  d3[Y.name] = d2.sum().Y
  d3['total'] = d2.count().Y
  d3[Y.name + '_rate'] = d2.mean().Y
  d4 = (d3.sort_index(by = 'min_' + X.name)).reset_index(drop = True)
  print "=" * 60
  print d4
 
mono_bin(data.bad, data.ltv)
mono_bin(data.bad, data.bureau_score)
mono_bin(data.bad, data.age_oldest_tr)
mono_bin(data.bad, data.tot_tr)
mono_bin(data.bad, data.tot_income)
