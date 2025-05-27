import streamlit as st

st.title("devan deple kece XF")
st.write(
    "devan deple kece XF"
)
st.image("IMG-20250520-WA0020.jpg", width=500)



st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
  st.write(f"{angka} adalah Bilangan Genap")
else:
  st.write(f"{angka} adalah Bilangan Ganjil")
    
