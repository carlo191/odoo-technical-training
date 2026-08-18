# 🏠 Odoo Real Estate Module — Progetto di Sviluppo

Repository personale di esercizi svolti seguendo il corso ufficiale **[Odoo Technical Training - Introduction to Development](https://www.odoo.com/slides)**, disponibile su odoo.com/slides.

## 🎯 Obiettivo

Sviluppare un **modulo Odoo personalizzato per la gestione di proprietà immobiliari**, acquisendo competenze tecniche reali in sviluppo Odoo attraverso esercizi pratici su **Odoo 19 Community**. Il percorso copre: modellazione dati, creazione di viste, gestione della sicurezza, azioni personalizzate e inheritance di viste.

## 🛠️ Ambiente di sviluppo

- **OS**: Windows con WSL2 (Ubuntu)
- **Odoo**: versione 19.0 (Community Edition)
- **Database**: PostgreSQL 18
- **Editor**: VS Code (con estensione WSL)
- **Python**: 3.14

## 📁 Struttura del repository

```
technical-training/
└── estate/                           # Modulo custom: Real Estate
    ├── __init__.py                   # Inizializzazione modulo
    ├── __manifest__.py               # Metadati modulo
    ├── models/
    │   ├── __init__.py
    │   ├── estate_property.py        # Modello principale proprietà
    │   ├── estate_property_type.py   # Tipi di proprietà
    │   ├── estate_property_tag.py    # Tag/categorie
    │   ├── estate_property_offer.py  # Offerte ricevute
    │   └── res_users.py              # Estensione modello Users (inheritance)
    ├── security/
    │   ├── security.xml              # Gruppi e diritti
    │   └── ir.model.access.csv       # Permessi per modello
    ├── views/
    │   └── estate_property_views.xml # Viste: search, form, list + inheritance Users
    ├── demo/
    │   └── demo.xml                  # Dati di prova
    └── static/                       # Assets statici (se necessari)
```

## 📚 Progresso nel corso

- [x] **Chapter 0-2** — Introduzione, Struttura moduli, Modelli & Campi
- [x] **Chapter 3** — Dati demo (`demo.xml`)
- [x] **Chapter 4** — Diritti di accesso (`ir.model.access.csv`, gruppo `estate_admin`)
- [x] **Chapter 5** — Azioni e Menu (`ir.actions.act_window`, `menuitem`)
- [x] **Chapter 6** — Attributi dei campi (readonly, copy, default) e Vista Lista
- [x] **Chapter 7-18** — Campi relazionali (Many2one, One2many, Many2many), Campi computati, Onchange
- [x] **Chapter 19** — **View Inheritance** (Aggiunta tab "Proprietà" alla vista Users)

## 🏗️ Modello Dati — Estate Property

### Entità principale: `estate.property`

**Campi principali:**
- `name` (Char) — Titolo della proprietà
- `expected_price` (Float) — Prezzo richiesto
- `selling_price` (Float) — Prezzo di vendita effettivo
- `state` (Selection) — Stato (Nuova → Offerta Ricevuta → Offerta Accettata → Venduta/Annullata)
- `date_availability` (Date) — Data disponibilità
- `postcode`, `living_area`, `bedrooms`, `facades` — Dettagli proprietà
- `garden` (Boolean) — Ha giardino?
- `garden_area`, `garden_orientation` — Dimensioni e orientamento giardino
- `total_area` (Computed) — Area totale (living_area + garden_area)
- `best_price` (Computed) — Migliore offerta ricevuta

### Relazioni:
- **Many2one** `property_type_id` → Tipo di proprietà (villa, appartamento, ecc.)
- **Many2one** `salesperson_id` → Agente commerciale (res.users)
- **Many2one** `buyer_id` → Compratore (res.partner)
- **One2many** `offer_ids` → Offerte ricevute
- **Many2many** `tag_ids` → Categorie/tag

### Azioni personalizzate:
- `azione_venduta()` — Marca proprietà come venduta
- `azione_annullata()` — Annulla la vendita
- `_onchange_garden()` — Automatizza garden_area e orientation
- `_check_delete_state()` — Impedisce eliminazione se in stato intermedio

---

## 👥 Estensione del Modello Users (Chapter 19)

**Nuovo file:** `models/res_users.py`

Estensione della vista `res.users` (modello Users di Odoo) tramite **view inheritance**:
- Aggiunge campo `property_ids` (One2many) per mostrare le proprietà dell'agente
- Crea nuovo tab "Proprietà" nella scheda utente
- Usa XPath per inserire il campo dentro la `<notebook>` esistente

```python
class ResUsers(models.Model):
    _inherit = "res.users"
    property_ids = fields.One2many("estate.property", "salesperson_id")
```

**Vista XML:**
```xml
<record id="base_view_users_form_inherit" model="ir.ui.view">
    <field name="inherit_id" ref="base.view_users_form"/>
    <xpath expr="//notebook" position="inside">
        <page string="Proprietà">
            <field name="property_ids"/>
        </page>
    </xpath>
</record>
```

---

## 🎨 Viste Implementate

### 1. **Vista Search** — Ricerca e filtraggio
- Campi ricercabili: Titolo, Tipo, CAP, Prezzo, Camere, Superficie
- Filtri predefiniti: "Available" (Nuova o Offerta Ricevuta)

### 2. **Vista Form** — Scheda dettaglio proprietà
- Header con statusbar e bottoni azione
- Sezioni organizzate in group
- Notebook con tab "Offerte" (lista offerte ricevute)
- Chatter (thread commenti e attività)

### 3. **Vista List** — Elenco proprietà
- Colonne: Titolo, Tipo, Agente, CAP, Camere, Superficie, Prezzi, Tag
- Widget many2many_tags per visualizzazione tag

### 4. **Vista Users (Inheritance)** — Tab Proprietà
- Mostra elenco proprietà assegnate all'agente
- Aggiunto tramite view inheritance (XPath)

---

## 🚀 Come avviare l'ambiente

### Requisiti:
- PostgreSQL 18+
- Python 3.11+
- Odoo 19.0 Community

### Installazione:
```bash
# Clonare repo Odoo
cd ~
git clone https://github.com/odoo/odoo.git --branch 19.0 --depth 1

# Installare dipendenze
pip install -r odoo/requirements.txt

# Avviare Odoo con il modulo estate
cd odoo
python3 odoo-bin --addons-path=addons,../technical-training \
                  -d estate_db \
                  -u estate \
                  --dev xml \
                  --stop-after-init
```

### Accesso:
- URL: [http://localhost:8069](http://localhost:8069)
- Utente: `admin`
- Password: `admin`

### Per sviluppo continuo (con hot-reload):
```bash
python3 odoo-bin --addons-path=addons,../technical-training \
                  -d estate_db \
                  --dev xml
```

---

## ✨ Funzionalità principali

✅ **Gestione Proprietà**
- Creazione proprietà con dettagli completi
- Stato workflow (Nuova → Offerta → Venduta/Annullata)
- Validazioni (prezzi positivi, stato cancellazione controllato)

✅ **Offerte Immobiliari**
- Ricezione offerte su proprietà
- Calcolo automatico migliore offerta
- Validazione date scadenza

✅ **Integrazione Users**
- Agenti collegati a proprietà
- View inheritance per mostrare proprietà nella scheda agente
- Filtri e ricerche

✅ **Tag e Categorie**
- Classificazione proprietà per colore
- Ricerca per categoria

✅ **Sicurezza**
- Gruppo `estate_admin` con permessi specifici
- Controllo accesso per modello

---

## 🧪 Testing e Debug

Attiva la modalità debug Odoo:
```bash
python3 odoo-bin --addons-path=addons,../technical-training -d estate_db --dev xml
```

Modalità debug attiva:
- Tracciamento SQL
- Hot-reload XML
- Visualizzazione eccezioni dettagliate

---

## 📖 Concetti Odoo imparati

| Concetto | Descrizione |
|----------|-------------|
| **Model** | Classe Python che rappresenta una tabella DB |
| **Fields** | Campi del modello (Char, Float, Many2one, ecc.) |
| **Many2one** | Relazione uno-a-molti (FK) |
| **One2many** | Relazione inversa molti-a-uno |
| **Many2many** | Relazione simmetrica |
| **Computed Fields** | Campi calcolati on-the-fly con `@api.depends` |
| **Onchange** | Logica trigger quando campi cambiano valore |
| **Views** | Form/List/Search in XML |
| **View Inheritance** | Estensione viste esistenti con XPath |
| **Actions** | Bottoni personalizzati e azioni UI |
| **Security** | Gruppi e IR.Model.Access |
| **SQL Constraints** | Vincoli a livello DB |

---

## 📝 Note

- Questo modulo segue la struttura **standard ufficiale Odoo** (Real Estate training module).
- Licenza: **LGPL-3** (Community, pratica personale).
- Viste XML utilizzano tag moderni (`<list>`, non deprecato `<tree>`).
- Fully compatible con **Odoo 19 Community Edition**.

---

## 🔗 Risorse utili

| Risorsa | Link |
|---------|------|
| Documentazione Odoo 19 | https://www.odoo.com/documentation/19.0 |
| Corso Technical Training | https://www.odoo.com/slides |
| Odoo GitHub | https://github.com/odoo/odoo |
| ORM API | https://www.odoo.com/documentation/19.0/developer/reference/orm.html |
| Security | https://www.odoo.com/documentation/19.0/developer/tutorials/server_framework_101/13_security.html |

---

**Autore:** Carlo  
**Data inizio:** 2026  
**Status:** 🔄 In corso (Chapter 19/30+)

