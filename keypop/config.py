from pathlib import Path

def get_config_dir() -> Path:
    """
    Возвращает путь: ~/.config/keypop/
    """
    return Path.home() / ".config" / "keypop"

def get_keys_file() -> Path:
    """
    Возвращает путь: ~/.config/keypop/keys.json
    """
    return get_config_dir() / "keys.json"

def ensure_config_dir() -> None:
    """
    Создает директорию если ее нет
    """
    config_dir = get_config_dir()
    if not config_dir.exists():
        config_dir.mkdir(parents=True, exist_ok=True)
        print("создана директория .config/keypop/")