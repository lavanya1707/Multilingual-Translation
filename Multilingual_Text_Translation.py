import streamlit as st
from translate import Translator

# List of target languages
languages = {
    'fr': 'French',
    'it': 'Italian',
    'es': 'Spanish',
    'ru': 'Russian',
    'de': 'German',
    'kn': 'Kannada',
    'hi': 'Hindi',
    'te': 'Telugu',
    'bn': 'Bengali',
    'ml': 'Malayalam',
    'ta': 'Tamil'
}

# Streamlit app title
st.title('Multilingual Text Translation')

# Input text area for user input
text = st.text_area('Enter the text to translate:', '')

# Button to trigger translation
if st.button('Translate'):
    if text:
        st.subheader('Translations:')
        for lang_code, lang_name in languages.items():
            translator = Translator(to_lang=lang_code)
            translation = translator.translate(text)
            st.write(f'{lang_name}: {translation}')
    else:
        st.warning('Please enter text for translation.')
