import streamlit as st 
import pandas as pd
import eland as ed
import numpy as np
from client import get_client

def main():
	"""Deploying Streamlit App In Docker"""

	st.title("Streamlit App")
	st.header("Deploying Streamlit in Docker")


	activities = ["EDA","Plots"]

	choice = st.sidebar.selectbox('Select Activities',activities)

	if choice == 'EDA':
		st.subheader("EDA")
		st.text("Hello world!")
		es = get_client()
		df = ed.DataFrame(es, "uzleuven_mir*").to_pandas() 
		st.bar_chart(df)

	elif choice == 'Plots':
		st.subheader("Visualization")
		st.text("There are no plots here")


if __name__ == '__main__':
	main()