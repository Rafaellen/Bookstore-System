from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / 'data'
BACKUP_DIR = BASE_DIR / 'backups'
EXPORT_DIR = BASE_DIR / 'exports'

DATA_DIR.mkdir(parents=True, exist_ok=True) 
BACKUP_DIR.mkdir(parents=True, exist_ok=True)
EXPORT_DIR.mkdir(parents=True, exist_ok=True)


DB_PATH = DATA_DIR / 'livraria.db'