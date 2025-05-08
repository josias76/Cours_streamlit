import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as plt 


############################ Plotly #######################################
st.subheader("Plotly")

#dataframe des temperature hebdomadaires 

temps = pd.DataFrame(

    {'day': ["Monday",'Tuesday',"Wednesday",'Thursday',"Friday","Saturday",'Sunday'],
     "temp":[28,27,25,31,32,35,36]


    }
)


