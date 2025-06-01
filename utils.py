import os
import markdown
from weasyprint import HTML

def save_uploaded_file(file, path):
    with open(path, "wb") as f:
        f.write(file.read())

def create_pdf(markdown_text, output_path):
    # Crear carpeta si no existe
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Convertir markdown a HTML con soporte de tablas
    html_body = markdown.markdown(markdown_text, extensions=['tables'])

    # Añadir estilos CSS para las tablas y formato general
    style = """
    <style>
        body {
            font-family: Arial, sans-serif;
            font-size: 12pt;
            margin: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 1em;
        }
        th, td {
            border: 1px solid #333;
            padding: 6px 8px;
            text-align: left;
        }
        th {
            background-color: #eee;
        }
        strong, b {
            font-weight: bold;
        }
    </style>
    """

    html_complete = f"<html><head>{style}</head><body>{html_body}</body></html>"

    # Generar PDF con WeasyPrint
    HTML(string=html_complete).write_pdf(output_path)
