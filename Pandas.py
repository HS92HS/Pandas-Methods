import pandas as pd
s1 = pd.Series

data = pd.read_csv("netflix_titles.csv")
print(data.columns)

# Group by
a = data[['type','title']]
print(a)
data1 = data.groupby(["type","title"]).count()
print(data1)
#
b = data.drop('duration',axis=1)
print(b.columns)
axis = 0 drop rows
axis = 1 drop columns

def nan(s):
    return s*0

c = data[['release_year']].apply(nan)
print(c)

from matplotlib import pyplot as plt
import numpy as np

data = pd.read_csv('netflix_titles.csv')
# print(data.columns)
# (['show_id', 'type', 'title', 'director', 'cast',
#   'country', 'date_added','release_year', 'rating',
#   'duration', 'listed_in', 'description']

a = data[['country']].head()
b = data[['title']].head()
b2 = list([b])
print(b2)
c = data[['release_year']].head()
c2 = list([c])
d = data[['duration']].head()
print(b)
a.replace(to_replace=np.nan,value='Pak',inplace=True)
print(a)

plt.hist(a,color='g')
plt.show()

plt.bar(c2,b2)
plt.show()

