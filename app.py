import streamlit as st 
import pandas as pd
import numpy as np

def main():
	"""Deploying Streamlit App In Docker"""

	st.title("Streamlit App")
	st.header("Deploying Streamlit in Docker")


	activities = ["EDA","Plots"]

	choices = st.sidebar.selectbox('Select Activities',activities)

	if choices == 'EDA':
		st.subheader("EDA")
		st.text("Hello world!")
		st.bar_chart(pd.DataFrame(np.random.normal(size=[10, 3])))

	elif choices == 'Plots':
		st.subheader("Visualization")
		st.text("There are no plots here")


if __name__ == '__main__':
	main()