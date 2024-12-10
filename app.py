import streamlit as st
import requests, random

API_KEY = 'ac9d6eb2db11ddbdcf38a14178051db767191ea9' 
EMOJI_API_URL = 'https://emoji-api.com/emojis'

st.title("Random Emoji Generator")

if st.button("Get Random Emoji"):
    response = requests.get(EMOJI_API_URL, params={'access_key': API_KEY})
    emojis = response.json()
    chosen_emoji = random.choice(emojis)    
    character = chosen_emoji['character']
    st.write(f"<div style='font-size:72px;'>{character}</div>", unsafe_allow_html=True)
else:
    st.write("Button not clicked yet!")