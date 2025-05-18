import streamlit as st 
import numpy as np 
import joblib


#navicon and header
st.set_page_config(page_title="prediction", page_icon="📈", layout="wide")  
st.title("Prédiction du prix d'une voiture en fonction des ses caractèristiques")
st.subheader("Cette application est réalisé par josias_nteme")
st.markdown("***Cette application utilise un modèle de Machine Learning pour prédire le prix d'une voiture***")


# chargement du modèle
model = joblib.load(filename="final-model.joblib")



# Définition d'une fonction d'inference
def inference (symboling,normalized_losses,wheel_base,length,width,heigh,curb_weight ,engine_size,bore,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg):
    new_data = np.array([
        symboling,normalized_losses,wheel_base,length,
        width,heigh,curb_weight ,engine_size,bore,stroke,
        compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg

    ])

    pred = model.predict(new_data.reshape(1,-1))
    return pred
# L'utilisateur saisie une valeur pour chaque caaractèristique de la voiture


symboling = st.number_input(label ="symboling :",min_value=0, value=3)
normalized_losses = st.number_input("normalized_losses :", value=100)
wheel_base= st.number_input("wheel_base :", value=90)
length = st.number_input("length :", value=150)
width = st.number_input("width  :", value=150)
heigh= st.number_input("heigh :", value=65)
curb_weight = st.number_input("curb_weight :",value=200)
engine_size =  st.number_input("engine-size :", value=120)
bore = st.number_input("bore :", value=3.0)
stroke = st.number_input("stroke", value=3.0)
compression_ratio = st.number_input("compression-ratio :", value=90)
horsepower = st.number_input("horsepower :", value=110)
peak_rpm = st.number_input("peak-rpm :",value=5000)
city_mpg = st.number_input("city-mpg :", value=20)
highway_mpg = st.number_input("highway-mpg :", value=30)


# création du bouton " predict" qui retourne la prédiction

if st.button("Predict"):
    prediction = inference (
        symboling,normalized_losses,wheel_base,length,
        width,heigh,curb_weight ,engine_size,bore,stroke,
        compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg

    )
    resultat = "Le prix(en dollars) de cette voiture est égal à : " + str(prediction[0])
    st.success(resultat)





# bande de bas de pages
st.markdown("""
    <hr style="border-top: 1px solid #4CAF50; margin-top: 50px;"/>
    <div style="text-align: center; color: #888; font-size: 0.9em;">
        &copy; 2025 <strong>Josias Nteme</strong> - Tous droits réservés.
    </div>
""", unsafe_allow_html=True)