import streamlit as st

# Заголовок приложения
st.title("Проверка анаграмм")

# Поля ввода
text1 = st.text_input("Введите первое слово:")
text2 = st.text_input("Введите второе слово:")

# Функция проверки анаграммы
def isAnagram(s, t):
  ds={}
  dt={}

  for i in s:
    if i in ds:
      ds[i]+=1
    else:
      ds[i]=1

  for i in t:
    if i in dt:
      dt[i]+=1
    else:
      dt[i]=1
  k=0
  for i in dt:
    if i in ds and ds[i]==dt[i]:
      k+=1
    else:
      return False

  if k==len(ds):
    return True
  else:
    return False

# Проверка и вывод результата
if st.button("Проверить"):
    if isAnagram(text1, text2):
        st.success("Это анаграмма!")
    else:
        st.error("Это не анаграмма.")
