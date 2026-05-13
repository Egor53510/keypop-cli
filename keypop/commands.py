from pathlib import Path
from keypop.storage import add_key, get_key_cli, list_keys as get_list_keys, remove_key, export, update_key
from keypop.ui.ui import success, error

def _mask(key: str) -> str:
    if len(key) <= 4:
        return "*" * len(key)
    return key[:2] + "***" + key[-2:]

def add(name: str | None = None, key: str | None = None):
    """
    add:
    - интерактивный (если нет аргументов)
    - неинтерактивный (если передали name/key)
    """
    if not name:
        name = input("Name of key: ").strip()
    
    if not key:
        key = input("Input key: ").strip()

    successed = add_key(name=name, key=key)

    if not successed:
        error(f"Key '{name}' already exists") 
        confirm = input("Overwrite? (y/n): ").lower().strip()

        if confirm != "y":
            success("Canceled")
            return
        
        add_key(name=name, key=key, overwrite=True)

    success(f"Key '{name}' added")

def get(name: str, unmasked: bool = False, to_env: str | None = None):
    key = get_key_cli(name=name)

    if not key:
        error("Key not found")
        return
    
    if to_env:
        path = Path(to_env)
        mode = "a" if path.exists() else "w"

        with open(path, mode, encoding="utf-8") as f:
            f.write(f"{name}={key}")
        success(f"Written to {to_env}")    
    if unmasked:
        print(f"{name} = {key}")
    else:
        print(f"{name} = {_mask(key)}")
    
def list_keys():
    keys = get_list_keys()

    if not keys:
        error("No keys")
        return
    
    print("\nNAME       KEY")
    print("-" * 30)

    for name , key in keys.items():
        print(f"{name:<10} {_mask(key)}")

def remove(name: str):
    confirm = input(f"Delete '{name}' key ? (y/n): ").lower().strip()
    if confirm != 'y':
        success("Cancelled")
        return

    successed = remove_key(name=name)

    if successed:
        success(f"Removed: {name}")
    else:
        error("Key not found")

def update(name: str | None = None, key: str | None = None):
    """
    Обновляет значение ключа.
    Интерактивный (нет аргументов) или неинтерактивный (есть name/key).
    """
    if not name:
        name = input("Name of key to update: ").strip()

    current = get_key_cli(name)
    if not current:
        error(f"Key '{name}' not found")
        confirm = input("Create new key? (y/n): ").lower().strip()
        if confirm != "y":
            success("Canceled")
            return
        key = key or input("Input new key: ").strip()
        add_key(name=name, key=key)
        success(f"Key '{name}' created")
        return

    if not key:
        key = input(f"Input new value for '{name}': ").strip()

    confirm = input(f"Update '{name}'? (y/n): ").lower().strip()
    if confirm != "y":
        success("Canceled")
        return

    update_key(name=name, new_key=key)
    success(f"Key '{name}' updated")

def export_all(env_file: str):
    keys = export()

    path = Path(env_file)
    mode = "a" if path.exists() else "w"

    with open(path, mode, encoding="utf-8") as f:
        for name, key in keys.items():
            f.write(f"{name}={key}\n")

    success("Exported to {env_file}")


def version():
    print("keypop CLI v0.1.0")
