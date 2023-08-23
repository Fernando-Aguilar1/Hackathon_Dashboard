import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


@st.cache  # Esto permite que los datos solo se carguen una vez, en lugar de recargarlos cada vez que cambia la aplicación.
def load_data():
    return pd.read_csv("data.csv")

data = load_data()
st.write(data)


def plot_bar_chart_NN(data):
    fig, ax = plt.subplots()
    ax.bar(data["Equipo"], data["Score"])
    ax.set_xlabel("Nombre del equipo")
    ax.set_ylabel("Score del modelo")
    ax.set_title("Neural Network Model")
    return fig

fig = plot_bar_chart_NN(data)


def plot_bar_chart_ST(data):
    fig, ax = plt.subplots()
    ax.bar(data["Equipo"], data["Score"])
    ax.set_xlabel("Nombre del equipo")
    ax.set_ylabel("Score del modelo")
    ax.set_title("Series Time  Model")
    return fig

fig_1 = plot_bar_chart_ST(data)

def load_data():
    return pd.read_csv("data.csv")

data = load_data()

st.write(data)

st.pyplot(fig)
st.pyplot(fig_1)

