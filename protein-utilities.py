import pandas as pd
import numpy as np
import regex as re
import random
import sklearn
import scipy
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans


def do_PCA(filename, filetype="csv", dim = 2):
    '''
    This is designed to fit a PCA on a file input. File should be a CSV or otherwise with no label column

    Inputs:
    filename: path to file to fit PCA on
    filetype: either CSV, table, excel (xls, etc)
    n_components: # of PCA dimensions to find

    Returns a fitted PCA dataframe
    '''
    if filetype == "csv":
        simul = pd.read_csv(filename)
    elif filetype == "table":
        simul = pd.read_table(filename)
    else:
        simul = pd.read_excel(filename)
    
    pca=PCA(dim)

    sdf = pca.fit_transform(simul)
    
    return sdf


def do_KMeans(df, clusters = 3):
    '''

    Perform KMeans on a PCA dataframe and visualize clusters

    Inputs:
    df: PCA-fitted DF
    clusters: number of PCA clusters. 3 recommended

    Outputs:
    
    Kmeans object
    '''

    kmeans = KMeans(clusters)
    kmeans.fit(df)
    y_kmeans=kmeans.predict(df)

   
    df = pd.DataFrame(df)
    #viz time
    
    df['subtype'] = y_kmeans

    plt.scatter(df[:, 0], df[:, 1], c=df['subtype'], s=50, cmap='viridis')

    centers = kmeans.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);


test_df = do_PCA("Desktop/granumhealth_mvp/cases_simul.csv")
do_KMeans(test_df)


    
