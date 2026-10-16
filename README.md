<<<<<<< HEAD
# Inventory Management System (CLI)

A small command-line application for managing product stock. It supports adding, listing, updating stock, deleting products, and reporting items at or below a low-stock threshold. Product data is persisted in a local JSON file.

## Technology

- Python 3.10+
- Python standard library (`argparse`, `json`, `dataclasses`, `pathlib`)
- `pytest` for unit tests
- `Bandit` for Static Application Security Testing (SAST)
- GitHub Actions for CI automation

## Project structure

```text
inventory-devsecops/
├── inventory/
│   ├── __init__.py
│   ├── models.py
│   ├── validators.py
│   ├── storage.py
│   ├── service.py
│   └── cli.py
├── tests/test_inventory.py
├── main.py
├── requirements.txt
├── pyproject.toml
├── README.md
└── .github/workflows/devsecops.yml
```

The five main source modules (`models.py`, `validators.py`, `storage.py`, `service.py`, and `cli.py`) have distinct responsibilities.

## Run locally

Use Python 3.10 or newer. From the project root, create and activate a virtual environment if desired.

```bash
python -m venv .venv
# Windows PowerShell:
.venv\\Scripts\\Activate.ps1
# Linux/macOS:
source .venv/bin/activate

python -m pip install -r requirements.txt
python main.py add P001 "Wireless Mouse" 12 89000
python main.py add P002 "USB Cable" 3 25000
python main.py list
python main.py stock P001 8
python main.py low-stock --threshold 5
python main.py delete P002
```

By default, data is stored at `data/inventory.json`. Use `--data PATH` immediately after `main.py` to choose another file, for example:

```bash
python main.py --data ./sample-data.json list
python main.py --data ./sample-data.json add P003 "USB Hub" 4 75000
```

## Run tests

```bash
pytest -v
```

## CI/CD and security pipeline

The workflow is defined in `.github/workflows/devsecops.yml` and runs on `push` to `main` and `pull_request` targeting `main`. It uses `ubuntu-latest`.

1. **Build job:** installs dependencies, compiles Python files, and runs unit tests with pytest.
2. **SAST job:** runs only after `build` succeeds (`needs: build`) and scans the `inventory/` source package with Bandit.
3. **Quality Gate:** `bandit -r inventory -ll -ii` fails the job when Bandit reports findings at **Medium or High severity** and **Medium or High confidence**. A failing build also prevents the SAST job from running. This is a simple severity/confidence-based gate; it does not prove that the application is completely secure.
4. **Artifact:** the workflow uploads `bandit-report.json` when the report was generated, including when a later scan step fails.

## Limitations

This is an educational CLI application, not a production inventory platform. It does not include user accounts, concurrent access locking, database transactions, or a web interface. Bandit finds certain risky code patterns but does not replace code review, dependency scanning, or dynamic testing.
=======
# devsecops-p5-0110225168
>>>>>>> cd409818b9e54e91cedcbeffd247d9fdac749abc
