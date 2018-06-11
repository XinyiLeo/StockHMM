from pandas import Series, DataFrame
import pandas as pd
import numpy as np


# obj = Series([4, 7, -5, 3]) P112
# print(obj)
# print(obj.values)
# print(obj.index)
# obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
# print(obj2)
# print(obj2.index)
# print(obj2['a'])
# obj2['d'] = 6
# print(obj2[['c', 'a', 'd']])
# print(obj2[obj2 > 0])
# print('b' in obj2)

# sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
# obj3 = Series(sdata)
# states = ['California', 'Ohio', 'Oregon', 'Texas']
# obj4 = Series(sdata, index=states)
# print(obj4)
# pd.isnull(obj4)
# pd.notnull(obj4)

# Data frame P115
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 'year': [2000, 2001, 2002, 2001, 2002], 'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data, columns=['year', 'state', 'pop'])
print(frame)

# Index Objects P120
# obj = Series(range(3), index=['a', 'b', 'c'])
# index = obj.index
# print(index[1:])
# index = pd.Index(np.arange(3))
# obj2 = Series([1.5, -2.5, 0], index=index)
# obj2.index is index
# Index objects are immutable and thus can't be modified by the user:
# obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
# obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
# obj = Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
# new_obj = obj.drop('c')
# Dropping entries from an axis

# P145 Filling in missing data
# P147 Hierarchical indexing
# data = Series(np.random.randn(10),
#               index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
#                      [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
# print(data.unstack())
