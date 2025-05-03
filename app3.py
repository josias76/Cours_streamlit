import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt


st.title("Application de Distribution normale")
st.subheader("Auteur : josias_nteme")
st.write(
    ("Cette application permet d'afficher l'histogramme d'une distribution normale."
     " L'utilisateur a la possibilité de varier le nombre de bins de l'histogramme"
    "et de donner un titre au graphique. ")
)
#création du tableau de la loi normale
data = np.random.normal(size=1000)
# transformation en dataframe
data = pd.DataFrame(data, columns=["Dist_norm"])

#Affichage de cette dataframe sur l'application Streamlit
#st.write(data.head())
st.dataframe(data.head())

#Affichage du graphique avec une interraction de l'utilisateur 
fig, ax = plt.subplots()
n_bins = st.number_input(
    label = "Choisis un nombre de bins",
    min_value = 10,
    value = 20
)
ax.hist(data.Dist_norm,bins= n_bins)
graph_title = st.text_input(
    label= "Ecrire le titre du graphique"
)
plt.title(graph_title)
st.pyplot(fig)