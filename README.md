# PDF Compiler

**PDF Compiler** è un'applicazione progettata per automatizzare la compilazione di PDF a partire da dati presenti in un file Excel.

## Origine dell'idea
Il progetto è nato per risolvere un problema reale affrontato dal team di marketing durante l'organizzazione di eventi. La preparazione di badge nominali per i partecipanti era un processo completamente manuale, che richiedeva di copiare e incollare i dati (nome, cognome, azienda) da un file Excel a un PDF per ciascun partecipante. Questo metodo era dispendioso in termini di tempo e soggetto a errori.

**PDF Compiler** è stata sviluppata per eliminare questa inefficienza, consentendo di generare automaticamente badge compilati per n partecipanti con un singolo clic.

## Cosa fa
L'app consente di:
- Automatizzare la compilazione dei PDF: i dati vengono estratti automaticamente da un file Excel e inseriti nei campi del PDF.
- Gestire grandi quantità di documenti: che si tratti di 10 o 1.000 partecipanti, l'app genera rapidamente tutti i PDF necessari.
- Adattarsi a ogni contesto: sebbene progettata inizialmente per badge nominali, l'app può essere utilizzata per compilare qualsiasi tipo di PDF con campi compilabili, come contratti, moduli personalizzati o documenti aziendali.

## Perché usarla
**PDF Compiler** elimina il lavoro manuale, aumentando la produttività e riducendo il rischio di errori. È ideale per:
- Eventi aziendali e conferenze: genera badge nominali per i partecipanti.
- Automazione di documenti amministrativi: compila contratti e moduli in modo rapido e preciso.
- Qualsiasi scenario: dove è necessario inserire dati in PDF in modo automatico.

## Come funziona
1. **Carica un PDF**: l'utente carica un PDF compilabile con i campi che devono essere riempiti.
2. **Carica un file Excel**: un file Excel con i dati da inserire, organizzati in colonne (es. nome, cognome, azienda).
3. **Mappa i campi**: tramite un'interfaccia intuitiva, l'utente associa i campi del PDF alle colonne dell'Excel.
4. **Genera i PDF**: con un singolo clic, vengono generati tutti i PDF compilati.
5. **Scarica i PDF**: i documenti vengono compressi in un archivio ZIP, pronto per essere scaricato.

## Punti di forza
1. Scalabilità: ideale per eventi piccoli o grandi con migliaia di partecipanti.
2. Precisione: riduce al minimo gli errori manuali.
3. Flessibilità: utilizzabile in vari contesti, non solo per badge.

## Tecnologie utilizzate
- Python
- Streamlit: per l'interfaccia web
- fillpdf: per la compilazione dei PDF
- openpyxl: per la lettura dei file Excel

## Come eseguire localmente
1. Clona il repository:
   ```bash
   git clone https://github.com/<tuo-username>/PDFCompiler.git
