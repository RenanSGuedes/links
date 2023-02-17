import streamlit as st
from PIL import Image

st.title(":speech_balloon: Welcome!")
image = Image.open('./quasar.png')
st.image(image)
st.header("_Aplicações_")

col1, col2, col3 = st.columns(3)

with col1:
    st.write(":alien: :green[TWILIO (WHATS)]")
    st.markdown(
        "[![Foo](https://i.imgur.com/xLUAqd6.png)](https://sheets-twilio.streamlit.app/)")

with col2:
    st.write(":space_invader: :blue[COMPILADOR CSV (UPL)]")
    st.markdown(
        "[![Foo](https://i.imgur.com/wWAOXvS.png)](https://compilador-csv.streamlit.app/)"
    )

with col3:
    st.write(":cow: CONTAGEM (BHN)")
    st.markdown(
        "[![Foo](https://i.imgur.com/xmHRZ0h.png)](https://contagem.streamlit.app/)"
    )
