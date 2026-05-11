import argparse
from keypop import commands

def main():
    parser = argparse.ArgumentParser(prog="keypop", description="Simple CLI tool for storing and managing API keys")
    parser.add_argument("--version", action="store_true", help="Show version")
    subparsers = parser.add_subparsers(dest="command")

    #add
    add_parser = subparsers.add_parser("add", help="Add a new API key", description="Add a new API key to storage")
    add_parser.add_argument("name", nargs="?", help="Key name")
    add_parser.add_argument("key", nargs="?", help="Key value")

    #get
    get_parser = subparsers.add_parser("get", help="Get a stored API key", description="Get a stored API key by name")
    get_parser.add_argument("name", help="Key name")
    get_parser.add_argument("--unmasked", action="store_true", help="Show full key instead of masked")
    get_parser.add_argument("--to-env", metavar="FILE", help="Write key to .env file (format: NAME=KEY)")

    #update
    update_parser = subparsers.add_parser("update", help="Update an existing key", description="Update an existing key's value")
    update_parser.add_argument("name", nargs="?", help="Key name to update")
    update_parser.add_argument("key", nargs="?", help="New key value")

    #remove
    remove_parser = subparsers.add_parser("remove", help="Remove a stored key", description="Remove a stored key by name")
    remove_parser.add_argument("name", help="Key name to remove")

    #export
    export_parser = subparsers.add_parser("export", help="Export all keys to .env file", description="Export all keys to .env file")
    export_parser.add_argument("file", nargs="?", default=".env", help="Target file path (default: .env)")

    args = parser.parse_args()

    if args.version:
        commands.version()

    elif args.command == "add":
        commands.add(args.name, args.key)

    elif args.command == "get":
        commands.get(args.name, args.unmasked, args.to_env)

    elif args.command == "list":
        commands.list_keys()

    elif args.command == "remove":
        commands.remove(args.name)

    elif args.command == "update":
        commands.update(args.name, args.key)

    elif args.command == "export":
        commands.export_all(args.file)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()