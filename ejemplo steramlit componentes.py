import datetime
import pandas as pd
import streamlit as st

# Título principal de la aplicación
st.title("Sistema de registro y carga de datos")

# --- 1. DATOS PERSONALES (text_input, slider, date_input) ---
st.subheader("1. Información del usuario")

nombre = st.text_input("¿Cómo te llamas?")
edad = st.slider("Selecciona tu edad", min_value=0, max_value=100, value=25)
fecha_nacimiento = st.date_input("Selecciona tu fecha de nacimiento", datetime.date(2000, 1, 1))

# --- 2. PREFERENCIAS (selectbox, radio) ---
st.subheader("2. Preferencias")

color_favorito = st.selectbox("¿Cuál es tu color favorito?", ["Rojo", "Azul", "Verde"])
genero_musical = st.radio("Elige tu género musical preferido", ["Pop", "Rock", "Jazz"])

# --- 3. COMENTARIOS ADICIONALES (text_area) ---
st.subheader("3. Observaciones")

mensaje = st.text_area("Escribe tus comentarios o notas sobre el registro:")

# --- 4. CARGA DE ARCHIVOS (file_uploader) ---
st.subheader("4. Carga de archivo de datos")

archivo = st.file_uploader("Elige un archivo CSV para inspeccionar", type="csv")

if archivo is not None:
    df = pd.read_csv(archivo)
    st.write("Vista previa de los datos cargados:")
    st.write(df)

# --- 5. ACCIÓN FINAL (button y st.write) ---
st.write("---")

if st.button("Procesar registro"):
    if nombre.strip() == "":
        st.write("Por favor, ingresa al menos un nombre para continuar.")
    else:
        st.write("### Resumen del registro generado:")
        
        # Uso de st.write para texto con formato y variables
        st.write(f"**Usuario:** {nombre}")
        st.write(f"**Edad registrada:** {edad} años")
        st.write(f"**Fecha seleccionada:** {fecha_nacimiento}")
        st.write(f"**Color favorito:** {color_favorito}")
        st.write(f"**Género musical:** {genero_musical}")
        st.write(f"**Mensaje/Notas:** {mensaje if mensaje else '(Sin observaciones)'}")
        
        # Demostración de st.write mostrando una lista/estructura de datos directa
        st.write("Valores empaquetados para inferencia/procesamiento:")
        st.write([nombre, edad, str(fecha_nacimiento), color_favorito, genero_musical])