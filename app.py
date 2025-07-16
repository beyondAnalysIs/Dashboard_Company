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

# filtros de búsqueda
col1,col2,col3 = st.columns(3)
with col1:
    periodo = st.selectbox('📅 Periodo:',['Últimos 30 días', 'Último Trimestre', 'Último año'])

with col2:
    categoria = st.selectbox('📌 Categoría:',['General', 'Ventas', 'Marketing', 'Producto'])
    
with col3:
    comparacion = st.selectbox('📊 Comparación:',['Periodo anterior', 'Año pasado', 'Promedio'])
    
# Kpis
st.markdown('## 📊 KPIs')
col1,col2,col3,col4 = st.columns(4)

with col1:
    ingresos_total = df['ingresos_diarios'].sum()
    st.metric('💶 Ingresos Totales', f'€{ingresos_total:,.0f}', f'{np.random.uniform(5,15):,.1f}%')

with col2:
    usuarios_prom = df['usuarios_activos'].mean()
    st.metric('👥 Usuarios Activos', f'{usuarios_prom:,.0f}', f'{np.random.uniform(2, 8):,.1f}%')
    
with col3:
    conversion = df['conversion_rate'].mean()
    st.metric('🔀 Tasa de conversión', f'{conversion: .2f}', f'{np.random.uniform(-0.5,1.2):.2f}%')

with col4:
    costo_adq = df['costo_adquisicion'].mean()
    st.metric('💰 CAC Promedio', f'€{costo_adq: .0f}', f'{np.random.uniform(2, 8):.1f}%')        

# Gráficos interactivos con plotly
st.markdown('## 📊 Gráficos Interactivos')

col1,col2 = st.columns(2)

with col1:
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['fecha'], y=df['ingresos_diarios'], mode='lines', name='Ingresos Reales', line=dict(color='#1f4e79')))
    z = np.polyfit(range(len(df)), df['ingresos_diarios'], 1) # Regresión Lineal
    p = np.poly1d(z) #función evaluable
    fig.add_trace(go.Scatter(x=df['fecha'], y=p(range(len(df))), mode='lines', name='Tendencia', line=dict(color="#E33131", dash='dash')))
    fig.update_layout(title='💶 Evolución de Ingresos', height=400, template='plotly_white')
    st.plotly_chart(fig,use_container_width=True)
    
# Funel de conversión
with col2:
    etapas = ['Visitantes', 'Leads', 'Oportunidades', 'Clientes']
    valores = [10000, 2500, 625, 156]
    funnel = go.Figure(go.Funnel(y=etapas, x=valores, textinfo='value+percent initial'))
    funnel.update_layout(title='🎯 Funnel de Conversión', height=400, template='plotly_white')
    st.plotly_chart(funnel, use_container_width=True)