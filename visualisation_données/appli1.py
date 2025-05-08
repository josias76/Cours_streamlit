import pandas as pd
import numpy as np
import streamlit as st


st.title("Initialisation à la Data visualisation avec streamlit")
st.subheader("Auteur : josias_nteme")
st.markdown("***Cette application affiche différents types de graphiques***")


random_data = np.random.normal(size=1000)
#création d'un graphique linéaire
st.line_chart(random_data)

#Diagramme à bar
bar_data = pd.DataFrame(
    [100,19,88,54],
    ["A","B","C","D"]
)
st.bar_chart(bar_data)
# Carte

df = pd.read_excel("new_york.xlsx").head(100)
st.write(df.head(10))
#st.map(df[['longitude','latitude']])