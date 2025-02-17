import streamlit as st

st.title('🎈 Dash')

st.write('Новый Дэш')

df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")

with st.expamder('Data'):
  st.write()
  X_raw = df.drop('Specoes', axis = 1)
  st.dataFrame(X_raw)

  st.write('y')
  y_raw = df.species
  st.dataframe(y_raw)
