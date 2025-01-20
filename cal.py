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


st.markdown("""
    <h1 style="font-size: 8px; font-weight: bold; color: #335c81;">Hello, I am Ashok , welcome in my Advance Calculator</h1>
""", unsafe_allow_html=True)

class Calculator:
    def __init__(self):
        self.expression = ""

    def perform_operation(self, a, b, operator):
        """Perform the basic arithmetic operations."""
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

    def calculate(self, expression_input):
        """Process the expression and compute the result."""
        try:
            operators = ['+', '-', '*', '/', '%', '//']
            split_result = [x.strip() for x in re.split(r'[\+\-\*/%\s//]+', expression_input)]
            extracted_operators = [op for op in expression_input if op in operators]

            split_result = [int(x) for x in split_result]

            result = split_result[0]
            
            for i, operator in enumerate(extracted_operators):
                result = self.perform_operation(result, split_result[i + 1], operator)

            return result
        except ValueError as ve:
            return f"Error: {ve}"
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
        except Exception as e:
            return f"An unexpected error occurred: {e}"


class CalculatorUI:
    def __init__(self, calculator):
        self.calculator = calculator
        if "expression" not in st.session_state:
            st.session_state.expression = ""

    def handle_button_click(self, value):
        """Update the expression when a button is clicked."""
        if value == "C":
            st.session_state.expression = ""
        else:
            st.session_state.expression += str(value)

    def display_calculator_buttons(self):
        """Display calculator buttons on the Streamlit interface."""
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
                        self.handle_button_click(button)

    def display_result(self):
        """Display the result of the calculation."""
        expression_input = st.text_input("Enter the expression:", value=st.session_state.expression, key="expression_input")
        
        if st.button("Calculate"):
            if expression_input:
                result = self.calculator.calculate(expression_input)
                st.write(f"Result of expression: {result}")
            else:
                st.write("Please enter an expression and click the 'Calculate' button.")
                
calculator = Calculator()
calculator_ui = CalculatorUI(calculator)
calculator_ui.display_calculator_buttons()
calculator_ui.display_result()

st.markdown(
    """
    <style>
    .button-container {
        display: flex;
        justify-content: center;
        position: fixed;
        bottom: 20px;
        width: 100%;
    }
    .button-container a {
        font-size: 18px;
        padding: 10px 20px;
        background-color: #4CAF50;
        color: white;
        text-align: center;
        border-radius: 5px;
        text-decoration: none;
    }
    .button-container a:hover {
        background-color: #45a049;
    }
    </style>
    <div class="button-container">
        <a href="https://ashok-prajapati2.github.io/Portfolio/" target="_blank">About Me</a>
    </div>
    """,
    unsafe_allow_html=True,
)
