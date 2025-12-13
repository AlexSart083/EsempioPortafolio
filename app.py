import streamlit as st
import pandas as pd

# Configurazione della pagina
st.set_page_config(
    page_title="Portafogli Modello - Esempi di Investimento",
    page_icon="📊",
    layout="wide"
)

# Titolo principale
st.title("📊 Esplora i Nostri Portafogli Modello")

# Introduzione
st.markdown("""
Benvenuto nella sezione dedicata agli **esempi di portafogli d'investimento**. 

Qui troverai esempi di portafogli diversificati costruiti con ETF UCITS, 
suddivisi per profilo di rischio (Basso, Medio, Alto). Questi portafogli sono 
pensati come **spunti didattici** per comprendere come costruire una strategia 
d'investimento bilanciata.

⚠️ **IMPORTANTE**: Queste informazioni sono fornite **a scopo puramente educativo** 
e non costituiscono consulenza finanziaria personalizzata. Prima di investire, 
fai sempre le tue ricerche e, se necessario, consulta un consulente finanziario 
professionale.
""")

st.divider()

# Definizione dei dati degli ETF
def get_portafogli_data():
    """Restituisce i dati strutturati dei portafogli modello"""
    
    portafogli = {
        "basso_rischio": {
            "titolo": "🛡️ Portafogli a Basso Rischio",
            "descrizione": """
            Questi portafogli sono orientati alla **stabilità** e alla **protezione del capitale**, 
            con una minore esposizione al mercato azionario. Ideali per chi ha un orizzonte 
            temporale breve-medio o bassa tolleranza al rischio.
            """,
            "portafogli": [
                {
                    "nome": "Portafoglio Semplificato Basso Rischio (ETF Unico)",
                    "descrizione": """
                    Un ETF multi-asset bilanciato che investe in azioni e obbligazioni globali. 
                    Adatto a chi cerca **massima semplicità** con un rischio contenuto.
                    """,
                    "componenti": [
                        {
                            "nome": "Vanguard LifeStrategy 40% Equity UCITS ETF",
                            "isin": "IE00BMVB5P51",
                            "ter": "0.25%",
                            "tipo_asset": "Multi-Asset Bilanciato",
                            "allocazione": "100%",
                            "descrizione_breve": "Investimento globale con 40% azioni e 60% obbligazioni",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00BMVB5P51"
                        }
                    ]
                },
                {
                    "nome": "Portafoglio Bilanciato Basso Rischio (Multi-ETF)",
                    "descrizione": """
                    Combina una **maggioranza di obbligazioni** con una minoranza di azioni globali 
                    per un buon equilibrio tra crescita e stabilità.
                    """,
                    "componenti": [
                        {
                            "nome": "iShares Core Global Aggregate Bond UCITS ETF",
                            "isin": "IE00B3F81R35",
                            "ter": "0.10%",
                            "tipo_asset": "Obbligazionario Globale",
                            "allocazione": "65%",
                            "descrizione_breve": "Obbligazioni governative e corporate globali investment grade",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00B3F81R35"
                        },
                        {
                            "nome": "iShares Core MSCI World UCITS ETF",
                            "isin": "IE00B4L5Y983",
                            "ter": "0.20%",
                            "tipo_asset": "Azionario Globale",
                            "allocazione": "35%",
                            "descrizione_breve": "Azioni dei paesi sviluppati di tutto il mondo",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00B4L5Y983"
                        }
                    ]
                }
            ]
        },
        "medio_rischio": {
            "titolo": "⚖️ Portafogli a Medio Rischio",
            "descrizione": """
            Questi portafogli cercano un **equilibrio tra crescita del capitale e moderazione del rischio**. 
            Adatti a chi ha un orizzonte temporale medio-lungo e accetta una moderata volatilità 
            per ottenere rendimenti potenzialmente più elevati.
            """,
            "portafogli": [
                {
                    "nome": "Portafoglio Semplificato Medio Rischio (ETF Unico)",
                    "descrizione": """
                    Un ETF multi-asset con una **maggiore esposizione azionaria**, per chi cerca 
                    un buon compromesso tra semplicità e potenziale di rendimento.
                    """,
                    "componenti": [
                        {
                            "nome": "Vanguard LifeStrategy 60% Equity UCITS ETF",
                            "isin": "IE00BMVB5R75",
                            "ter": "0.25%",
                            "tipo_asset": "Multi-Asset Bilanciato",
                            "allocazione": "100%",
                            "descrizione_breve": "Investimento globale con 60% azioni e 40% obbligazioni",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00BMVB5R75"
                        }
                    ]
                },
                {
                    "nome": "Portafoglio Bilanciato Medio Rischio (Multi-ETF)",
                    "descrizione": """
                    Una ripartizione **50/50** tra azioni e obbligazioni per una crescita moderata 
                    nel medio-lungo periodo.
                    """,
                    "componenti": [
                        {
                            "nome": "Vanguard FTSE All-World UCITS ETF",
                            "isin": "IE00BK5BQT80",
                            "ter": "0.22%",
                            "tipo_asset": "Azionario Globale",
                            "allocazione": "50%",
                            "descrizione_breve": "Azioni di paesi sviluppati ed emergenti a livello globale",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00BK5BQT80"
                        },
                        {
                            "nome": "iShares Core Global Aggregate Bond UCITS ETF",
                            "isin": "IE00B3F81R35",
                            "ter": "0.10%",
                            "tipo_asset": "Obbligazionario Globale",
                            "allocazione": "50%",
                            "descrizione_breve": "Obbligazioni governative e corporate globali investment grade",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00B3F81R35"
                        }
                    ]
                }
            ]
        },
        "alto_rischio": {
            "titolo": "🚀 Portafogli ad Alto Rischio",
            "descrizione": """
            Questi portafogli sono orientati alla **massima crescita del capitale** nel lungo periodo, 
            accettando un'alta volatilità. Adatti a chi ha un orizzonte temporale lungo (10+ anni) 
            e alta tolleranza alle fluttuazioni di mercato.
            """,
            "portafogli": [
                {
                    "nome": "Portafoglio Semplificato Alto Rischio (ETF Unico)",
                    "descrizione": """
                    Un ETF **100% azionario globale**, ideale per chi ha un lungo orizzonte temporale 
                    e tolleranza per le fluttuazioni di mercato.
                    """,
                    "componenti": [
                        {
                            "nome": "Vanguard FTSE All-World UCITS ETF",
                            "isin": "IE00BK5BQT80",
                            "ter": "0.22%",
                            "tipo_asset": "Azionario Globale",
                            "allocazione": "100%",
                            "descrizione_breve": "Azioni di paesi sviluppati ed emergenti a livello globale",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00BK5BQT80"
                        }
                    ]
                },
                {
                    "nome": "Portafoglio Azionario Diversificato Alto Rischio (Multi-ETF)",
                    "descrizione": """
                    Un portafoglio **quasi interamente azionario**, diversificato su varie aree 
                    geografiche per massimizzare il potenziale di crescita.
                    """,
                    "componenti": [
                        {
                            "nome": "iShares Core MSCI World UCITS ETF",
                            "isin": "IE00B4L5Y983",
                            "ter": "0.20%",
                            "tipo_asset": "Azionario Paesi Sviluppati",
                            "allocazione": "75%",
                            "descrizione_breve": "Azioni dei paesi sviluppati di tutto il mondo",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00B4L5Y983"
                        },
                        {
                            "nome": "iShares Core MSCI Emerging Markets IMI UCITS ETF",
                            "isin": "IE00BKM4GZ66",
                            "ter": "0.18%",
                            "tipo_asset": "Azionario Mercati Emergenti",
                            "allocazione": "15%",
                            "descrizione_breve": "Azioni di paesi emergenti (large, mid e small cap)",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00BKM4GZ66"
                        },
                        {
                            "nome": "iShares Core Global Aggregate Bond UCITS ETF",
                            "isin": "IE00B3F81R35",
                            "ter": "0.10%",
                            "tipo_asset": "Obbligazionario Globale",
                            "allocazione": "10%",
                            "descrizione_breve": "Obbligazioni globali per minima stabilizzazione",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00B3F81R35"
                        }
                    ]
                }
            ]
        }
    }
    
    return portafogli


