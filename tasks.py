from pathlib import Path

from invoke import task

REPO_ROOT = Path(__file__).parent


@task
def chat_gpt_clone(c, solution=False):
    """Start the chat GPT clone application. Use the --solution flag to start the solution version."""
    root_folder = "solutions" if solution else "exercises"
    path = (
        REPO_ROOT
        / root_folder
        / "01_basic_concepts"
        / "04_chat_GPT_clone_application"
        / "main.py"
    )
    path = path.resolve().absolute()
    c.run(f"streamlit run {path}")


@task
def house_description_writer(c, solution=False):
    """Start the house description writer application. Use the --solution flag to start the solution version."""
    root_folder = "solutions" if solution else "exercises"
    path = (
        REPO_ROOT
        / root_folder
        / "02_clever_prompting"
        / "03_house_description_writer_application"
        / "main.py"
    )
    path = path.resolve().absolute()
    c.run(f"streamlit run {path}")


@task
def pydata_qa_bot(c, solution=False):
    """Start the PyData QA bot. Use the --solution flag to start the solution version."""
    root_folder = "solutions" if solution else "exercises"
    path = REPO_ROOT / root_folder / "03_RAG" / "04_pydata_qa_bot" / "main.py"
    c.run(f"streamlit run {path}")


@task()
def data_chatbot(c, solution=False):
    """Start the "talk to the data" chatbot application. Use the --solution flag to start the solution version."""
    root_folder = "solutions" if solution else "exercises"
    path = (
        REPO_ROOT / root_folder / "04_agents" / "extras" / "04_data_chatbot" / "main.py"
    )
    c.run(f"streamlit run {path}")


@task
def hackathon(c, solution=False):
    """Starts the hackathon application. Use the --solution flag to start the solution version."""
    root_folder = "solutions" if solution else "exercises"
    path = REPO_ROOT / root_folder / "42_hackathon" / "main.py"
    c.run(f"streamlit run {path}")


@task
def streamlit_demo(c, solution=False, exercise=1):
    """Starts the hackathon application. Use the --solution flag to start the solution version."""
    root_folder = "solutions" if solution else "exercises"
    if exercise == 1:
        file = "1_simple_line_chart.py"
    elif exercise == 2:
        file = "2_line_chat_interaction.py"
    else:
        file = "3_sidebar.py"
    path = REPO_ROOT / "streamlit" / root_folder / file
    c.run(f"streamlit run {path}")


@task()
def generate_exercises(c):
    """Generate the exercise folder based on the solutions folder. Without the answers of course."""
    path = REPO_ROOT / "scripts" / "generate_exercises.py"
    path = path.resolve().absolute()

    input_folder = REPO_ROOT / "solutions"
    input_folder = input_folder.resolve().absolute()

    output_folder = REPO_ROOT / "exercises"
    output_folder = output_folder.resolve().absolute()
    c.run(
        f"python {path} --input_folder {input_folder} --output_folder {output_folder}"
    )


@task()
def generate_exercises_streamlit(c):
    """Generate the exercise folder for the streamlit material based on the solutions folder. Without the answers of course."""
    path = REPO_ROOT / "scripts" / "generate_exercises.py"
    path = path.resolve().absolute()

    input_folder = REPO_ROOT / "streamlit" / "solutions"
    input_folder = input_folder.resolve().absolute()

    output_folder = REPO_ROOT / "streamlit" / "exercises"
    output_folder = output_folder.resolve().absolute()
    c.run(
        f"python {path} --input_folder {input_folder} --output_folder {output_folder}"
    )
