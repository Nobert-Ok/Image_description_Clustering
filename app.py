import pickle
import streamlit as st
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import LabelEncoder
label_enc = LabelEncoder()

tfid= pickle.load(open('Tfidfmodels.pkl','rb'))
model=pickle.load(open('kmeanmodel.pkl','rb'))    


# front end elements of the web page 
html_temp = """ 
<div style ="background-color:blue;padding:5px;"> 
<h4 style ="color:black;text-align:center;">Streamlit New Article Clustering App</h4> 
</div> 
""" 
st.markdown(html_temp, unsafe_allow_html = True) 

data= pd.read_csv('https://raw.githubusercontent.com/Nobert-Ok/Image_description_Clustering/main/train.csv')


for i in range(3):
    st.text(str(i))


# documents = data['description'].values.astype("U")
# model.fit(tfid.fit_transform(documents))

# st.dataframe(pred)


# data['cluster'] = model.labels_

# clusters = data.groupby('cluster')  

# for cluster in clusters.groups:
#     data_clusters = clusters.get_group(cluster)[['categories','title','description']] # get title and overview columns
#     st.dataframe(data_clusters)




# if st.button("Predict"): 
#   pred = model.predict(tfid.transform([Content]))
#   if pred==1:
#     st.write('This news article is on politics.')   
#     st.write('Below is the list of related links similar to your politics news')   
#     pred= int(pred)
#     data_pred = data.loc[(data['label'] == pred)]
#     st.dataframe(data_pred['links'].unique())
#   elif pred==0:
#     st.write('This news article is on business')
#     st.write('Below is the list of related links similar to your business news')   
#     term="business"
#     pred= int(pred)
#     data_pred = data.loc[(data['label'] == pred)]
#     st.dataframe(data_pred['links'].unique())
#   elif pred==2:
#     st.write('This news article is on culture') 
#     st.write('Below is the list of related links similar to your culture news')   
#     pred= int(pred)
#     term="pol"
#     pred= int(pred)
#     data_pred = data.loc[(data['label'] == pred)]
#     st.dataframe(data_pred['links'].unique())
#   elif pred==3:
#     st.write('This news article is on sports')
#     st.write('Below is the list of related links similar to your sports news')   
#     pred= int(pred)
#     term='sport'
#     data_pred = data.loc[(data['label'] == pred)]
#     st.dataframe(data_pred['links'].unique())
