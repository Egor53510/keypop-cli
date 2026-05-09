import os
from pathlib import Path
from keypop.storage import add_key, get_key, list_keys as get_list_keys, remove_key, export, update_key

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

    success = add_key(name=name, key=key)

    if not success:
        print(f"Key '{name}' already exists")
        confirm = input("Overwrite? (y/n): ").lower().strip()

        if confirm != "y":
            print("Canceled")
            return
        
        add_key(name=name, key=key, overwrite=True)

    print(f"✓ Key '{name}' added")

def get(name: str, unmasked: bool = False, to_env: str | None = None):
    key = get_key(name=name)

    if not key:
        print("Key not found")
        return
    
    if to_env:
        path = Path(to_env)
        mode = "a" if path.exists() else "w"

        with open(path, mode, encoding="utf-8") as f:
            f.write(f"{name}={key}")
        print(f"✓ Written to {to_env}")    
    if unmasked:
        print(f"{name} = {key}")
    else:
        print(f"{name} = {_mask(key)}")
    
def list_keys():
    keys = get_list_keys()

    if not keys:
        print("No keys")
        return
    
    print("\nNAME       KEY")
    print("-" * 30)

    for name , key in keys.items():
        print(f"{name:<10} {_mask(key)}")

def remove(name: str):
    confirm = input(f"Delete '{name}' key ? (y/n): ").lower().strip()
    if confirm != 'y':
        print("Cancelled")
        return

    success = remove_key(name=name)

    if success:
        print(f"✓ Removed: {name}")
    else:
        print("Key not found")

def update(name: str | None = None, key: str | None = None):
    """
    Обновляет значение ключа.
    Интерактивный (нет аргументов) или неинтерактивный (есть name/key).
    """
    if not name:
        name = input("Name of key to update: ").strip()

    current = get_key(name)
    if not current:
        print(f"Key '{name}' not found")
        confirm = input("Create new key? (y/n): ").lower().strip()
        if confirm != "y":
            print("Canceled")
            return
        key = key or input("Input new key: ").strip()
        add_key(name=name, key=key)
        print(f"✓ Key '{name}' created")
        return

    if not key:
        key = input(f"Input new value for '{name}': ").strip()

    confirm = input(f"Update '{name}'? (y/n): ").lower().strip()
    if confirm != "y":
        print("Canceled")
        return

    update_key(name=name, new_key=key)
    print(f"✓ Key '{name}' updated")

def export_all(env_file: str):
    keys = export()

    path = Path(env_file)
    mode = "a" if path.exists() else "w"

    with open(path, mode, encoding="utf-8") as f:
        for name, key in keys.items():
            f.write(f"{name}={key}\n")

    print("✓ Exported to {env_file}")


def version():
    print("keypop CLI v0.1.0")
