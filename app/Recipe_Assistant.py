import streamlit as st
from streamlit_multipage import MultiPage
import os
from utils import *

st.set_page_config(
    page_title="Ask Ajji",
    page_icon=":curry:",
    layout="wide",
    initial_sidebar_state="expanded",
    )
def main():
    app = MultiPage()
    st.sidebar.title('Ask Ajji!')
    st.sidebar.image("app/recipeAjji.jpeg", use_column_width=True)
    with st.sidebar:
        st.markdown('Welcome to ask Ajji! Ask Ajji is a friendly assistant that can help you with your cooking queries. You can ask Ajji for recipes on your favourite Indian dishes and she help you with the best possible answer.')
    
    st.subheader("Ask  Ajji for a recipe...")    
    with st.expander("Recipe Assistant", expanded=True):
        app_input= get_input()
        recipe_submit_button = st.button(label="Click for recipe!")
        with st.spinner("Finding recipes...."):
            if recipe_submit_button and app_input:
                recipes= get_recipesforinput(app_input)
                st.subheader("Recipe:")
                st.image("app/chefgrandmom.jpeg", width=500)                  
                st.write(recipes)



def get_input():
    input_text = st.text_area(
        label="Give me the recipe for?",
        placeholder="What would you like to cook?",
        height=100,
        key="app_input",
        help="Please enter the name of the dish which you would like to cook and I will give you the recipe",
    )
    return input_text

if __name__ == "__main__":
    main()