import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout="wide")
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("يارب المطوع  يطلع الكلب ")
st.subheader("قربت طلعته ان شاء الله")
st.write("ادعوا <b>على المطوع<b/>  الكلب  ",
         unsafe_allow_html=True)

st.text_input(label="", placeholder="اضف دعوه تأجر عليها...", on_change=add_todo, key='new_todo')


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    

    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

