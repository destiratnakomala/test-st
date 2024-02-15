import streamlit as st
import pandas as pd

fname = st.text_input("Enter Name:")
age = st.number_input("How old are you?")
gender = st.radio("2) Are you a male or female?",["-","Female","Male"],key="Q02")
		
result = {
	'name':fname,
	'age':age,
	'gender':gender,
	}


with st.expander("CONTINUE"):
	answer = pd.DataFrame(result,index=[0])
	answer.to_csv('data/answer.csv',index=False)
	st.write(answer)
