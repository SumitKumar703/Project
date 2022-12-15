# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 15:53:02 2022

@author: kumar
"""

import numpy as np
import pandas as pd
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open("D:\\execlr\\Project\\trained_model.sav",'rb'))

# creating a function for Forecasting
def Gold_Price_Forecasting(input_data):
     prediction=loaded_model.forecast(input_data)
     return(prediction)
  
def load_data(fo):
    return pd.DataFrame(
        {
            "Price": fo[0:]
        }
    )


   

def main():
    # giving the title
    st.title('Gold_Price_Forecasting Web App')
    
    #getting Input days
    Days = st.number_input("Number of days")
    
    # Code for Forecasting
    forecasting = ""
    df=""
    # Creating a button for Prediction
    
    if st.button("Forecast"):
        Input = Days
        forecasting=Gold_Price_Forecasting(Input)
        df=load_data(forecasting)
    
    st.success(st.write(df))

if __name__=='__main__':
    main()