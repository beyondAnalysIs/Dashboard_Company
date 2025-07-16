import streamlit as st 
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Configuración de la página

st.set_page_config(
    page_title='Dashboard Company 20025',
    page_icon='🎇',
    layout='wide',
    initial_sidebar_state= 'expanded'
)
 
def generar_datos_empresa():
    fechas = pd.date_range(start='2025-01-01', end=datetime.today(), freq='D')
    datos = {
        'fecha' : fechas,
        'ingresos_diarios' : np.random.normal(50000,15000,len(fechas)),
        'usuarios_activos' : np.random.normal(12000,3000,len(fechas)),
        'conversion_rate' : np.random.normal(2.5,0.8,len(fechas)),
        'costo_adquisicion' : np.random.normal(45,12,len(fechas)),
        'ltv_cliente' : np.random.normal(180,40,len(fechas))      
    }
    
    df = pd.DataFrame(datos)
    df['ingresos_diarios'] *= (1 + np.arange(len(df)) * 0.0001) # tendencia
    return df

df = generar_datos_empresa()


# Título principal
st.markdown('<h1 class="main-header">🏆 Dashboard Company 20025</h1>', unsafe_allow_html=True)


