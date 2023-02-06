import streamlit as st
from PIL import Image

st.title(":speech_balloon: Welcome!")
image = Image.open('./quasar.png')
st.image(image)
st.header("_Aplicações_")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader(":alien: :green[TWILIO]")
    st.markdown(
        "[![Foo](https://i.imgur.com/xLUAqd6.png)](https://sheets-twilio.streamlit.app/)")

with col2:
    st.subheader(":space_invader: :blue[COMPILADOR CSV]")
    st.markdown(
        "[![Foo](https://i.imgur.com/wWAOXvS.png)](https://compilador-csv.streamlit.app/)"
    )

with col3:
    st.subheader(":cow: CONTAGEM BHN")
    st.markdown(
        "[![Foo](https://i.imgur.com/xmHRZ0h.png)](https://contagem.streamlit.app/)"
    )
