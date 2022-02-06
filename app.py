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

# data= pd.read_csv('https://raw.githubusercontent.com/Nobert-Ok/Image_description_Clustering/main/train.csv')

@st.cache  # No need for TTL this time. It's static data :)
def get_data_by_state():
	return pd.read_csv('https://raw.githubusercontent.com/Nobert-Ok/Image_description_Clustering/main/train.csv')

data = get_data_by_state()
data['image_description'] = data['description']
data = data[data['image_description'].notna()]
documents = data['image_description'].values.astype("U")
data['cluster'] = model.labels_


clusters = data.groupby('cluster')  
for cluster in clusters.groups:
    data_clusters = clusters.get_group(cluster)[['categories','image_description']] # get title and overview columns
    st.text('Cluster ' + str(cluster+1))
    st.dataframe(data_clusters)
