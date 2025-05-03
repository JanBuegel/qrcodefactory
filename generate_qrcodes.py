import os
import pandas as pd
import qrcode
from PIL import Image
from qrcode.image.pil import PilImage
from tqdm import tqdm
import zipfile

# === CONFIGURATION ===
CSV_FILE = "input.csv"           # Path to your CSV file
OUTPUT_DIR = "qr_codes"          # Output directory for PNGs
FILENAME_TEMPLATE = "{id}.png"   # Naming template for output files

# === CREATE OUTPUT DIRECTORY ===
os.makedirs(OUTPUT_DIR, exist_ok=True)

# === LOAD CSV DATA ===
df = pd.read_csv(CSV_FILE)

# === GENERATE QR CODES WITH TRANSPARENT BACKGROUND ===
for _, row in tqdm(df.iterrows(), total=len(df), desc="Generating QR Codes"):
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(row["data"])
    qr.make(fit=True)

    # Generate image with white background (to be made transparent later)
    img = qr.make_image(
        image_factory=PilImage,
        fill_color="black",
        back_color="white"
    ).convert("RGBA")

    # Convert white background to transparent
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[:3] == (255, 255, 255):  # white
            newData.append((255, 255, 255, 0))  # fully transparent
        else:
            newData.append(item)
    img.putdata(newData)

    # Save as PNG
    filename = FILENAME_TEMPLATE.format(**row)
    img.save(os.path.join(OUTPUT_DIR, filename))

# === CREATE ZIP ARCHIVE ===
zip_path = f"{OUTPUT_DIR}.zip"
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for filename in os.listdir(OUTPUT_DIR):
        if filename.endswith(".png"):
            zipf.write(os.path.join(OUTPUT_DIR, filename), arcname=filename)

print(f"\n✅ {len(df)} QR codes generated with transparent backgrounds.")
print(f"📦 ZIP archive created: {zip_path}")
