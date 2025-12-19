# 📝 Guida per Aggiungere Nuovi Portafogli

Questa guida spiega come aggiungere nuovi portafogli al file `AzionarioPort.txt`.

## 📋 Formato Base

Il file è organizzato in 3 sezioni principali:
- **Multi Portfolios**: Portafogli con più ETF
- **Single**: Portafogli con un singolo ETF
- **ESG**: Portafogli ESG (qualsiasi numero di ETF)

## 🔧 Struttura di un Portafoglio

### Header del Portafoglio
```
PORTxx - Risk Y, ESG Z, MinDurY W Rebalance R
```

Dove:
- `PORTxx`: ID univoco del portafoglio (es. PORT2a, PORT15, PORT23a)
- `Y`: Livello di rischio da 1 a 8
- `Z`: Flag ESG (0 = no, 1 = sì)
- `W`: Durata minima in anni (può essere un range come "1..xx" o un numero)
- `R`: Frequenza ribilanciamento (NO, 1y, 3M, ecc.)

### Componenti del Portafoglio

Per **portafogli multi-ETF**:
```
XX% Nome ETF ISIN TER
```

Dove:
- `XX%`: Percentuale di allocazione
- `Nome ETF`: Nome completo dell'ETF
- `ISIN`: Codice ISIN (formato: 2 lettere + numeri/lettere)
- `TER`: Total Expense Ratio in formato decimale (0,12 = 0.12%)

Per **portafogli single ETF**:
```
Nome ETF ISIN TER
```
(senza percentuale, si assume 100%)

## 📝 Esempi Completi

### Esempio 1: Portafoglio Multi-ETF

```
PORT9 - Risk 4, ESG 0, MinDurY 10 Rebalance 1y
40% Vanguard FTSE All-World UCITS ETF (USD) Accumulating IE00BK5BQT80 0,22
30% iShares Core Euro Government Bond UCITS ETF (Acc) IE00B4WXJJ64 0,09
20% iShares Physical Gold ETC IE00B4ND3602 0,12
10% iShares EUR Corporate Bond UCITS ETF (Acc) IE00B3F81R35 0,20
```

### Esempio 2: Portafoglio Single ETF

```
PORT18 - Risk 5, ESG 0, MinDurY 10
Amundi Prime All Country World UCITS IE0003XJA0J9 0,07
```

### Esempio 3: Portafoglio ESG

```
PORT28 - Risk 6, ESG 1, MinDurY 10 Rebalance 1y
70% iShares MSCI World ESG Enhanced CTB UCITS ETF USD (Acc) IE00B8KGV557 0,20
20% Vanguard ESG Developed Europe All Cap UCITS ETF (EUR) Acc IE00BNG8L385 0,12
10% Amundi Index Euro Corporate SRI 0-3 Y UCITS ETF DR (C) LU1437017350 0,12
```

## ⚠️ Regole Importanti

1. **Separazione delle Sezioni**: Lascia una riga vuota tra i portafogli
2. **Formato TER**: Usa la virgola come separatore decimale (0,12 non 0.12)
3. **ISIN Validi**: Assicurati che l'ISIN sia corretto (controllabile su JustETF)
4. **Somma Percentuali**: Per portafogli multi-ETF, la somma deve essere 100%
5. **Collocazione**: 
   - Portafogli con 2+ ETF → sezione "Multi Portfolios"
   - Portafogli con 1 ETF → sezione "Single"
   - Portafogli ESG → sezione "ESG" (indipendentemente dal numero di ETF)

## 🎯 Linee Guida per i Livelli di Rischio

- **Rischio 1-2**: Principalmente obbligazioni, minima esposizione azionaria
- **Rischio 3-4**: Mix bilanciato 40-60% azioni
- **Rischio 5-6**: Prevalenza azionaria 60-80%
- **Rischio 7-8**: 80-100% azioni, strategie aggressive o leverage

## 📊 Suggerimenti per l'Orizzonte Temporale

- **1-3 anni**: Solo obbligazioni a breve, money market
- **3-5 anni**: Rischio basso con obbligazioni prevalenti
- **5-7 anni**: Rischio basso-medio
- **7-10 anni**: Rischio medio
- **10+ anni**: Qualsiasi livello di rischio

## ✅ Checklist Prima di Aggiungere

- [ ] ID portafoglio univoco
- [ ] Livello di rischio appropriato (1-8)
- [ ] Flag ESG corretto
- [ ] Orizzonte temporale realistico
- [ ] ISIN verificati su JustETF
- [ ] TER aggiornati
- [ ] Percentuali sommano a 100% (se multi-ETF)
- [ ] Formato corretto (spazi, virgole)
- [ ] Sezione appropriata (Multi/Single/ESG)

## 🔄 Dopo l'Aggiunta

1. Salva il file `AzionarioPort.txt`
2. Riavvia l'applicazione Streamlit
3. Verifica che il nuovo portafoglio appaia correttamente
4. Controlla TER medio ponderato
5. Testa i link JustETF

## 🐛 Troubleshooting

**Il portafoglio non appare?**
- Controlla il formato dell'header
- Verifica che ci sia una riga vuota tra i portafogli
- Assicurati che l'ISIN sia nel formato corretto

**TER errato?**
- Usa la virgola (,) non il punto (.) come separatore decimale
- Il TER deve essere dopo l'ISIN

**Allocazioni non corrette?**
- Per multi-ETF: percentuale deve iniziare la riga
- Per single ETF: NON includere la percentuale

## 💡 Suggerimenti

1. **Mantieni coerenza**: Segui lo stile degli altri portafogli
2. **Nomi chiari**: Usa nomi ETF completi e ufficiali
3. **Aggiorna TER**: Controlla periodicamente i TER su JustETF
4. **Documenta**: Aggiungi note speciali usando il formato `(nota)` dopo il componente
5. **Testa**: Verifica sempre l'apparenza finale nell'app

## 📚 Risorse Utili

- [JustETF](https://www.justetf.com/it/) - Database ETF europei
- [Morningstar](https://www.morningstar.it/) - Analisi fondi
- [Borsa Italiana](https://www.borsaitaliana.it/) - Quotazioni ETF
- [Quantalys](https://www.quantalys.it/) - Ricerca fondi

---

**Buona aggiunta di portafogli! 🚀**
