import streamlit as st

st.title('Hola')
st.write('Bella')
select=st.selectbox('Scegli',['Ora','Dopo'])
if select=='Ora':
    st.write('BELLLLLAAA')
