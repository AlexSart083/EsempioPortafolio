# Portafogli Modello - App Streamlit

App Streamlit per esplorare esempi di portafogli d'investimento basati su ETF UCITS, suddivisi per profilo di rischio.

## 🚀 Come eseguire l'app

### Prerequisiti
- Python 3.8 o superiore
- pip (package manager Python)

### Installazione

1. **Clona o scarica il repository**

2. **Installa le dipendenze**
   ```bash
   pip install -r requirements.txt
   ```

3. **Esegui l'app**
   ```bash
   streamlit run portafogli_modello.py
   ```

4. **Apri il browser**
   L'app si aprirà automaticamente nel browser all'indirizzo `http://localhost:8501`

## 📁 Struttura del Progetto

```
.
├── portafogli_modello.py    # File principale dell'app
├── requirements.txt          # Dipendenze Python
└── README.md                 # Questo file
```

## 🌐 Pubblicazione Online

### Streamlit Community Cloud (Gratuito)

1. Carica il progetto su GitHub
2. Vai su [share.streamlit.io](https://share.streamlit.io)
3. Connetti il tuo repository GitHub
4. Seleziona il file `portafogli_modello.py`
5. Deploy!

## ⚠️ Disclaimer

Questa app è fornita esclusivamente a scopo educativo. Non costituisce consulenza finanziaria.
I dati potrebbero non essere aggiornati - verifica sempre le informazioni sui siti ufficiali degli emittenti.

## 📊 Funzionalità

- **3 Profili di Rischio**: Basso, Medio, Alto
- **Portafogli Semplificati**: Con un singolo ETF multi-asset
- **Portafogli Diversificati**: Con multiple componenti
- **Informazioni Dettagliate**: ISIN, TER, allocazioni, link di approfondimento
- **Interfaccia Intuitiva**: Navigazione semplice con sidebar ed expander

## 🛠️ Tecnologie Utilizzate

- **Streamlit**: Framework per app web interattive
- **Pandas**: Manipolazione e visualizzazione dati
- **Python 3**: Linguaggio di programmazione

## 📝 Note

- I portafogli mostrati sono esempi teorici
- I TER (Total Expense Ratio) indicati sono approssimativi
- Verifica sempre i dati più recenti prima di investire
