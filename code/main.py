import streamlit as st
import langchain_fuc

# streamlit is used to develop simple application without need of frontend technologies(data scientist call it as POC(Proof of concept) Applications)

st.title("Restaurant Manager")
cuisine=st.sidebar.selectbox("Pick a cuisine",("Indian","mexican","Italian","Arabic","American"))
if cuisine:
    response = langchain_fuc.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")

    for item in menu_items:
        st.write("-",item)