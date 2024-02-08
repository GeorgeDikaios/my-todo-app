import streamlit as st
import toDo_functions as functions

todos = functions.get_todos()


def add_todo():
    if st.session_state["new_todo"]:
        new_todo = st.session_state["new_todo"] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)



# def complete_todo():

st.title("My Todo Apps")
st.subheader("This is my todo app.")
st.write("This app is to increase you productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter todo", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

st.session_state