"""Regenerate the gallery images from the saved outputs in each notebook.
Run from the repo root:  python corrected/scripts/extract_results.py
No dependencies beyond the Python standard library."""
import json, base64, os, glob

# PNG-output index to use per original notebook (-1 = final frame)
FRAME = {
    "01-diffusion-single-region": -1,
    "02-diffusion-three-regions": 1,   # step 100, before the regions diffuse into a faint blob
    "03-proliferation-small-diffusion": -1,
    "04-diffusion-proliferation": -1,
    "05-diffusion-proliferation-irrigation": -1,  # final vessel-density field
}

# (notebook glob, output folder, mode)
#   "frame": one image, chosen by FRAME (original notebooks)
#   "last":  the last image (corrected notebooks draw one summary figure)
#   "all":   every image, saved as <stem>-1.png, <stem>-2.png, ... (notebooks 06-10)
SOURCES = [
    ("original/notebooks/*.ipynb", "original/figures", "frame"),
    ("corrected/notebooks/0[1-5]-*.ipynb", "corrected/figures", "last"),
    ("corrected/notebooks/0[6-9]-*.ipynb", "corrected/figures", "all"),
    ("corrected/notebooks/1[0-9]-*.ipynb", "corrected/figures", "all"),
]

for pattern, dest, mode in SOURCES:
    os.makedirs(dest, exist_ok=True)
    for nb in sorted(glob.glob(pattern)):
        stem = os.path.splitext(os.path.basename(nb))[0]
        with open(nb, encoding="utf-8") as f:
            data = json.load(f)
        pngs = []
        for cell in data.get("cells", []):
            for out in cell.get("outputs", []):
                img = out.get("data", {}).get("image/png")
                if img:
                    pngs.append("".join(img) if isinstance(img, list) else img)
        if not pngs:
            print(f"{stem}: no images, skipped"); continue
        if mode == "all":
            for k, png in enumerate(pngs, start=1):
                with open(f"{dest}/{stem}-{k}.png", "wb") as g:
                    g.write(base64.b64decode(png))
            print(f"{nb}: {len(pngs)} frames -> {dest}/{stem}-1..{len(pngs)}.png")
            continue
        idx = FRAME.get(stem, -1) if mode == "frame" else -1
        with open(f"{dest}/{stem}.png", "wb") as g:
            g.write(base64.b64decode(pngs[idx]))
        print(f"{nb}: {len(pngs)} frames -> {dest}/{stem}.png (frame {idx})")
