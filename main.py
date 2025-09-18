from pyscript import document
from pyscript import Element

def generate_message():
    name = document.getElementById("name_input").value
    age = document.getElementById("age_input").value
    school = document.getElementById("school_input").value
    Element("student_profile_name").write(f"Name: {name}")
    Element("student_profile_age").write(f"Age: {age}")
    Element("student_profile_school").write(f"School: {school}")

    notes_1 = """
    {name_input} is currently {age_input} years old and studies in {school_input}
    This information was gathered through input fields and displayed using
    a multiline string in Python via PyScript
    """
    document.getElementById("notes").write(notes_1)