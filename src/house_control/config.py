from pathlib import Path

DICTIONARY_FILE = Path('../../data/odm.txt')
if not DICTIONARY_FILE.exists():
    DICTIONARY_FILE = Path('../data/odm.txt')
    assert DICTIONARY_FILE.exists(), f"Cannot find required file {DICTIONARY_FILE.name}"
