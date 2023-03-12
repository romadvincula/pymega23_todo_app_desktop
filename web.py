import streamlit as st
import functions


def add_todo():
    todos = functions.get_todos()
    todo = st.session_state["new_todo"]
    print(todo)
    todos.append(todo + "\n")
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        print(checkbox)
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st._rerun()


st.text_input(label="Add a new todo...", label_visibility="hidden", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")

st.session_state