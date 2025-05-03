import argparse
import os
import pandas as pd
import qrcode
from qrcode.image.pil import PilImage
from PIL import Image
import zipfile
from tqdm import tqdm
from io import BytesIO

def generate_qr_codes(csv_file, zip_file, use_logo=False, logo_file=None):
    # Read input CSV
    df = pd.read_csv(csv_file)

    # Create ZIP archive
    with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for _, row in tqdm(df.iterrows(), total=len(df), desc="Generating QR Codes"):
            # Create QR code with high error correction
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(row["data"])
            qr.make(fit=True)

            # Create image
            img = qr.make_image(
                image_factory=PilImage,
                fill_color="black",
                back_color="white"
            ).convert("RGBA")

            # Make white background transparent
            datas = img.getdata()
            newData = []
            for item in datas:
                if item[:3] == (255, 255, 255):
                    newData.append((255, 255, 255, 0))
                else:
                    newData.append(item)
            img.putdata(newData)

            # If logo should be used
            if use_logo and logo_file and os.path.exists(logo_file):
                logo = Image.open(logo_file).convert("RGBA")
                qr_width, qr_height = img.size
                logo_size = int(qr_width * 0.2)
                logo = logo.resize((logo_size, logo_size), Image.ANTIALIAS)
                x = (qr_width - logo_size) // 2
                y = (qr_height - logo_size) // 2
                img.paste(logo, (x, y), logo)

            # Save image to bytes and write into zip
            buffer = BytesIO()
            filename = f"{row['id']}.png"
            img.save(buffer, format="PNG")
            zipf.writestr(filename, buffer.getvalue())

    print(f"\n✅ {len(df)} QR codes written to ZIP: {zip_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate QR codes from a CSV file into a ZIP archive.")
    parser.add_argument("--csv", required=True, help="Path to the input CSV file")
    parser.add_argument("--zip", required=True, help="Name of the output ZIP file")
    parser.add_argument("--use-logo", action="store_true", help="Include this flag to embed a logo")
    parser.add_argument("--logo", default="logo.png", help="Path to logo image file")
    args = parser.parse_args()

    generate_qr_codes(args.csv, args.zip, args.use_logo, args.logo)
