import streamlit as st
import pandas as pd
from application_functions import pca_function
import plotly.express as px
import numpy as np

st.set_page_config(layout= 'wide')
scatter_plot_column, settings_column = st.beta_columns((4, 1))

scatter_plot_column.title('Multi-Dimensional Analysis')

settings_column.title('Settings')
uploaded_file = settings_column.file_uploader("Choose file.")

if uploaded_file is not None:
    data_import = pd.read_csv(uploaded_file)
    pca_data, pca_cols, categorical_cols = pca_function(data_import)
    pca_1 = settings_column.selectbox("First Principal Component", options= pca_cols)
    pca_cols.remove(pca_1)
    pca_2 = settings_column.selectbox("Second Principal Component", options= pca_cols)
    categorical_variable = settings_column.selectbox("Select Variable", options= categorical_cols)
    categorical_cols.remove(categorical_variable)
    categorical_variable_2 = settings_column.selectbox("Select hover variable", options= categorical_cols)
    scatter_plot_column.plotly_chart(px.scatter(data_frame= pca_data, x= pca_1, y= pca_2,  color=categorical_variable, height= 800, hover_data= [categorical_variable_2]), use_container_width= True)

else:
    scatter_plot_column.header("Please choose a file.")



