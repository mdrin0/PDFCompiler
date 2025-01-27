import os
import pandas as pd
from fillpdf import fillpdfs
import streamlit as st
import tempfile
import zipfile

st.title("PDF Compiler App")

# Istruzioni
st.markdown("""
## Come Utilizzare l'App
1. **Carica un PDF**: Carica un file PDF compilabile contenente i campi da riempire.
2. **Carica un File Excel**: Assicurati che il file contenga i dati da inserire nel PDF.
3. **Mappa i Campi**: Collega i campi del PDF alle colonne dell'Excel.
4. **Scegli il Nome dei File**: Seleziona i campi dell'Excel per generare i nomi dei PDF.
5. **Compila i PDF e Scarica l'Archivio**: Premi il pulsante per generare i PDF e scaricarli.
""")

# Caricamento dei file
uploaded_pdf = st.file_uploader("Carica un file PDF compilabile", type=["pdf"])
uploaded_excel = st.file_uploader("Carica un file Excel", type=["xlsx"])

if uploaded_pdf and uploaded_excel:
    # Salva il PDF in un file temporaneo
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        pdf_path = temp_pdf.name
        temp_pdf.write(uploaded_pdf.read())

    # Leggi i dati dal file Excel
    try:
        excel_data = pd.read_excel(uploaded_excel)
    except Exception as e:
        st.error(f"Errore durante la lettura del file Excel: {e}")
        st.stop()

    # Identifica i campi del PDF
    st.header("Identifica i campi del PDF")
    pdf_fields = fillpdfs.get_form_fields(pdf_path)
    st.write("Campi trovati nel PDF:")
    st.json(pdf_fields)

    # Mappa i campi PDF -> colonne Excel
    st.header("Mappa i campi PDF alle colonne Excel")
    field_mapping = {}
    for pdf_field in pdf_fields.keys():
        selected_column = st.selectbox(f"Mappa per il campo PDF: {pdf_field}", [""] + list(excel_data.columns))
        if selected_column:
            field_mapping[pdf_field] = selected_column

    # Scegli i campi per nominare i file
    st.header("Scegli i campi per nominare i file")
    file_naming_columns = st.multiselect("Seleziona i campi Excel da usare per nominare i file:", list(excel_data.columns))

    # Compilazione PDF
    if st.button("Compila PDF e Scarica"):
        # Crea una cartella temporanea per i PDF compilati
        with tempfile.TemporaryDirectory() as temp_dir:
            try:
                zip_filename = os.path.join(temp_dir, "PDF_Compilati.zip")
                with zipfile.ZipFile(zip_filename, "w") as zipf:
                    for i, row in excel_data.iterrows():
                        form_data = {pdf_field: row[excel_col] for pdf_field, excel_col in field_mapping.items()}
                        filename = "_".join([str(row[col]) for col in file_naming_columns]) + ".pdf"
                        output_path = os.path.join(temp_dir, filename)
                        fillpdfs.write_fillable_pdf(pdf_path, output_path, form_data)
                        zipf.write(output_path, arcname=filename)
                
                # Leggi il file ZIP per il download
                with open(zip_filename, "rb") as f:
                    zip_data = f.read()

                # Pulsante per il download
                st.success("PDF generati con successo!")
                st.download_button(
                    label="Scarica Archivio ZIP",
                    data=zip_data,
                    file_name="PDF_Compilati.zip",
                    mime="application/zip"
                )

            except Exception as e:
                st.error(f"Errore durante la generazione dei PDF: {e}")




