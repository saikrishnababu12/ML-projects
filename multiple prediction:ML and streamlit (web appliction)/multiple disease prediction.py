# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:02:38 2024

@author: inampudicharan
"""

import streamlit as st
import pickle
from streamlit_option_menu import option_menu
hloaded_model=pickle.load(open("C:/Users/inampudicharan/Downloads/hear_disease_model.sav",'rb'))
dloaded_model=pickle.load(open('C:/Users/inampudicharan/Downloads/diabetes_model.sav','rb'))

with st.sidebar:
    selected=option_menu("Multiple Disease prediction system",
                         ["Diabetes Prediction","heart Disease prediction"
                          ],default_index=0)
if(selected=="Diabetes Prediction"):
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
        cp=st.text_input('chest pain type(4 values)')
        trestbps= st.text_input('resting bps value')
        chol= st.text_input('serum cholestoral value')
        fbs= st.text_input('fasting blood suger value')
        restecg= st.text_input('resting electrocardiographic result value')
        thalach= st.text_input('max heart rate value')
        exang= st.text_input('exercise induced angina')
        oldpeak= st.text_input('oldpeak value')
        slope= st.text_input('slope value')
        ca= st.text_input('number of major vessels colored by flourosopy')
        output=''
        if(st.button("test result")):
          output=heart_prediction(age ,sex ,cp	,trestbps,chol	,fbs	,restecg	,thalach	,exang,	oldpeak,	slope,	ca)
        
        st.success(output)
    main()
if(selected=="heart Disease prediction"):
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
    main()
    