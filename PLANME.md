## 🌟 **OVERZICHT: De 3 Lagen van AniFunny**

### 🧠 **1. De *Kernmotor* – het hoofdprogramma**

*Doet precies wat jij beschrijft:*

* Input = lange tekst
* Output =

  * 📹 Een .mp4-bestand (YouTube-ready)
  * 🌐 Een interactieve HTML-pagina met:

    * tekstblok-animatie
    * "volgende"-knop
    * cookie-opslag
    * gebruikersvoortgang-bewaking
    * melding bij voortijdig verlaten
* Géén GUI nodig, gewoon als Python-script uitvoerbaar
* Duidelijke structuur, **leesbaar zonder commentaar**

### 🧩 **2. De *Interface-module* – GUI voor makers**

*Bouwt bovenop de kernmotor:*

* Gebruiker typt of plakt tekst
* Selecteert:

  * presentatievorm (WhatsApp / boek / grafisch)
  * geluidsopties (spraak, muziek, rap etc.)
  * animatiestijl
* Preview direct zichtbaar
* Klik op "exporteer" → maakt automatisch YouTube-versie + HTML-versie
* Zonder kennis van programmeren

### 🎥 **3. De *Visuele leerlaag* – geanimeerde educatie**

*Een animatie óver het programma zelf:*

* Legt stap voor stap uit:

  * hoe de kernmotor werkt
  * hoe GUI functies aanroept
  * hoe animatie-blokken uit tekst worden gegenereerd
* Toont code én interface synchroon
* Speciaal bedoeld voor jonge developers
* Extra leerfeature: "klik hier om deze code live aan te passen en te testen"

---

## 🚀 **AANPAK VAN DE BOUW**

Laten we beginnen met **laag 1: het kernscript**, zoals je voorstelt. Dan werken we in deze volgorde:

### 🔹 **Fase A.** Prototype bouwen dat:

1. Tekst verdeelt in leesbare blokken (framegrootte: 640x360)
2. Elke blok *letter voor letter* animerend toont
3. Bij vol scherm: speelt een geluid + toont flits
4. Bouwt een mp4-video op basis van deze animatie
5. Bouwt daarnaast een HTML/JS/CSS pagina met:

   * zelfde animatie
   * "volgende"-knop
   * cookie-opslag van voortgang

➡️ Daarna bouwen we een simpele GUI eromheen (laag 2)
➡️ En tot slot de leer-animatie (laag 3)


* flits/sound bij framewissel
* renderen als video en HTML?

Of wil je eerst de structuur van de `.txt`-input of de eerste testtekst samen bepalen? Jij leidt, ik volg ✨🧑‍💻
