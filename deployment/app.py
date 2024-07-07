import streamlit as st 
import eda 
import prediction 

navigation = st.sidebar.selectbox('Pilih Halaman:', {'EDA':'eda','Prediction':'pred'})

if navigation == 'EDA':
    eda.run()
else:
    prediction.run()