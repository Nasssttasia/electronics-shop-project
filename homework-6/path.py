from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_PATH = Path.joinpath(ROOT, 'src')
ITEM_PATH = Path.joinpath(SRC_PATH, 'item.csv')
# ITEMS_PATH = Path.joinpath(SRC_PATH, 'items.csv')