import streamlit as st
import pandas as pd

st.title("Meu primeiro dashboard")

st.subheader("3A1")

st.write("Ola, mudo!")

nome = st.text_input("Digite seu nome")

st.write("Ola,", nome)

df = pd.DataFrae({'disciplina': ["Python", "Maematica", "Portugues"], 'nota': [10, 5, 0]})