import streamlit as st

st.session_state.tasks = []

st.title("See on TodoList ")

def add_task():
    task = st.session_state.new_task
    if task:
        st.session_state.tasks.append(task)
        st.session_state.new_task = ""


def show_tasks():
    if not st.session_state.tasks:
        st.info("Nimekiri on tühi")
        return
    
    for index, task in enumerate(st.session_state.tasks):
        cols = st.columns([0.08, 0.80, 0.11])
        with cols[0]:
            task["done"] = st.checkbox("", value=task["done"], key=f"done_{index}")
        with cols[1]:
            if task["done"]:
                text = f"~~{task['text']}~~"
            else:
                text = task["text"]
        with cols[2]:
            if st.button("Kustuta", key=f"delete_{index}"):
                st.session_state.tasks.pop(index)
                st.rerun()