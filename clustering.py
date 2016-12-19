import numpy as np
from sklearn.cluster import KMeans
from sklearn.cluster import MeanShift, estimate_bandwidth
import pandas as pd
from matplotlib import style
from matplotlib import pyplot as plt
style.use('ggplot')

path = 'C:/Users/admin/Desktop/4ano/IB/IBprojetoFinal-20161203T230454Z/IBprojetoFinal/txt/data'
data = np.load(path)

'''
Data stacked in vector

Family
Drug name
Exact Mass
Mol Weight
'''
equal = []
iPoints = []
print len(data[0,:])
for i in range(0, len(data[1,:])):
    x=0
    for j in range(0,len(data[1,:])):
      if data[1,i] == data[1,j] and i!=j:
          x=x+1
          iPoints.append(i)

    equal.append(x)

data = np.delete(data,iPoints,axis = 1)
data = np.delete(data, (0,1), axis = 0)
print len(data[0,:])
data = data.transpose()
#print data

##########################################
######     Kmeans Clustering       #######
##########################################

kmeans = KMeans(n_clusters = 18 , random_state = 0)
kmeans.fit(data,y=None)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

plt.scatter(centroids[:,0],centroids[:,1],marker = 'x', s=150, linewidths = 5, zorder = 10)

plt.show()

#print labels

##########################################
#####    Hierarchical Clustering     #####
##########################################
'''
data = np.array(data).astype(float)

bandwidth = estimate_bandwidth(data,quantile = 0.2)
ms = MeanShift(bandwidth = bandwidth,bin_seeding = True)
ms.fit(data)
labels1 = ms.labels_
centroids1 = ms.cluster_centers_

labels_unique = np.unique(labels1)
n_clusters_ = len(labels_unique)


np.set_printoptions(threshold='nan')
print('number of clusters: %d' % n_clusters_)
print labels1
'''