import streamlit as st
from agents import analyze_pdf_agent, generate_syllabus_agent, translate_agent, pdf_export_agent
from utils import save_uploaded_file

st.set_page_config(page_title="Generador de Propuesta Didáctica FP", layout="wide")
st.title("📘 Generador de Propuesta Didáctica - FP")
st.write("¡App cargada correctamente!")

# 1) Subida del archivo PDF
pdf_file = st.file_uploader("📤 Sube el archivo PDF con módulos", type="pdf")

if pdf_file:
    save_uploaded_file(pdf_file, "pdfs/modules.pdf")

    try:
        modules = analyze_pdf_agent("pdfs/modules.pdf")
       #st.write("📋 Módulos detectados:", modules)
    except Exception as e:
        st.error(f"❌ Error al analizar el PDF: {e}")
        st.stop()

    selected_module = st.selectbox("📚 Selecciona un módulo", modules)

    prompt = st.text_area("✏️ Introduce la estructura del prompt", height=300)

    if st.button("🧠 Generar Propuesta Didáctica"):
        if prompt and selected_module:
            try:
                st.write("⏳ Generando propuesta didáctica...")

                syllabus_es = generate_syllabus_agent(selected_module, prompt)
                st.write("✅ Propuesta en español generada correctamente.")
                st.markdown(syllabus_es)

                syllabus_eu = translate_agent(syllabus_es)
                st.write("✅ Traducción al euskera completada.")
                st.markdown(syllabus_eu)

                pdf_export_agent(syllabus_es, syllabus_eu)
                st.success("✅ Propuesta generada con éxito.")

                with open("outputs/syllabus_es.pdf", "rb") as f_es:
                    st.download_button("📄 Descargar en Español", f_es, "syllabus_es.pdf")

                with open("outputs/syllabus_eu.pdf", "rb") as f_eu:
                    st.download_button("📄 Descargar en Euskera", f_eu, "syllabus_eu.pdf")

            except Exception as e:
                st.error(f"❌ Error durante la generación: {e}")
        else:
            st.error("❗ Asegúrate de rellenar todos los campos.")
