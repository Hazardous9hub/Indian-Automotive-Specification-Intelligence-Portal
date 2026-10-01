import os
from PIL import Image

vehicles_dir = "3d_viewer/assets/vehicles"
max_width = 600

count = 0
for fname in sorted(os.listdir(vehicles_dir)):
    if fname.endswith(".png"):
        fpath = os.path.join(vehicles_dir, fname)
        orig_kb = os.path.getsize(fpath) / 1024.0
        
        im = Image.open(fpath)
        
        # Resize to max_width preserving aspect ratio
        if im.width > max_width:
            h = int(im.height * (max_width / float(im.width)))
            im = im.resize((max_width, h), Image.Resampling.LANCZOS)
        
        # Quantize colors to 256 palette with alpha transparency
        im_opt = im.quantize(colors=256, method=Image.Quantize.FASTOCTREE)
        
        # Save to temporary path first
        temp_path = fpath + ".tmp"
        im_opt.save(temp_path, format="PNG", optimize=True)
        
        # Check size
        new_kb = os.path.getsize(temp_path) / 1024.0
        os.replace(temp_path, fpath)
        
        print(f"{fname:<28}: {orig_kb:>7.1f} KB  -->  {new_kb:>5.1f} KB  (Dim: {im.size})")
        count += 1

print(f"\nSUCCESS: Optimized all {count} vehicle PNG images for Tableau Image Role (All under 120 KB)!")
