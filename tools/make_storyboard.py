from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

root = Path(__file__).resolve().parents[1]
ui = root / "assets" / "ui"
out = root / "assets" / "storyboard-main-path.png"

items = [
    ("08-home-cta.jpg", "打开"),
    ("09-scan-aim.jpg", "对准"),
    ("10-surface-chooser.jpg", "选台面"),
    ("12-ar-ready-relock.jpg", "出模贴住"),
    ("13-press-progress.jpg", "长按蓄力"),
    ("14-seal-post-mood.jpg", "封印收束"),
]

thumb_h = 420
gap = 16
pad_x = 24
pad_top = 28
label_h = 36
pad_bottom = 20
bg = (250, 247, 242)
rule = (230, 220, 210)
text_color = (90, 70, 55)

imgs = []
for name, label in items:
    im = Image.open(ui / name).convert("RGB")
    ratio = thumb_h / im.height
    w = max(1, int(im.width * ratio))
    im = im.resize((w, thumb_h), Image.Resampling.LANCZOS)
    imgs.append((im, label))

cell_w = max(im.width for im, _ in imgs)
total_w = pad_x * 2 + cell_w * len(imgs) + gap * (len(imgs) - 1)
total_h = pad_top + thumb_h + label_h + pad_bottom

canvas = Image.new("RGB", (total_w, total_h), bg)
draw = ImageDraw.Draw(canvas)

font = None
for fp in [
    r"C:\Windows\Fonts\msyh.ttc",
    r"C:\Windows\Fonts\msyhbd.ttc",
    r"C:\Windows\Fonts\simhei.ttf",
    r"C:\Windows\Fonts\arial.ttf",
]:
    try:
        font = ImageFont.truetype(fp, 18)
        break
    except Exception:
        pass
if font is None:
    font = ImageFont.load_default()

x = pad_x
for i, (im, label) in enumerate(imgs):
    ox = x + (cell_w - im.width) // 2
    canvas.paste(im, (ox, pad_top))
    if i < len(imgs) - 1:
        sx = x + cell_w + gap // 2
        draw.line(
            [(sx, pad_top + 20), (sx, pad_top + thumb_h - 20)],
            fill=rule,
            width=1,
        )
    bbox = draw.textbbox((0, 0), label, font=font)
    tw = bbox[2] - bbox[0]
    tx = x + (cell_w - tw) // 2
    ty = pad_top + thumb_h + 8
    draw.text((tx, ty), label, fill=text_color, font=font)
    x += cell_w + gap

max_w = 1600
if canvas.width > max_w:
    nh = int(canvas.height * (max_w / canvas.width))
    canvas = canvas.resize((max_w, nh), Image.Resampling.LANCZOS)

canvas.save(out, "PNG", optimize=True)
print(out, canvas.size, out.stat().st_size)
