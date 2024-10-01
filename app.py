import sys

VERSION = "0.0.1"

def print_version():
    print(f"v{VERSION}")
    sys.exit(0)

if __name__=="__main__":
    print_version()
