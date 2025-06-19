import streamlit as st
import os

st.title("Deep ML Practice Problems Explorer")

# Set the root directory for problems (adjust if needed)
PROBLEM_ROOT = os.path.dirname(os.path.abspath(__file__))

def find_problem_files(root):
    py_files = []
    for dirpath, dirnames, filenames in os.walk(root):
        for fname in filenames:
            if fname.endswith(".py") and fname != "app.py":
                rel_path = os.path.relpath(os.path.join(dirpath, fname), root)
                py_files.append(rel_path)
    return sorted(py_files)

problem_files = find_problem_files(PROBLEM_ROOT)

st.sidebar.header("Select a Problem File")
selected_file = st.sidebar.selectbox("Python files:", problem_files)

if selected_file:
    st.subheader(f"Viewing: `{selected_file}`")
    file_path = os.path.join(PROBLEM_ROOT, selected_file)
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()
    st.code(code, language="python")

st.sidebar.markdown("---")
st.sidebar.info("Add new `.py` files to your repo and they will appear here automatically.")
