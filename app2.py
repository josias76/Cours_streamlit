import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt




#création du tableau de la loi normale
data = np.random.normal(size=1000)
# transformation en dataframe
data = pd.DataFrame(data, columns=["Dist_norm"])

#Affichage de cette dataframe sur l'application Streamlit
#st.write(data.head())
st.dataframe(data.head())

#Affichage du graphique
fig, ax = plt.subplots()
ax.hist(data.Dist_norm)
st.pyplot(fig)