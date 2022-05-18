import argparse


def is_odd(n):
    return n % 2 == 0


def verify_function():
    test_odd = [0, 2, 6, 20, -822, 24523452]
    test_even = [1, 3, -5, 81, -9233, 692303]
    for item in test_odd:
        assert is_odd(item)
    for item in test_even:
        assert not is_odd(item)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_number", type=int, help="an integer")
    args = parser.parse_args()

    verify_function()

    if is_odd(args.input_number):
        print(f"{args.input_number} is an odd number !")
    else:
        print(f"{args.input_number} is an even number !")
