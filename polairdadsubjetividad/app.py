import os
import streamlit as st
from PIL import Image
from textblob import TextBlob
from googletrans import Translator

# Asegúrate de que esta ruta es correcta
image_path = os.path.join("polairdadsubjetividad", "roboto.jpg")

translator = Translator()

st.markdown("""
    <style>
    .title {
        font-family: 'Arial', sans-serif;
        color: #2E86C1;
    }
    .header {
        font-family: 'Courier New', Courier, monospace;
        color: #FFFFFF;
    }
    .content {
        font-family: 'Verdana', sans-serif;
        color: #FFFFFF;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h0 class="title">¿Estas listo para aprender?</h0>', unsafe_allow_html=True)
st.markdown('<h2 class="header">Uso de TextBlob</h2>', unsafe_allow_html=True)
st.markdown('<p class="content">Por favor, escribe en el campo de texto la frase que deseas analizar</p>', unsafe_allow_html=True)

# Asegúrate de que la imagen exista en la ruta especificada
if os.path.exists(image_path):
    image = Image.open(image_path)
    st.image(image, caption="Análisis")
else:
    st.error(f"No se encontró la imagen en la ruta: {image_path}")

st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")

with st.sidebar:
    st.subheader("Polaridad y Subjetividad")
    st.markdown("""
    Polaridad: Indica los sentimientos que se expresan en el texto.
    Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.

    Subjetividad:Mide el contenido que varia segun la percepcion de la persona. Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.
    """)

with st.expander('Analizar Polaridad y Subjetividad en un texto'):
    text1 = st.text_area('Escribe por favor:')
    if text1:
        blob = TextBlob(text1)
        st.write('Polarity: ', round(blob.sentiment.polarity, 2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity, 2))

        polarity = round(blob.sentiment.polarity, 2)
        if polarity >= 0.5:
            st.write('Es un sentimiento Positivo')
        elif polarity <= -0.5:
            st.write('Es un sentimiento Negativo')
        else:
            st.write('Es un sentimiento Neutral')

with st.expander('Corrección en inglés'):
    text2 = st.text_area('Escribe por favor:', key='4')
    if text2:
        blob2 = TextBlob(text2)
        st.write(blob2.correct())
