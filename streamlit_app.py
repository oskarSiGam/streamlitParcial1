import pandas as pd
import streamlit as st
#import plotly.express as px

dfCalificaciones = pd.read_excel("tareas.xlsx")

dfCalificaciones["promedio"]= (dfCalificaciones["tarea1"]+dfCalificaciones["tarea2"]+dfCalificaciones["tarea3"]+dfCalificaciones["tarea4"])/4

dfCalificaciones["status"]=dfCalificaciones["promedio"].apply(lambda x: "APROBADO" if (x >= 70)else "REPROBADO")

dfResultados = dfCalificaciones[["matricula","promedio","status"]]

dfResultados

st.dataframe(dfResultados)

#fig = px.bar(dfResultados, x='status', y=dfResultados["status"].value_counts())

#st.plotly_chart(fig)
