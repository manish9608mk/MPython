import streamlit as st

# DISPLAY ELEMENTS
st.title("title: Fruits app")
st.header("major section")
st.subheader("Smaller section")
st.caption("Small supporting text like: Powered by fruits")

st.write("Hello, choose display elements")

# for drop down 
fruits = st.selectbox("choose your favourite fruits.",['Mango', 'Apple', 'Banana', 'Orange'])

st.write(f'You choose {fruits}. Excellent choice')

# MESSAGE
st.success("successfully choosing fruits.")

