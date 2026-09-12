# -*- coding: utf-8 -*-
"""Generate public storyboard strips from local UI frames (or ARANCANO_UI_FRAMES)."""
import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"
# Local frames only. Optional override: ARANCANO_UI_FRAMES=/path/to/ui
_env = os.environ.get("ARANCANO_UI_FRAMES", "").strip()
_CANDIDATES = [Path(_env)] if _env else []
_CANDIDATES.append(ROOT / "assets" / "ui")
UI = next((p for p in _CANDIDATES if p.exists()), _CANDIDATES[-1])

BOARDS = {
    "storyboard-main-path.png": [
        ("08-home-cta.jpg", "打开"),
        ("09-scan-aim.jpg", "对准"),
        ("10-surface-chooser.jpg", "选台面"),
        ("12-ar-ready-relock.jpg", "出模贴住"),
        ("13-press-progress.jpg", "长按蓄力"),
        ("14-seal-post-mood.jpg", "封印收束"),
    ],
    "storyboard-guide-loop.png": [
        ("02-guide-want-scratch.jpg", "想挠"),
        ("03-guide-shutter.jpg", "快门"),
        ("04-guide-recognize.jpg", "识别出包"),
        ("05-guide-longpress.jpg", "长按"),
        ("06-guide-seal.jpg", "出餐封印"),
    ],
    "storyboard-press-multimodal.png": [
        ("11-pre-press-mood.jpg", "开捏前"),
        ("12-ar-ready-relock.jpg", "贴住可按"),
        ("13-press-progress.jpg", "蓄力中"),
    ],
    "storyboard-decision-fallback.png": [
        ("10-surface-chooser.jpg", "默认C / 退路A"),
        ("12-ar-ready-relock.jpg", "微调贴位"),
    ],
    "storyboard-seal-record.png": [
        ("14-seal-post-mood.jpg", "封印"),
        ("15-record-calendar.jpg", "月历记录"),
        ("16-today-card.jpg", "今日入册"),
    ],
    "storyboard-brand-entry.png": [
        ("00-splash-intro.jpg", "开屏"),
        ("01-onboard-annno.jpg", "认识Annno"),
        ("07-promise-go-press.jpg", "去开捏"),
    ],
    "storyboard-track-a.png": [
        ("a01-pre-press-mood.jpg", "开捏前"),
        ("a02-css-ready.jpg", "贴图就绪"),
        ("a03-css-follow.jpg", "贴图跟包"),
        ("a04-css-pressing.jpg", "长按蓄力"),
    ],
}

THUMB_H = 780
GAP = 20
PAD_X = 28
PAD_TOP = 32
LABEL_H = 44
PAD_BOTTOM = 24
MAX_W = 2400
BG = (250, 247, 242)
RULE = (230, 220, 210)
TEXT = (90, 70, 55)


def load_font(size=22):
    for fp in [
        r"C:\Windows\Fonts\msyh.ttc",
        r"C:\Windows\Fonts\msyhbd.ttc",
        r"C:\Windows\Fonts\simhei.ttf",
        r"C:\Windows\Fonts\arial.ttf",
    ]:
        try:
            return ImageFont.truetype(fp, size)
        except Exception:
            pass
    return ImageFont.load_default()


def make_board(items, out_path):
    font = load_font(22)
    prepared = []
    for name, label in items:
        path = UI / name
        if not path.exists():
            raise FileNotFoundError(path)
        im = Image.open(path).convert("RGB")
        ratio = THUMB_H / im.height
        w = max(1, int(im.width * ratio))
        im = im.resize((w, THUMB_H), Image.Resampling.LANCZOS)
        prepared.append((im, label))

    cell_w = max(im.width for im, _ in prepared)
    total_w = PAD_X * 2 + cell_w * len(prepared) + GAP * (len(prepared) - 1)
    total_h = PAD_TOP + THUMB_H + LABEL_H + PAD_BOTTOM
    canvas = Image.new("RGB", (total_w, total_h), BG)
    draw = ImageDraw.Draw(canvas)

    x = PAD_X
    for i, (im, label) in enumerate(prepared):
        ox = x + (cell_w - im.width) // 2
        canvas.paste(im, (ox, PAD_TOP))
        if i < len(prepared) - 1:
            sx = x + cell_w + GAP // 2
            draw.line(
                [(sx, PAD_TOP + 24), (sx, PAD_TOP + THUMB_H - 24)],
                fill=RULE,
                width=1,
            )
        bbox = draw.textbbox((0, 0), label, font=font)
        tw = bbox[2] - bbox[0]
        tx = x + (cell_w - tw) // 2
        ty = PAD_TOP + THUMB_H + 10
        draw.text((tx, ty), label, fill=TEXT, font=font)
        x += cell_w + GAP

    if canvas.width > MAX_W:
        nh = int(canvas.height * (MAX_W / canvas.width))
        canvas = canvas.resize((MAX_W, nh), Image.Resampling.LANCZOS)

    canvas.save(out_path, "PNG", optimize=True)
    print(out_path.name, canvas.size, out_path.stat().st_size)


def main():
    if not UI.exists():
        raise SystemExit(f"missing UI frames: {UI}")
    for filename, items in BOARDS.items():
        make_board(items, OUT / filename)


if __name__ == "__main__":
    main()
