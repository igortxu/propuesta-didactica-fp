# 📘 Generador de Propuesta Didáctica - Formación Profesional

Esta aplicación web permite generar automáticamente propuestas didácticas para módulos de Formación Profesional. A partir de un documento PDF con módulos, el sistema extrae los nombres, permite seleccionar uno, y genera una propuesta didáctica estructurada, traducida automáticamente al euskera, y exportable en PDF.

---

## 🚀 Características

- 📤 Carga de documentos PDF con módulos de FP.
- 📚 Extracción automática de módulos.
- 🧠 Generación de propuestas didácticas con IA.
- 🌐 Traducción automática al euskera.
- 📄 Exportación de resultados en PDF (español y euskera).
- 🧱 Interfaz sencilla y funcional con Streamlit.

---

## 🛠️ Tecnologías utilizadas

- Python 3.9+
- [Streamlit](https://streamlit.io)
- [CrewAI](https://docs.crewai.com/)
- OpenAI API (GPT)
- fpdf
- PyPDF2

---

## 🔧 Requisitos de instalación

### 1. Clona el repositorio

```bash
git clone https://github.com/tuusuario/generador-propuesta-fp.git
cd generador-propuesta-fp
```

### 2. Crea un entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configura la clave de OpenAI

Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```env
OPENAI_API_KEY=tu_clave_secreta
```

---

## ▶️ Cómo usar la aplicación

Ejecuta el servidor local de Streamlit:

```bash
streamlit run main.py
```

1. Sube un archivo PDF que contenga una lista de módulos.
2. Selecciona el módulo deseado.
3. Introduce la estructura o el prompt para generar la propuesta.
4. Haz clic en **"Generar Propuesta Didáctica"**.
5. Descarga los archivos generados en PDF (español y euskera).

---

## 📁 Estructura del proyecto

```
generador-propuesta-fp/
│
├── main.py                 # Aplicación principal Streamlit
├── agents.py               # Lógica de agentes IA CrewAI
├── utils.py                # Utilidades (PDF, extracción, guardado)
├── requirements.txt        # Dependencias del proyecto
├── .env                    # Clave API de OpenAI (ignorado en Git)
├── .gitignore              # Archivos y carpetas excluidas
├── outputs/                # Carpeta para PDFs generados
└── pdfs/                   # Carpeta para PDFs subidos
```

---

## 📦 Despliegue

Este proyecto puede desplegarse en [Streamlit Cloud](https://streamlit.io/cloud) fácilmente:

1. Sube el proyecto a GitHub.
2. Ve a Streamlit Cloud y enlaza el repositorio.
3. Establece `main.py` como archivo principal.
4. Añade tu variable `OPENAI_API_KEY` en la configuración.

---

## ✍️ Licencia

MIT License.

---

## 🤝 Contribuciones

¿Quieres colaborar? ¡Las pull requests son bienvenidas!

---

## 📬 Contacto

Desarrollado por igortxu.  
Para dudas o sugerencias, abre una issue o escribe a [igortxu@gmail.com].
