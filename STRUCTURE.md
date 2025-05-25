## 📁 STRUCTURE.md – Bestands- en moduleoverzicht AniFunny

### 🔹 Hoofdmappen

* `src/` → Python-code en modules
* `examples/` → Markdownvoorbeelden en gegenereerde JSON/outputs
* `docs/` *(optioneel later)* → Gebruikersdocumentatie, handleidingen

---

### 🔹 Kernbestanden

| Bestand           | Doel                                          |
| ----------------- | --------------------------------------------- |
| `README.md`       | Uitleg voor externe gebruikers en bezoekers   |
| `PLANME.md`       | Projectplan en bouwfases                      |
| `GUIDEME.md`      | Samenwerkings-eed en rolverdeling             |
| `STRUCTURE.md`    | (dit bestand) Overzicht van bestandsstructuur |
| `src/ani_core.py` | Kernscript: .md → JSON frames                 |
| `src/ani_web.py`  | HTML/JS output (klikbare versie)              |
| `src/ani_gui.py`  | GUI voor input/preview/output                 |

---

### 🔹 Voorbeeldmateriaal

| Bestand                | Omschrijving                                   |
| ---------------------- | ---------------------------------------------- |
| `examples/sample.md`   | Voorbeeld markdown met dialoog                 |
| `examples/sample.json` | Door `ani_core.py` gegenereerde framestructuur |

---

### 🔹 Komende toevoegingen

* `src/ani_render.py` → Typanimatie en MP4-export
* `src/utils.py` → Algemene hulpfuncties (kleur, typgeluid, enz.)
* `src/config.py` → Instellingen en templates (stijlen, timing)

---

Deze structuur groeit met ons project mee. Alles wat we bouwen blijft transparant, herbruikbaar, en logisch georganiseerd. ✨