def mostra_portafoglio(portafoglio):
    """Visualizza i dettagli di un singolo portafoglio"""
    
    st.markdown(f"**Descrizione:** {portafoglio['descrizione']}")
    
    # Crea DataFrame con i componenti
    componenti_data = []
    for comp in portafoglio['componenti']:
        componenti_data.append({
            "Nome ETF": comp['nome'],
            "ISIN": comp['isin'],
            "TER": comp['ter'],
            "Tipo Asset": comp['tipo_asset'],
            "Allocazione": comp['allocazione'],
            "Descrizione": comp['descrizione_breve']
        })
    
    df = pd.DataFrame(componenti_data)
    
    # Mostra la tabella
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    # Link per maggiori informazioni
    st.markdown("**🔗 Link per approfondimenti:**")
    for comp in portafoglio['componenti']:
        st.markdown(f"- [{comp['nome']}]({comp['link_info']})")
    
    # Calcolo TER medio ponderato (se multi-ETF)
    if len(portafoglio['componenti']) > 1:
        ter_medio = sum(
            float(comp['ter'].replace('%', '')) * float(comp['allocazione'].replace('%', '')) / 100
            for comp in portafoglio['componenti']
        )
        st.info(f"💰 **TER medio ponderato del portafoglio:** {ter_medio:.2f}%")


