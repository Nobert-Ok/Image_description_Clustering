import pickle
import streamlit as st
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import LabelEncoder
label_enc = LabelEncoder()

model=pickle.load(open('kmeanmodel.pkl','rb'))    


# front end elements of the web page 
html_temp = """ 
<div style ="background-color:blue;padding:5px;"> 
<h1 style ="color:black;text-align:center;">Image Description Text Clustering</h1> 
</div> 
<h4>This web page displays clusters of product image description of 45187 amazon products.
The clustering is based on the similarity of the product image description.
</h4>
<h4>Below are the 5 different clusters of the products</h4>
""" 
st.markdown(html_temp, unsafe_allow_html = True) 

for cluster in range(1,6):
    st.text('Cluster ' + str(cluster))
    data = pd.read_csv('Cluster '+str(cluster)+'.csv')
    st.dataframe(data[['categories','image_description']])
