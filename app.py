import streamlit as st

st.title("Hello Streamlit in VC Code!")
st.write("This is a basic Streamlit app")
st.write("Edit the code and see the changes live!")
st.button("Click Me!")

# --- Interactive examples ---
st.markdown("---")

st.header("Try a text input")
name = st.text_input("Enter your name:")
if name:
	st.write(f"Hello, {name}! 👋")

st.header("Counter example")
if 'count' not in st.session_state:
	st.session_state.count = 0

def increment():
	st.session_state.count += 1

st.write(f"Current count: {st.session_state.count}")
st.button("Increment", on_click=increment)
