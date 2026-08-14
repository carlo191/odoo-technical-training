# Odoo Technical Training — Percorso di Pratica

Repository personale di esercizi svolti seguendo il corso ufficiale **[Odoo Technical Training - Introduction to Development](https://www.odoo.com/slides)**, disponibile su odoo.com/slides.

## 🎯 Obiettivo

Fare pratica di sviluppo di moduli custom su **Odoo 19 Community**, seguendo passo passo gli esercizi del corso ufficiale, per acquisire competenze tecniche reali (ORM, viste, sicurezza, azioni) in un contesto lavorativo che utilizza Odoo.

## 🛠️ Ambiente di sviluppo

- **OS**: Windows con WSL2 (Ubuntu)
- **Odoo**: versione 19.0 (Community Edition)
- **Database**: PostgreSQL 18
- **Editor**: VS Code (con estensione WSL)
- **Python**: 3.14

## 📁 Struttura del repository

```
odoo/                          # Repo ufficiale Odoo (branch 19.0)
├── addons/                    # Moduli core Odoo (non modificare)
├── technical-training/        # I miei esercizi del corso
│   └── estate/                # Modulo custom: Real Estate
│       ├── __init__.py
│       ├── __manifest__.py
│       ├── models/
│       │   ├── __init__.py
│       │   └── estate_property.py
│       ├── security/
│       │   ├── security.xml
│       │   └── ir.model.access.csv
│       ├── views/
│       │   └── estate_property_views.xml
│       └── demo/
│           └── demo.xml
└── setup/
```

## 📚 Progresso nel corso

- [x] Chapter 0-2 — Introduzione, Struttura moduli, Modelli & Campi
- [x] Chapter 3 — Dati demo (`demo.xml`)
- [x] Chapter 4 — Diritti di accesso (`ir.model.access.csv`, gruppo `estate_admin`)
- [x] Chapter 5 — Azioni e Menu (`ir.actions.act_window`, `menuitem`)
- [x] Chapter 6 — Attributi dei campi (readonly, copy, default) e Vista Lista
- [ ] Chapter 7+ — Campi relazionali (in corso)

## 🚀 Come avviare l'ambiente

```bash
cd ~/odoo
python3 odoo-bin --addons-path=addons,technical-training -d mydb -u estate --dev xml
```

Poi apri il browser su [http://localhost:8069](http://localhost:8069).

## 📝 Note

- Il modulo `estate` segue la struttura standard del tutorial ufficiale Odoo (Real Estate module).
- Licenza usata per gli esercizi: `LGPL-3` (Community, per pratica personale — non destinato alla distribuzione commerciale in questa fase).
- Le viste utilizzano il tag `<list>` (non `<tree>`, deprecato a partire da Odoo 18).

## 🔗 Risorse utili

- [Documentazione ufficiale Odoo 19](https://www.odoo.com/documentation/19.0)
- [Corso Technical Training](https://www.odoo.com/slides)
- [Odoo GitHub](https://github.com/odoo/odoo)

---

