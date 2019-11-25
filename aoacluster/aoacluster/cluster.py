def cluster(filename, centroid_x1, centroid_y1,centroid_x2, centroid_y2, centroid_x3, centroid_y3):
    import pandas as pd
    from matplotlib import pyplot as plt
    
    df1 = pd.read_csv(filename)

    df1[1] = (((df1['var1'] - (centroid_x1))**2) + (df1['var2'] - (centroid_y1))**2)
    df1[2] = (((df1['var1'] - (centroid_x2))**2) + (df1['var2'] - (centroid_y2))**2)
    df1[3] = (((df1['var1'] - (centroid_x3))**2) + (df1['var2'] - (centroid_y3))**2)

    df1['class'] = df1[[1,2,3]].idxmin(axis=1)

    print(df1.head())

    plt.scatter(df1['var1'], df1['var2'], c = df1['class'])
    plt.show()