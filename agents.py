import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from utils import create_pdf
import openai
from PyPDF2 import PdfReader

# Cargar variables desde .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Agente que analiza el PDF (usa función externa)
def analyze_pdf_agent(path):
    reader = PdfReader(path)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() + "\n"

    agent = Agent(
        role="Analista PDF",
        goal="Extraer la lista de módulos del texto de un PDF",
        backstory="Experto en análisis de documentos PDF."
    )

    task = Task(
        description=(
            "A partir del siguiente contenido extraído de un PDF, "
            "extrae únicamente los nombres de los módulos que aparecen:\n\n"
            f"{full_text}"
        ),
        expected_output="Lista clara y ordenada de los módulos detectados",
        agent=agent
    )

    crew = Crew(agents=[agent], tasks=[task])
    result = crew.kickoff()
    return [line.strip() for line in str(result).split("\n") if line.strip()]

# Agente que genera la propuesta didáctica
def generate_syllabus_agent(module, prompt):
    agent = Agent(
        role="Diseñador Didáctico",
        goal="Crear propuesta didáctica del módulo",
        backstory="Experto en pedagogía FP."
    )

    task = Task(
        description=f"Genera la propuesta para el módulo: {module}\nEstructura:\n{prompt}",
        expected_output="Texto en español",
        agent=agent
    )

    crew = Crew(agents=[agent], tasks=[task])
    result = crew.kickoff()
    return str(result)

# Agente que traduce al euskera
def translate_agent(text):
    agent = Agent(
        role="Traductor Euskera",
        goal="Traducir al euskera",
        backstory="Traductor experto de español a euskera."
    )

    task = Task(
        description=f"Traduce el siguiente texto al euskera:\n{text}",
        expected_output="Texto en euskera",
        agent=agent
    )

    crew = Crew(agents=[agent], tasks=[task])
    result = crew.kickoff()
    return str(result)

# Exporta ambos PDFs
def pdf_export_agent(text_es, text_eu):
    create_pdf(text_es, "outputs/syllabus_es.pdf")
    create_pdf(text_eu, "outputs/syllabus_eu.pdf")
