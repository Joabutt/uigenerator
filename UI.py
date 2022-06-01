import streamlit as st
import openai
import os
from ml_backend import ml_backend
openai.api_key = os.getenv("OPENAI_API_KEY")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("UI generator")

backend = ml_backend() 



 

with st.form(key="form"):
    prompt = st.text_input("Input your parameters for your desired app.")
    st.text(f"Example: Generate a comprehensive user interface for an app with html that shows different kinds of features, and style it with css.")

    submit_button = st.form_submit_button(label='Submit!')
     
            
     
    if submit_button:
        with st.spinner("Connecting and generating... Please give it awhile to generate code, espically for large inputs."):
            output = backend.ui(prompt)
        st.markdown("# 🟢Reply:")
        st.code(output, language='html')
        

        
