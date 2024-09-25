import argparse
from .module import greet

def cli():
    # Parse arguments
    parser = argparse.ArgumentParser(description="Command line interface")
    parser.add_argument('name', type=str, help="Name")
    args = parser.parse_args()

    # Run library code
    greet(args.name)

if __name__ == "__main__":
    # Entrypoint to the command line interface
    cli()
