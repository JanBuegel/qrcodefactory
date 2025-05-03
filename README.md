# QR Code Batch Generator (CLI Edition)

This Python script reads a CSV file and generates a batch of QR codes with transparent backgrounds, optionally embedding a logo in the center. The result is a ZIP archive containing all QR code PNGs.

## 📄 Features

- Batch generation of 2k–5k QR codes
- Transparent background (great for printing)
- Optional logo embedded in the center
- Outputs ZIP archive only (no separate PNG files on disk)
- CLI with flexible arguments

## 📦 Requirements

- Python 3.7+
- Install dependencies:

```bash
pip install qrcode[pil] pandas pillow tqdm
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

### Embed a logo in the center of each QR code:

```bash
python generate_qrcodes_cli.py --csv input.csv --zip qr_codes.zip --use-logo --logo logo.png
```

- `--csv`: Path to your input CSV
- `--zip`: Name of the output ZIP file
- `--use-logo`: Optional flag to include a logo
- `--logo`: Path to the logo PNG file (default: `logo.png`)

## 🖨️ Output

- ZIP archive with one PNG file per entry (`id.png`)
- All QR codes have transparent background
- Optional logo overlay (centered)

## 🧪 Tips

- Use a transparent PNG logo for best results
- Logos should cover no more than ~20% of the QR code area
- QR codes use high error correction to ensure scan reliability

## 📄 License

MIT – use it freely, improve it wildly 🚀
