import sys


def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to the projet."


if __name__ == "__main__":
    who = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greet(who))
