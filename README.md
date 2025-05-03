# QR Code Batch Generator (CLI Edition)

This Python script reads a CSV file and generates a batch of QR codes with transparent backgrounds. The result is a ZIP archive containing all QR code PNGs.

## 📄 Features

- Batch generation of 2k–5k QR codes
- Transparent background (great for printing)
- Outputs ZIP archive
- CLI with flexible arguments

## 📦 Requirements

- Python 3.7+
- Install dependencies:

```bash
pip install qrcode pandas pillow tqdm
```

## 📁 CSV Format

The input CSV must contain two columns: `id` and `data`

```csv
id,data
001,https://example.com/001
002,https://example.com/002
...
```

## 🚀 Usage

```bash
python generate_qrcodes_cli.py --csv input.csv --zip qr_codes.zip
```

- `--csv`: Path to your input CSV
- `--zip`: Name of the output ZIP file

## 🖨️ Output

- ZIP archive with one PNG file per entry (`id.png`)
- All QR codes have transparent background

## 📄 License

MIT – use it freely, improve it wildly 🚀