# Sidebar per navigazione
st.sidebar.title("📋 Navigazione")
st.sidebar.markdown("""
Scegli il profilo di rischio più adatto alle tue esigenze:
- **Basso Rischio**: Stabilità e protezione
- **Medio Rischio**: Equilibrio crescita/stabilità  
- **Alto Rischio**: Massima crescita di lungo periodo
""")

profilo_selezionato = st.sidebar.radio(
    "Vai alla sezione:",
    ["Tutti i Portafogli", "Basso Rischio", "Medio Rischio", "Alto Rischio"]
)

# Carica i dati
portafogli_data = get_portafogli_data()

# Funzione per mostrare una categoria di portafogli
def mostra_categoria(categoria_key, categoria_data):
    st.header(categoria_data['titolo'])
    st.markdown(categoria_data['descrizione'])
    
    for i, portafoglio in enumerate(categoria_data['portafogli'], 1):
        with st.expander(f"📁 {portafoglio['nome']}", expanded=(i == 1)):
            mostra_portafoglio(portafoglio)
    
    st.divider()


# Mostra i portafogli in base alla selezione
if profilo_selezionato == "Tutti i Portafogli":
    mostra_categoria("basso_rischio", portafogli_data["basso_rischio"])
    mostra_categoria("medio_rischio", portafogli_data["medio_rischio"])
    mostra_categoria("alto_rischio", portafogli_data["alto_rischio"])
elif profilo_selezionato == "Basso Rischio":
    mostra_categoria("basso_rischio", portafogli_data["basso_rischio"])
elif profilo_selezionato == "Medio Rischio":
    mostra_categoria("medio_rischio", portafogli_data["medio_rischio"])
elif profilo_selezionato == "Alto Rischio":
    mostra_categoria("alto_rischio", portafogli_data["alto_rischio"])


# Disclaimer finale
st.markdown("---")
st.warning("""
### ⚠️ Disclaimer Importante

Queste informazioni sono fornite **esclusivamente a scopo educativo e informativo**. 
I portafogli presentati sono **esempi teorici** e non costituiscono:

- Consulenza finanziaria personalizzata
- Raccomandazioni di investimento
- Garanzie di rendimento futuro

**Prima di investire:**
1. Valuta attentamente la tua situazione finanziaria personale
2. Considera il tuo orizzonte temporale e la tua tolleranza al rischio
3. Fai le tue ricerche approfondite sui prodotti finanziari
4. Consulta un consulente finanziario professionale se necessario

I rendimenti passati non sono indicativi dei rendimenti futuri. Ogni investimento comporta rischi, 
inclusa la possibile perdita del capitale investito.
""")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <small>App creata a scopo didattico • Dati aggiornati al 2024 • 
    Verifica sempre le informazioni più recenti sui siti ufficiali degli emittenti</small>
</div>
""", unsafe_allow_html=True)
