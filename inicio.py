import streamlit as st
import pandas as pd

st.title('El mejor Pokemon')

st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQepGGijcbZSBi1FpzNoTmlVK9rudUMZ2dMHj80EPxyPQ&s=10')

st.write('made by mtrxgamer')

df = pd.read_csv('https://raw.githubusercontent.com/mtrxgamer/proyecto_uno/refs/heads/main/pokemon.csv')

st.write(df)