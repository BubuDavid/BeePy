import streamlit as st
from tools import styles
import random

styles.get_bootstrap_styles()
styles.get_bootstrap_scripts()
styles.load_my_styles()
styles.load_header()


# Frase inicial
st.markdown(
    """
		<h1 class="text-center">
			Talleres<span class='color-yellow'>,</span> conferencias<span class='color-yellow'>,</span> programación<span class='color-yellow'>,</span> Python y más<span class='color-yellow'>...</span>
        </h1>
    """,
	unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
	images = [
		'https://i.imgur.com/jAQILyd.jpg',
		'https://i.imgur.com/OVNsYDy.jpg',
		'https://i.imgur.com/EGjQzQY.jpg',
		'https://i.imgur.com/T7pglCl.jpg',
		'https://i.imgur.com/NaAIdil.jpg',
		'https://i.imgur.com/cWjWIBC.jpg',
		'https://i.imgur.com/HQJ6HAQ.jpg',
	]
	st.image(random.choice(images), use_column_width=True)

with col2:
	# Acerca del evento
	st.markdown(
		"""
			<h2 class="title"> Acerca del evento 🐍</h2>
			<p class="text">
				BeePy, es un evento enfocado en talleres de programación, especialmente en Python, diseñados para dar a conocer el potencial de la programación en diversas áreas de la ciencia y ayudar a los estudiantes de la DCI a aplicar lo aprendido en sus respectivos campos científicos. Además, busca difundir la importancia de las ciencias de datos y ciencias computacionales como herramientas para resolver problemas de manera eficiente y accesible.
			</p>
		""",
		unsafe_allow_html=True)
	

# Register section
st.markdown(
	"""
		<h2 class="title"> Regístrate 📝</h2>
		<p class="text">
			Para participar en el evento, debes registrarte en el siguiente formulario:
		</p>
		<div class="text-center">
			<a href="https://forms.gle/HHNswqvHMUgm2zVh6"> <button class="btn" id="register-btn"> Registrarme </button> </a>
		</div>
	""",
	unsafe_allow_html=True)

# Footer
st.markdown(
	"""
	<div class="footer">
		<p class="text-center">
			Hecho en <a href="http://streamlit.io" target="_blank"> <img src="https://i.imgur.com/iIOA6kU.png" class="footer__img" alt="Streamlit Logo"></a> con ❤️ por <a href="https://github.com/Bubudavid" target="_blank">Bubu</a> para la DCI 🐝
		</p>
	""",
unsafe_allow_html=True)

