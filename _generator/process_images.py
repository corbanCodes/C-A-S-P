#!/usr/bin/env python3
"""Crop, colour-correct and compress the chosen candidates into assets/img/.

Only the files listed in PICKS ship. Everything else stays in _generator/raw/
(gitignored) so the shortlist stays reviewable without bloating the repo.
"""
import glob, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
OUT = os.path.join(HERE, "..", "assets", "img")

# out-name -> (raw glob, crop geometry, extra magick args)
WIDE = "1800x1013^"      # 16:9 heroes and banners
CARD = "1200x900^"       # 4:3 cards
TALL = "1000x1250^"      # portrait detail

PICKS = {
    # --- accessibility ---
    "plaza-ramp":        ("ada-compliant-design--wyly-slope*", WIDE, []),
    "entrance-ramp":     ("tactile-paving-in-the-united-states--mcdonald-place-northeast*", WIDE, []),
    "curb-ramp":         ("tactile-paving-in-the-united-states--sidewalk-ramp-to-flush-curb-with-flat-tac*", CARD, []),
    "sidewalk-ramp":     ("tactile-paving-truncated-domes--long-gradual-sidewalk-ramp-to-tactile-paving-a*", CARD, []),
    "tactile-pad":       ("tactile-paving-truncated-domes--tactile-paving-march-2025-sarah-stierch*", CARD, []),
    "parking-sign":      ("disabled-parking--handicapped-parking-sign-in-the-las-cienegas*", TALL, []),
    "parking-stalls":    ("disabled-parking--c260916*", CARD, []),
    "handrail":          ("disability-handrails--san-francisco-airport-marriott*", CARD, []),
    "restroom":          ("accessible-toilets--public-toilet-1*", CARD, []),
    # --- structural / EEE ---
    "weathered-wood":    ("wood-decay--2011-365-82-cracks-across-time*", WIDE, []),
    "residential-eee":   ("balconies-in-the-united-states--1407-beach-cmhd*", WIDE, []),
    "condo-lake":        ("apartment-buildings-in-california--condominiums-on-the-lake-nara-543527*",
                          WIDE, ["-modulate", "100,72,100", "-auto-level", "-brightness-contrast", "-4x6"]),
    "condo-construction":("apartment-buildings-in-california--condominium-construction-nara-543583*",
                          CARD, ["-modulate", "100,68,100", "-auto-level", "-brightness-contrast", "-4x6"]),
    "commercial-street": ("california-street-commercial-building--commercial-building-alisal-street-salin*", WIDE, []),
}

def run(cmd):
    subprocess.run(cmd, check=True)

def main():
    os.makedirs(OUT, exist_ok=True)
    manifest = {m["file"]: m for m in json.load(open(os.path.join(RAW, "manifest.json")))}
    used = []
    for name, (pattern, geom, extra) in PICKS.items():
        hits = sorted(glob.glob(os.path.join(RAW, pattern)))
        if not hits:
            print(f"  !! no raw file for {name} ({pattern})", file=sys.stderr)
            continue
        src = hits[0]
        dst = os.path.join(OUT, f"{name}.jpg")
        run(["magick", src, "-auto-orient", *extra,
             "-resize", geom, "-gravity", "center", "-extent", geom.rstrip("^"),
             "-strip", "-interlace", "Plane", "-sampling-factor", "4:2:0",
             "-quality", "82", dst])
        run(["cwebp", "-quiet", "-q", "80", dst, "-o", os.path.join(OUT, f"{name}.webp")])
        meta = manifest.get(os.path.basename(src), {})
        used.append({"name": name, **{k: meta.get(k) for k in
                    ("title", "creator", "license", "license_url", "page")}})
        print(f"{name}.jpg  <-  {os.path.basename(src)[:60]}")

    with open(os.path.join(HERE, "used_images.json"), "w") as f:
        json.dump(used, f, indent=2)
    print(f"\n{len(used)} images in assets/img/")

if __name__ == "__main__":
    main()
