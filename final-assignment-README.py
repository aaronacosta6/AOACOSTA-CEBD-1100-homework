# 2019 November 25 – Final Assignment

# to import this package, pip install aoacluster
# it assumes 3 cluster, of which the user will input the coordinates as the function parameters
# example: cluster(filename, centroid_x1, centroid_y1, centroid_x2, centroid_y2, centroid_x3, centroid_y3)

from aoacluster.aoacluster import cluster

#PLOT 1
cluster.cluster('/Users/Aaron/Desktop/data/data-1.csv', -10, -4.25, -6.3, -8.6, -1.14, 4.23)

#PLOT 2
cluster.cluster('/Users/Aaron/Desktop/data/data-2.csv', 21.39, 16.31, 20.93, 1.8, 28.06, 21.73)

#PLOT 3
cluster.cluster('/Users/Aaron/Desktop/data/data-3.csv', 95.34, 124.41, 136.22, 154.90, 185.33, 185.39)