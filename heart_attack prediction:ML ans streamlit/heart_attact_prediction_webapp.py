# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:05:14 2024

@author: inampudicharan
"""

import numpy as np
import pickle
import streamlit as st
loaded_model=pickle.load(open("C:/Users/inampudicharan/Downloads/hear_disease_model.sav",'rb'))
def heart_prediction(dataset):
 input_datanum=np.asarray(dataset)
 input_data_reshape=input_datanum.reshape(1,-1)
 prediction=loaded_model.predict(input_data_reshape)
 print(prediction)
 if(prediction[0]==0):
   return "person does not have heart disease"
 else:
    return "person has heart disease"


def main():
    st.title("heart attact prediction")
    age=st.text_input('Age')
    sex=st.text_input('Gender')
    cp=st.text_input('cp value')
    trestbps= st.text_input('trestbps value')
    chol= st.text_input('cholerstrol value')
    fbs= st.text_input('fbs value')
    restecg= st.text_input('restecg value')
    thalach= st.text_input('thalach value')
    exang= st.text_input('exang value')
    oldpeak= st.text_input('oldpeak value')
    slope= st.text_input('slope value')
    ca= st.text_input('ca value')
    output=''
    if(st.button("test result")):
      output=heart_prediction(age ,sex ,cp	,trestbps,chol	,fbs	,restecg	,thalach	,exang,	oldpeak,	slope,	ca)
    
    st.success(output)
if __name__=='__main__':
    main()
    
    