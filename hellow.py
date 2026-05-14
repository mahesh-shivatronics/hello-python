import streamlit as st

st.title("Calculator")

a = st.number_input("First Number")
b = st.number_input("Second Number")

operation = st.selectbox(
    "Choose Operation",
    ["Add", "Subtract", "Multiply", "Divide"]
)

if st.button("Calculate"):

    if operation == "Add":
        result = a + b

    elif operation == "Subtract":
        result = a - b

    elif operation == "Multiply":
        result = a * b

    elif operation == "Divide":
        result = a / b if b != 0 else "Cannot divide by zero"

    st.write("Result:", result)
