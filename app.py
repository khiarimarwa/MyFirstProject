import streamlit as st 
import pandas as tab
st.title ("Marwa Site")
st.write ("Bienvenue sur mon site web")

data = {"Nom" : ["Alice", "Bob", "Marwa"],
        "Age" : [10,25,26] }
        df = tab.DataFrame(data)

st.dataframe(df)
