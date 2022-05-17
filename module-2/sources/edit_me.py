import argparse


def main(a):
    print("OK !")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("a", type=int, help="an integer")
    args = parser.parse_args()
    main(args.a)
