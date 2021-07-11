import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np


def pca_function(df):

    numerical_columns_list = []
    categorical_columns_list = []

    for i in df.columns:
        if df[i].dtype == np.dtype("float64") or df[i].dtype == np.dtype("int64"):
            numerical_columns_list.append(i)

        else:
            categorical_columns_list.append(i)

    df_numerical_columns = df[numerical_columns_list]
    df_categorical_columns = df[categorical_columns_list]

    df_numerical_columns = df_numerical_columns.apply(lambda x: x.fillna(np.mean(x)))

    scaler = StandardScaler()
    scaled_values = scaler.fit_transform(df_numerical_columns)

    pca = PCA()
    pca_data = pca.fit_transform(scaled_values)
    pca_data = pd.DataFrame(pca_data)

    new_column_names = ["PCA_"+str(i) for i in range(1, len(pca_data.columns)+1)]
    columns_mapping = dict(zip(list(pca_data.columns), new_column_names))

    pca_data = pca_data.rename(columns= columns_mapping)

    output = pd.concat([df, pca_data], axis=1)

    return output, new_column_names, list(df_categorical_columns.columns)


