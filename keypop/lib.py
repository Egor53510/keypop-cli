from keypop.storage import get_key_cli, load_keys

def get_key(name: str) -> str | None:
    """Get key"""
    return get_key_cli(name=name)

def get_all_keys() -> dict[str, str]:
    """Get all keys"""
    kyes = load_keys()
    return kyes