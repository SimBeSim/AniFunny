# ani_video.py – YouTube-achtige MP4 generator
# ----------------------------------------------
# Dit script maakt van sample.json een automatisch afspelende video-achtige animatie en rendert dit als MP4

from pathlib import Path
import json
import random
from moviepy.editor import ImageClip, concatenate_videoclips
from PIL import Image, ImageDraw, ImageFont
import tempfile

WIDTH, HEIGHT = 640, 360
FONT_SIZE = 22  # Aangepast voor betere regelpassing
DURATION_PER_CHAR = 0.031  # Iets langzamer dan standaard leestempo (-30%)
MARGIN = 20
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def render_typing_clip():
    typing_text = "aan het typen..."
    duration = random.uniform(3, 8)

    img = Image.new("RGB", (WIDTH, HEIGHT), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    except:
        font = ImageFont.load_default()

    w, h = draw.textbbox((0, 0), typing_text, font=font)[2:]
    x = (WIDTH - w) // 2
    y = (HEIGHT - h) // 2
    draw.text((x, y), typing_text, font=font, fill=(180, 180, 180))

    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        img.save(tmp.name)
        clip = ImageClip(tmp.name).set_duration(duration)

    return clip


def render_frame_to_clip(speaker, text):
    full_text = f"{speaker}:\n{text}"
    duration = max(2.5, len(text) * DURATION_PER_CHAR)

    img = Image.new("RGB", (WIDTH, HEIGHT), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    except:
        font = ImageFont.load_default()

    lines = full_text.split("\n")
    line_heights = [draw.textbbox((0, 0), line, font=font)[3] for line in lines]
    total_height = sum(line_heights)
    y = (HEIGHT - total_height) // 2
    for line in lines:
        w, h = draw.textbbox((0, 0), line, font=font)[2:]
        x = (WIDTH - w) // 2
        draw.text((x, y), line, font=font, fill=(255, 255, 255))
        y += h

    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        img.save(tmp.name)
        text_clip = ImageClip(tmp.name).set_duration(duration)

    return concatenate_videoclips([render_typing_clip(), text_clip])


def generate_video(frames_path, output_path):
    with open(frames_path, encoding='utf-8') as f:
        frames = json.load(f)

    clips = [render_frame_to_clip(frame['speaker'], frame['text']) for frame in frames]
    final = concatenate_videoclips(clips, method="compose")
    final.write_videofile(str(output_path), fps=24)


if __name__ == "__main__":
    json_path = Path("examples/sample.json")
    output_path = Path("examples/sample.mp4")

    if json_path.exists():
        generate_video(json_path, output_path)
        print(f"🎥 Video gegenereerd naar {output_path}")
    else:
        print("⚠️ Voorbeeldbestand ontbreekt: examples/sample.json")
