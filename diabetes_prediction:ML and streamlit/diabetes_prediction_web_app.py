# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 09:03:09 2024

@author: inampudicharan
"""
import numpy as np
import pickle
import streamlit as st
loaded_model=pickle.load(open('C:/Users/inampudicharan/Downloads/diabetes_model.sav','rb'))

def diabetes_prediction(input_data):
    
 input_numpy=np.asarray(input_data)
 input_reshape=input_numpy.reshape(1,-1)
 #std_data=scaler.transform(input_reshape)
 p=loaded_model.predict(input_reshape)
 print(p)
 if(p[0]==0):
  return "Non-Diabetic"
 else:
   return "Diabetic"

 
def main():
    st.title("Diabetes prediction")
    Pregnancies = st.text_input("Number of pregnancies")
    Glucose=st.text_input("Glucose level")
    BloodPressure=st.text_input("BloodPressure value")
    SkinThickness= st.text_input("SkinThickness level")
    Insulin =st.text_input("Insulin level")
    BMI=st.text_input("BMI value")
    DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction level")
    Age=st.text_input("Age")
    
    diagnolisis=""
    if(st.button("Diabetes test result")):
        diagnolisis= diabetes_prediction([Pregnancies ,Glucose ,BloodPressure ,SkinThickness ,Insulin  ,BMI ,DiabetesPedigreeFunction ,Age])
    st.success(diagnolisis)
if __name__=="__main__":
    main()
        
        
        
    
    