# keypop

[![PyPI version](https://img.shields.io/pypi/v/keypop?color=blue)](https://pypi.org/project/keypop/)
[![Python versions](https://img.shields.io/pypi/pyversions/keypop?color=blue)](https://pypi.org/project/keypop/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Downloads](https://pepy.tech/badge/keypop/month)](https://pepy.tech/project/keypop)

Simple CLI tool and Python library for storing and managing API keys securely.

## Features

- **CLI** — easy commands: `keypop add openai sk-xxx`
- **Python Library** — use in scripts: `import keypop; keypop.get_key("openai")`
- **Export** — migrate to .env files

## Installation

### Using pipx (recommended)

```bash
pipx install keypop
```
### Using pip
```bash
pip install keypop
```

---

## Quick Start

## CLI

#### Add a key

```bash
keypop add openai sk-xxx
```

#### Get a key

```bash
keypop get openai
```

#### List all keys

```bash
keypop list
```

#### Export to .env

```bash
keypop export .env
```

#### Update a key

```bash
keypop update openai sk-new-key
```

#### Remove a key

```bash
keypop remove openai
```

## Python Library

```bash
pip install keypop
```
```python
import keypop

# Get single key
api_key = keypop.get_key("openai")

# Get all keys as dict
keys = keypop.all_keys()
```
---

### CLI Commands

add

Add a new API key.
```bash
keypop add <name> <key>   # Non-interactive
keypop add               # Interactive mode
```

---

get

Get a stored API key.
```bash
keypop get <name> [--unmasked] [--to-env <file>]
```
Options:
- --unmasked — show full key
- --to-env <file> — write to .env file

---

list

List all stored keys.
```bash
keypop list
```

---

update

Update an existing key.
```bash
keypop update <name> [new_key]
```

---

remove

Remove a stored key.
```bash
keypop remove <name>
```

---

export

Export all keys to .env file.
```bash
keypop export [file]
```

---

version

Show version.
```bash
keypop --version
```

---

## Configuration
- **Storage location**: `~/.config/keypop/keys.json`
- **Created automatically** on first use

---

Security

Prevent keys from saving in shell history

Add to ~/.zshrc or ~/.bashrc:

export HISTIGNORE="*keypop*"

Then run: source ~/.zshrc

---

License

MIT License — see LICENSE (LICENSE) file for details.
