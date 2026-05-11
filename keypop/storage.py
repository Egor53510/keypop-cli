import json

from keypop.config import get_keys_file, ensure_config_dir

def _load_raw() -> dict:
    """
    Загружает весь JSON файл.
    Если файла нет — возвращает пустую структуру.
    """
    ensure_config_dir()
    path = get_keys_file()

    if not path.exists():
        return {"version": "1.0", "keys": {}}

    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def _save_raw(data: dict) -> None:
    """
    Сохранение json
    """
    ensure_config_dir()
    path = get_keys_file()
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
def load_keys() -> dict:
    """Возвращает только keys"""
    return _load_raw().get("keys", {})


def save_keys(keys: dict) -> None:
    """Полная перезапись keys"""
    _save_raw({
        "version": "1.0",
        "keys": keys
    })

def get_key(name: str) -> str | None:
    """
    Получает ключ по имени
    """
    return load_keys().get(name)

def add_key(name: str, key: str, overwrite: bool = False) -> bool:
    keys = load_keys()

    if name in keys and not overwrite:
        return False

    keys[name] = key
    save_keys(keys=keys)
    return True

def remove_key(name: str) -> bool:
    """
    Удаляет ключ.
    Возвращает True если был удалён, False если не найден.
    """
    keys = load_keys()

    if name not in keys:
        return False

    del keys[name]
    save_keys(keys=keys)
    return True

def list_keys() -> list[str]:
    """
    Список всех имён ключей
    """
    return load_keys()

def update_key(name: str, new_key: str):
    """
    Обновляет ключ. 
    Возвращает True если обновлен, иначе False
    """
    keys = load_keys()
    if name not in keys:
        return False
    keys[name] = new_key
    save_keys(keys=keys)
    return True

def export() -> dict:
    return load_keys()