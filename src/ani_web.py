# ani_web.py – HTML/JS generator met typanimatie
# ----------------------------------------------
# Dit script maakt van sample.json een interactieve HTML-pagina

import json
import re
from pathlib import Path

def generate_typing_html(frames, output_path):
    html_head = """<!DOCTYPE html>
<html lang=\"nl\">
<head>
<meta charset=\"UTF-8\">
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
<title>AniFunny Web</title>
<style>
    body { font-family: 'Courier New', monospace; background: #111; color: #fff; padding: 2rem; }
    .frame { display: none; white-space: pre-wrap; font-size: 1.1rem; line-height: 1.5; }
    .active { display: block; }
    .speaker { color: #0f0; font-weight: bold; }
    #nextBtn { margin-top: 1rem; padding: 0.5rem 1rem; font-size: 1rem; }
    .cursor { display: inline-block; width: 10px; background: #0f0; animation: blink 1s steps(2, start) infinite; }
    @keyframes blink { 50% { background: transparent; } }
</style>
</head>
<body>
<h1>AniFunny Typanimatie</h1>
<div id=\"output\"></div>
<button id=\"nextBtn\">Volgende</button>
<script>
const frames = [
"""
    html_frames = ",\n".join([f"    {{speaker: '{f['speaker']}', text: `{f['text']}`}}" for f in frames])
    html_script = "]\n\nlet current = -1;\nconst output = document.getElementById(\"output\");\nconst btn = document.getElementById(\"nextBtn\");\n\nfunction typeText(text, speaker, callback) {\n    output.innerHTML = `<div class='speaker'>${speaker}:</div><div id='typed'></div>`;\n    const el = document.getElementById(\"typed\");\n    let i = 0;\n    const interval = setInterval(() => {\n        el.innerHTML = text.slice(0, i) + '<span class=\"cursor\"> </span>';\n        i++;\n        if (i > text.length) {\n            clearInterval(interval);\n            el.innerHTML = text;\n            callback();\n        }\n    }, 25);\n}\n\nfunction showNext() {\n    current++;\n    if (current >= frames.length) {\n        output.innerHTML = '<em>Einde</em>';\n        btn.disabled = true;\n        return;\n    }\n    const f = frames[current];\n    typeText(f.text, f.speaker, () => {});\n}\n\nbtn.addEventListener(\"click\", showNext);\n</script>\n</body>\n</html>"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_head + html_frames + html_script)

def convert_whatsapp_to_markdown(input_path, output_path):
    pattern = re.compile(r"^(\d{2}-\d{2}-\d{4} \d{2}:\d{2}) - (.*?): (.*)$")
    lines = Path(input_path).read_text(encoding="utf-8").splitlines()
    with open(output_path, "w", encoding="utf-8") as out:
        for line in lines:
            match = pattern.match(line)
            if match:
                _, speaker, message = match.groups()
                if message not in ["<Media weggelaten>", "null"]:
                    out.write(f"{speaker.strip()}: {message.strip()}\n")

if __name__ == "__main__":
    # Optioneel: WhatsApp-export omzetten naar markdown
    txt_path = Path("examples/sample_whatsapp.txt")
    md_path = Path("examples/sample.md")
    if txt_path.exists():
        convert_whatsapp_to_markdown(txt_path, md_path)
        print("📥 WhatsApp-export geconverteerd naar sample.md")

    # JSON genereren vanuit markdown
    json_path = Path("examples/sample.json")
    html_path = Path("examples/sample.html")
    if json_path.exists():
        frames = json.loads(json_path.read_text(encoding='utf-8'))
        generate_typing_html(frames, html_path)
        print(f"✅ HTML gegenereerd naar {html_path}")
    else:
        print("⚠️ Voorbeeldbestand ontbreekt: examples/sample.json")
