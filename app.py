import streamlit as st 
import pandas as pd
import numpy as np
import os
import pickle
import warnings

import matplotlib.pyplot as plt
import plotly.express as px
from collections import Counter

from matplotlib.figure import Figure
import seaborn as sns


st.set_page_config(page_title="Heart Disease", page_icon="https://www.freeiconspng.com/thumbs/heart-png/heart-png-15.png", layout='centered', initial_sidebar_state="collapsed")

def main():
    html_temp = """
    <div>
    <h1 style="color:MEDIUMSEAGREEN;text-align:left;"> Heart guess</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    col1, col2 = st.beta_columns([2,2])

    with col1:
        with st.expander(" ℹ️ Information", expanded=True):
            st.write("""
            Heart guess info [...]
            """)
        '''
        ## How does it work ❓
        Complete all the parameters and the machine learning model will predict [...] based on various parameters
        '''

    with col2:
        st.subheader("Info on the subject :")
        age = st.number_input("Age", 42)
        trestbps = st.number_input("trestbps", 42)
        chol = st.number_input("chol", 42)
        thalach = st.number_input("thalach", 42)
        oldpeak = st.number_input("oldpeak", 42)
        slope = st.number_input("slope", 42)
        ca = st.number_input("ca", 42)
        thal = st.number_input("thal", 42)

        feature_list = [age, trestbps, chol, thalach, oldpeak, slope, ca, thal]
        single_pred = np.array(feature_list).reshape(1,-1)

        if st.button('Predict'):
            loaded_model = load_model('model.pickle')
            prediction = loaded_model.predict(single_pred)

            col1.write('''
                    ## Results 🔍
                    ''')
            col1.write(f"{prediction.item()}")

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

if __name__ == '__main__':
	main()
