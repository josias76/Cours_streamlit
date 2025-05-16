import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px

#navicon and header
st.set_page_config(page_title="Data_viz2", page_icon="📈", layout="wide")  
st.title("Data visualisation avec streamlit")
st.subheader("Auteur : josias_nteme")
st.markdown("***Cette application affiche différents types de graphiques***")
st.write(
    ("Cette application permet d'afficher l'histogramme d'une distribution normale."
     " L'utilisateur a la possibilité de varier le nombre de bins de l'histogramme"
    "et de donner un titre au graphique. "))




############################ Plotly #######################################
st.subheader("Plotly Express dans Streamlite")

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

numeric_cols = cars.select_dtypes(exclude='object').columns.to_list()
var_x = st.selectbox("Choisis la variable en abscisse", numeric_cols)
var_y = st.selectbox("Choisis la variable en ordonnée", numeric_cols)
categoriel_cols = cars.select_dtypes(include='object').columns.to_list()
var_col = st.selectbox("Choisis la variable pour colorier les points", categoriel_cols)

fig3 = px.scatter(
    data_frame=cars,
    x=var_x,
    y=var_y,
    color=var_col,
    title=str(var_y) + " Vs " + str (var_x)
)
st.plotly_chart(fig3)

############################ Matplotlib et seaborn #######################################
st.subheader("Matplotlib et Seaborn dans Streamlite")
airbnb = pd.read_excel("new_york.xlsx")
st.subheader("1.Seaborn")

fig_sb, ax_sb = plt.subplots()
ax_sb = sns.histplot(airbnb['days_occupied'])
plt.xlabel("Nombre de jours d'occupation de l'appartement")
st.pyplot(fig_sb)



st.subheader("2.Matplotlib")
fig_mt, ax_mt = plt.subplots()
ax_mt=plt.hist(airbnb['days_occupied'])
plt.xlabel("Nombre de jours d'occupation de l'appartement")
st.pyplot(fig_mt)



st.markdown("""
    <hr style="border-top: 1px solid #4CAF50; margin-top: 50px;"/>
    <div style="text-align: center; color: #888; font-size: 0.9em;">
        &copy; 2025 <strong>Josias Nteme</strong> - Tous droits réservés.
    </div>
""", unsafe_allow_html=True)