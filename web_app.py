import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo + '\n')
    functions.write_todos(todos)


st.title("My Todo APP")
st.text("This app is to increase your productivity")
for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        functions.write_todos(todos)
        st.experimental_rerun()

st.text_input(label="Enter a todo here", placeholder="Add a Todo: ",
              on_change=add_todo, key='new_todo')


st.session_state