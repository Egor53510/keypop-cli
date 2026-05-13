# keypop

[![PyPI version](https://img.shields.io/pypi/v/keypop?color=blue)](https://pypi.org/project/keypop/)
[![Python versions](https://img.shields.io/pypi/pyversions/keypop?color=blue)](https://pypi.org/project/keypop/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Downloads](https://pepy.tech/badge/keypop/month)](https://pepy.tech/project/keypop)

Simple CLI tool for storing and managing API keys securely.

## Installation

### Using pipx (recommended)

```bash
pipx install keypop
```

### Using pip

```bash
pip install keypop
```

## Quick Start

```bash
# Add your first key
keypop add openrouter sk-xxx...

# Get a key (masked by default) or export to .env
keypop get openrouter

keypop get openrouter --to-env .env

# List all keys
keypop list

# Export all keys to .env file
keypop export .env

# Update a key
keypop update openai sk-new-key

# Remove a key
keypop remove openai
```

## Commands

### add

Add a new API key.

```bash
keypop add              # Interactive mode
keypop add <name> <key>  # Non-interactive mode
```

Examples:
```bash
keypop add openai sk-abc123
keypop add github ghp_xxxxxxxxxxxx
```

If a key with the same name exists, you'll be prompted to overwrite.

---

### get

Get a stored API key by name.

```bash
keypop get <name> [--unmasked] [--to-env <file>]
```

Options:
- `--unmasked` - Show the full key instead of masked version
- `--to-env <file>` - Write key to .env file (format: NAME=KEY)

Examples:
```bash
keypop get openai
keypop get openai --unmasked
keypop get openai --to-env .env.local
```

---

### list

List all stored keys.

```bash
keypop list
```

Output:
```
NAME       KEY
------------------------------
openai     sk-abc***23
github     ghp_xxx***yz
```

---

### update

Update an existing key's value.

```bash
keypop update <name> [new_key]
```

Options:
- Interactive mode if no arguments provided
- Non-interactive mode with name and new_key
- If key doesn't exist, prompts to create new one

Examples:
```bash
keypop update openai sk-new-key
keypop update openai        # Interactive mode
```

---

### remove

Remove a stored key.

```bash
keypop remove <name>
```

You'll be prompted for confirmation before deletion.

Example:
```bash
keypop remove openai
```

---

### export

Export all keys to a .env file.

```bash
keypop export [file]
```

Options:
- `file` - Target file path (default: .env)

Example:
```bash
keypop export .env
keypop export .env.production
```

Output format:
```
openai=sk-abc123
github=ghp_xxxxx
```

---

### --version

Show version information.

```bash
keypop --version
```

Output: `keypop CLI v0.1.0`

---

## Python Library
Install:
```bash
pip install keypop
```
Usage:

import keypop

# Get single key
api_key = keypop.get_key("openai")
# Get all keys as dict
keys = keypop.all_keys()


## Configuration

- **Storage location**: `~/.config/keypop/keys.json`
- **Created automatically** on first use

## Security

### Prevent keys from saving in shell history

When using keypop in interactive mode, keys are typed as input and may be saved in your shell history. To prevent this:

1. Open your shell config file:
   ```bash
   nano ~/.zshrc   # for Zsh
   # or
   nano ~/.bashrc  # for Bash
   ```

2. Add this line at the end:
   ```bash
   export HISTIGNORE="*keypop*"
   ```

3. Save and apply:
   ```bash
   source ~/.zshrc   # for Zsh
   # or
   source ~/.bashrc  # for Bash
   ```

Now all commands containing "keypop" will be ignored in your history.

## License

MIT License - see [LICENSE](LICENSE) file for details.