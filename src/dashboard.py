import nltk
import streamlit as st
from password_generator import PinGenerator, RandomPasswordGenerator, MemorabalePasswordGenerator

try:
    nltk.data.find('corpora/words')
except LookupError:
    nltk.download('words')

st.title(":closed_lock_with_key: Password Generator")


option = st.radio(
    "Please select your password type:",
    ("Random Password", "Memorable Password", "Pin Code")
)

if option == 'Pin Code':
    length = st.slider("Please select the length of your pin code.", 4, 32)
    generator = PinGenerator(length)
elif option == "Random Password":
    length = st.slider("Select the length of your password.", 8, 64)
    include_numbers = st.toggle("Include Numbers")
    include_symbols = st.toggle("Include Symbols")    
    generator = RandomPasswordGenerator(length, include_numbers, include_symbols)
elif option == "Memorable Password":
    num_of_words = st.slider("Number of words", 2, 8)
    separator = st.text_input("Separator")
    capitalize = st.toggle("Random Capitalize")
    generator = MemorabalePasswordGenerator(num_of_words,separator, capitalize)

password = generator.generate()
st.write(f"Your password is: {password}")
