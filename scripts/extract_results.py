"""Regenerate docs/results/*.png from the saved outputs in each notebook.
Run from the repo root:  python scripts/extract_results.py
No dependencies beyond the Python standard library."""
import json, base64, os, glob

os.makedirs("docs/results", exist_ok=True)

# PNG-output index to use per notebook (-1 = final frame)
FRAME = {
    "01-diffusion-single-region": -1,
    "02-diffusion-three-regions": 1,   # step 100, before the regions diffuse into a faint blob
    "03-proliferation-small-diffusion": -1,
    "04-diffusion-proliferation": -1,
    "05-diffusion-proliferation-irrigation": -1,  # final vessel-density field
}

for nb in sorted(glob.glob("notebooks/*.ipynb")):
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
    idx = FRAME.get(stem, -1)
    with open(f"docs/results/{stem}.png", "wb") as g:
        g.write(base64.b64decode(pngs[idx]))
    print(f"{stem}: {len(pngs)} frames -> docs/results/{stem}.png (frame {idx})")
