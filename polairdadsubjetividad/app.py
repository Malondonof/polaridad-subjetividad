import streamlit as st
from PIL import Image
from textblob import TextBlob
from googletrans import Translator

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

st.markdown('<h1 class="title">¿Como te sientes hoy?</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="header">Uso de textblob</h2>', unsafe_allow_html=True)
st.markdown('<p class="content">Por favor escribe en el campo de texto la frase que deseas analizar</p>', unsafe_allow_html=True)

image = Image.open("roboto.jpg")
st.image(image,caption = "analisis")

st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")

with st.sidebar:
               st.subheader("Polaridad y Subjetividad")
               ("""
                Polaridad: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
                Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.
                
               Subjetividad: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
               (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.

                 """
               ) 


with st.expander('Analizar Polaridad y Subjetividad en un texto'):
    text1 = st.text_area('Escribe por favor: ')
    if text1:

        #translation = translator.translate(text1, src="es", dest="en")
        #trans_text = translation.text
        #blob = TextBlob(trans_text)
        blob = TextBlob(text1)
       
        
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
        x=round(blob.sentiment.polarity,2)
        if x >= 0.5:
            st.write( 'Es un sentimiento Positivo 😊')
        elif x <= -0.5:
            st.write( 'Es un sentimiento Negativo 😔')
        else:
            st.write( 'Es un sentimiento Neutral 😐')

with st.expander('Corrección en inglés'):
       text2 = st.text_area('Escribe por favor: ',key='4')
       if text2:
          blob2=TextBlob(text2)
          st.write((blob2.correct())) 
