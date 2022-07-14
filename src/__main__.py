from os import getcwd
from parser import parse

if __name__ == "__main__":
    directory = getcwd()
    parse(f"{directory}/input/index.ts")
