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


def load_model(modelfile):
        loaded_model = pickle.load(open(modelfile, 'rb'))
        return loaded_model

st.set_page_config(page_title="Heart Disease", page_icon="https://www.freeiconspng.com/thumbs/heart-png/heart-png-15.png", layout='centered', initial_sidebar_state="collapsed")

def main():
    html_temp = """
    <div>
    <h1 style="color:MEDIUMSEAGREEN;text-align:left;"> Heart guess</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    col1, col2 = st.columns([2,2])

    with col1:
        with st.expander(" ℹ️ Information", expanded=True):
            st.write("""
            With the still growing amount of victims from the covid-19's vaccine,
	    more and more people are suffering from its side effect. Like any vaccine, 
	    COVID-19 vaccines can cause mild, short term side effects, such as a 
	    low-grade fever or pain or redness at the injection site. Most reactions 
	    to vaccines are mild and go away within a few days on their own. More 
	    serious or long-lasting side effects to vaccines are also possible. 
	    One of the more serious and long-lasting side effect is the myocarditis, 
	    a type of heart disease which affects thousands after the vaccination. 
	    However it is not the only heart disease possible side effect from the vaccination. 
	    Therefore we deployed an AI able to identify and/or predict if someone might or 
	    might not have a heart disease.
            """)
        '''
        ## How does it work ❓
        Simply fill in all the parameters 
	with your or your friends 
	informations and hit predict. The 
	AI will infer if the information
	corresponds to a patient with a 
	heart disease or not. Moreover, 
	if you want to test it out, you
	can just invent values for each 
	parameters and see which result 
	you will get.
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
            if prediction.item() == 0:
                col1.write("The patient has a heart disease")
            elif prediction.item() == 1:
                col1.write("The patient does not have a heart disease")

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

if __name__ == '__main__':
	main()
