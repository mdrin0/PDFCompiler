import os
import pandas as pd
from fillpdf import fillpdfs
import streamlit as st

# Percorso della cartella Downloads
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")


# Funzione per identificare i campi compilabili nel PDF
def get_pdf_fields(pdf_path):
    return fillpdfs.get_form_fields(pdf_path)


# Funzione per compilare i PDF
def compile_pdfs(pdf_path, excel_data, field_mapping, file_naming_columns, output_folder):
    for i, row in excel_data.iterrows():
        form_data = {}

        # Mappa i dati di ogni riga dell'Excel nei campi del PDF
        for pdf_field, excel_col in field_mapping.items():
            if excel_col in row:
                form_data[pdf_field] = row[excel_col]

        # Nome del file basato sulle colonne selezionate
        file_name_parts = [str(row[col]) for col in file_naming_columns]
        filename = "_".join(file_name_parts) + ".pdf"
        output_path = os.path.join(output_folder, filename)

        # Compila il PDF
        fillpdfs.write_fillable_pdf(pdf_path, output_path, form_data)
        print(f"Creato PDF: {output_path}")


# Streamlit App
st.title("PDF Compiler by Rino")
st.markdown("""
## Come utilizzare l'app
1. **Carica un PDF**: Carica un file PDF compilabile contenente i campi da riempire.
2. **Carica un file excel**: Assicurati che il file contenga i dati da inserire nel PDF.
3. **Mappa i campi**: Collega i campi del PDF alle colonne dell'Excel.
4. **Scegli il nome dei File**: Seleziona i campi dell'Excel per generare i nomi dei PDF.
5. **Compila i PDF**: Premi il pulsante per generare i PDF e salvarli nella tua cartella Downloads.
""")

# Step 1: Caricamento dei file
st.header("Carica i file")
uploaded_pdf = st.file_uploader("Carica un file PDF compilabile", type=["pdf"])
uploaded_excel = st.file_uploader("Carica un file Excel", type=["xlsx"])

if uploaded_pdf and uploaded_excel:
    # Salva il PDF temporaneamente
    pdf_path = os.path.join(downloads_folder, "uploaded_template.pdf")
    with open(pdf_path, "wb") as f:
        f.write(uploaded_pdf.read())

    # Leggi i dati dal file Excel
    excel_data = pd.read_excel(uploaded_excel)

    # Identifica i campi del PDF
    st.header("Identifica i campi del PDF")
    pdf_fields = get_pdf_fields(pdf_path)
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
    file_naming_columns = st.multiselect("Seleziona i campi Excel da usare per nominare i file:",
                                         list(excel_data.columns))

    # Compilazione PDF
    if st.button("Compila PDF"):
        compile_pdfs(pdf_path, excel_data, field_mapping, file_naming_columns, downloads_folder)
        st.success(f"PDF compilati e salvati in: {downloads_folder}")



