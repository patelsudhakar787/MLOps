import streamlit as st

# st.title("Hello StreamLit")
# st.write("This is Simple Streamlit app")

st.title("Interative Streamlit App")

#Input for Name
name = st.text_input("Enter your Name")

if name:
    st.write(f'Hello, {name}!')

#Select Number from Silder
number = st.number_input('Select a Number', 0 , 100, 50)
if number:
    st.write(f'Select Number is, {number}')

if st.button('Greet'):
    st.write('Greeting from Streamlit')

    