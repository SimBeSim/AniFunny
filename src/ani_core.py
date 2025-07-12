from pathlib import Path
import json

def parse_markdown_to_frames(md_text):
    frames = []
    current_speaker = None
    buffer = []

    for line in md_text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("Maxi:") or line.startswith("Samanta:") or line.startswith("Annabelle:") or line.startswith("Ilse:"):
            if buffer:
                frames.append({
                    "speaker": current_speaker,
                    "text": "\n".join(buffer).strip()
                })
                buffer = []
            parts = line.split(":", 1)
            current_speaker = parts[0].strip()
            buffer.append(parts[1].strip())
        else:
            buffer.append(line)

    if buffer:
        frames.append({
            "speaker": current_speaker,
            "text": "\n".join(buffer).strip()
        })

    return frames

def save_frames_as_json(frames, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(frames, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    sample_path = Path("examples/sample.md")
    if sample_path.exists():
        md_content = sample_path.read_text(encoding='utf-8')
        frames = parse_markdown_to_frames(md_content)
        save_frames_as_json(frames, "examples/sample.json")
        print(f"✅ {len(frames)} frames geëxporteerd naar examples/sample.json")
    else:
        print("⚠️ Bestand examples/sample.md niet gevonden.")
