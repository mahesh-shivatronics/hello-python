import streamlit as st

st.title("GUI Calculator")

a = st.number_input("Enter First Number")
b = st.number_input("Enter Second Number")

operation = st.selectbox(
    "Select Operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

if st.button("Calculate"):

    if operation == "Addition":
        result = a + b

    elif operation == "Subtraction":
        result = a - b

    elif operation == "Multiplication":
        result = a * b

    elif operation == "Division":
        if b != 0:
            result = a / b
        else:
            result = "Cannot divide by zero"

    st.success(f"Result: {result}")
