# QR Code Batch Generator

This Python script reads a CSV file and generates a batch of QR codes with transparent backgrounds. The result is a ZIP archive containing all QR code PNGs.

## 📄 Features

- Batch generation of 2k–5k QR codes
- Transparent background (ideal for printing on colored material)
- Automatic ZIP archive creation
- Progress bar for generation feedback

## 📦 Requirements

- Python 3.7+
- Dependencies:

```bash
pip install qrcode[pil] pandas pillow tqdm
```

## 📁 CSV Format

Your `input.csv` should look like this:

```csv
id,data
001,https://example.com/001
002,https://example.com/002
...
```

## 🚀 Run the script

```bash
python generate_qrcodes.py
```

This will:

- Create a `qr_codes/` directory with all PNG files
- Generate a `qr_codes.zip` archive

## 🖨️ Output

- PNG files: Named by `id`, e.g. `001.png`, `002.png`, ...
- Transparent background for clean printing

## 📄 License

MIT – do whatever you want 🚀
