import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px


############################ Plotly #######################################
st.subheader("Plotly")

#dataframe des temperature hebdomadaires 
dict = {'day': ["Monday",'Tuesday',"Wednesday",'Thursday',"Friday","Saturday",'Sunday'],
     "temp":[28,27,25,31,32,35,36],
     "habitant":[125.15,450.12,584.65,78.25,79.12,20.26,15.8],
     'PIB':[12,458,36,147,25,148,100]
     
     }


temps = pd.DataFrame(dict)
#st.write(temps)
# Diagramme à barre interractif avec plotly
fig1 = px.bar(data_frame = temps,
             x= 'day',
             y= "temp",
             title = "Temperatures moyennes journalières")
st.plotly_chart(fig1)

# Diagramme à bar avec d'autres fonctionnalité
fig2 = px.bar(data_frame = temps,
             x= 'day',
             y= "temp",
             hover_data=["habitant",'PIB'],
             color='PIB',
             title = "Evolution de la Temperature moyennes journalières en tenant compte du PIB ")
st.plotly_chart(fig2)

# Nuages de point interactif
cars = pd.read_csv("automobile.csv")
st.dataframe(cars)