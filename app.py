import streamlit as st
import requests 
from streamlit_lottie import st_lottie
from PIL import Image
    
st.set_page_config(page_title="Salfa Forestal", page_icon="images/logo.png",layout="wide")
 
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")        

# ---LOAD ASSETS

lottie_coding = load_lottieurl("https://lottie.host/343b520f-3fe8-4ddb-a1c9-20d29bd145ef/jPuC5JiaSo.json")
img_contact_form = Image.open("images/sala.jpg",)
img_dashboard = Image.open("images/dashboard.png")


# -- HEADER SECTION ---
with st.container():
    st.subheader("Bienvenidos a Telemetría Forestal ")
    st.title("Análisis de datos con Telemetría FORESTLINK ")
    st.write("Con estas herramientas personalizadas podrá ver su producción y estados de su máquinna")
    st.write("[Quieres saber mas >](https://salfamaquinaria.cl/post-venta/telemetria/#jdlink)")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Nuestro sistema de telemetría")
        st.write("##")
        st.write(
    """
    Dentro del centro de monitoreo ForestLink, contamos con Operation Center, el software de monitoreo desarrollado por John Deere para controlar el funcionamiento, desempeño y códigos de falla de la maquinaria John Deere. La plataforma le permitirá a nuestros clientes de pequeñas, grandes y medianas flotas:
Monitorear: Comprender las medidas de éxito fundamentales y el desempeño del proyecto relacionados con la seguridad, la productividad y la calidad del lugar de trabajo, tanto anivel de la máquina como del lugar de trabajo.
Comunicar: Compartir datos de trabajo y productividad entre las máquinas y mejorar la productividad como equipo de trabajo.
    
    """
        )
        
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
        
# -- CUANDRO PRINCIPAL

with st.container():
    st.write("---")
    st.header("Dashboard Personalizados")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        
        st.image(img_dashboard)
    with text_column:
        st.subheader("Crearemos tu dashboard a tu medida ") 
        st.write("""
                 ¡Crearemos tu Dashboard a medida y según tus necesidades de monitoreo!
                 Además estamos trabajando para que pronto tengas tu App personalizada.
                 """)   
       
             
        
# --- PRIMER CUADRO        
with st.container():
    st.write("---")
    #st.header("Sala de Telemetría")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("En esta sala se monitorea el pulso de cada equipo") 
        st.write("""
                 ¡¡¡Imaginate tener este servicio totalmente gratuito por la compra de tu máquina
                 o si ya eres cliente solo escríbenos y coordinaremos para trabajar en tu dashboard!!!.
                 """)   
        st.subheader("CONTÁCTATE CON UN ASESOR") 
        
        
        contact_form = """
        
       <form action="https://formsubmit.co/rperaltag@salfa.cl" method="POST">
        <input type="hidden" name="_captcha" value=""false>
        <input type="text" name="name" placeholder= "Su nombre" required>
        <input type="email" name="email" placeholder="Su email"required>
        <textarea name="mensaje" placeholder="Escriba su mensaje aquí" required></textarea>
        <button type="submit">Enviar</button>
        </form>
        
        """
        
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
            with right_column:
                st.empty()
        
    