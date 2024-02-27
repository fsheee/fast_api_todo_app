import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("Todo App")

def create_todo():
    st.header("Create Todo")
    title = st.text_input("Enter Todo Title")
    description = st.text_area("Enter Todo Description")
    if st.button("Add Todo"):
        response = requests.post(f"{BASE_URL}/todos/", json={"title": title, "description": description})
        if response.status_code == 200:
            st.success("Todo added successfully")

def update_todo():
    st.header("Update  Todo")
    todo_id = st.number_input("Enter Todo ID to update")
    title = st.text_input("Enter Todo Title", key="update_title")
    description = st.text_area("Enter Todo Description", key="update_description")
    
    if st.button("Update Todo"):
        response = requests.put(f"{BASE_URL}/todos/{todo_id}", json={"title": title, "description": description})
        
        if response.status_code == 200:
            st.success("Todo updated successfully")
            st.experimental_rerun()  # Force a rerun to update the display
        else:
            st.error("Failed to update todo. Please try again!")



    
def list_todo():
    st.header("List of Todos")
    
    # State variable to track visibility of todo list
    show_todo_list = st.button("Hide Todo List")
    
    # Fetch Todos button
    if st.button("Todo List") and not show_todo_list:
        response = requests.get(f"{BASE_URL}/todos")
        if response.status_code == 200:
            todos = response.json()
            if todos:
                for todo in todos:
                    st.write(f"ID: {todo['id']}, Title: {todo['title']}, Description: {todo['description']}")
            else:
                st.write("No todos found.")
        else:
            st.error("Failed to fetch todos. Please try again!")
    
def delete_todo():
    st.header("Delete  Todo")
    todo_id = st.number_input("Enter Todo ID to delete")
    if st.button("Delete Todo"):
        response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
        if response.status_code == 200:
            st.success("Todo deleted successfully")


if __name__ == "__main__":
    create_todo()
    update_todo()
    list_todo()
    delete_todo()
