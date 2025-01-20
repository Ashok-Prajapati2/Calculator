import streamlit as st
import re

st.markdown("""
    <style>
        .stApp {    
            background-color: #ffffff;
            background-image: linear-gradient(315deg, #ffffff 0%, #335c81 74%);
        }
    </style>
""", unsafe_allow_html=True)

st.title("Calculator")

def perform_operation(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            raise ValueError('Error (division by zero)')
        return a / b
    elif operator == '%':
        return a % b
    elif operator == '//':
        return a // b

if "expression" not in st.session_state:
    st.session_state.expression = ""

def handle_button_click(value):
    if value == "C":
        st.session_state.expression = ""
    else:
        st.session_state.expression += str(value)

cols = st.columns(3)
col_list = [
    [7, 8, 9], 
    [4, 5, 6],  
    [1, 2, 3],  
    [0, "+", '-'],  
    ['*', '/', 'C'],  
    ['H', 'U', 'R']  
]

for row in col_list:
    for i, button in enumerate(row):
        with cols[i]:
            if st.button(str(button)):
                handle_button_click(button)

expression_input = st.text_input("Enter the expression:", value=st.session_state.expression, key="expression_input")

if st.button("Calculate"):
    if expression_input:
        try:
            operators = ['+', '-', '*', '/', '%', '//']

            split_result = [x.strip() for x in re.split(r'[\+\-\*/%\s//]+', expression_input)] 
            extracted_operators = [op for op in expression_input if op in operators]

            split_result = [int(x) for x in split_result]

            result = split_result[0]
            
            for i, operator in enumerate(extracted_operators):
                result = perform_operation(result, split_result[i + 1], operator)

            st.write(f"Result of expression: {result}")
        
        except ValueError as ve:
            st.write(f"Error: {ve}")
        except ZeroDivisionError:
            st.write("Error: Division by zero is not allowed.")
        except Exception as e:
            st.write(f"An unexpected error occurred: {e}")

    else:
        st.write("Please enter an expression and click the 'Calculate' button.")
