from numpy import diagonal


class Matrix:
    pass


def main():
    m1 = Matrix((1, 0, 0), (0, 1, 0), (0, 1, 1))
    m2 = Matrix((1, 0, 0), (0, 1, 0), (0, 1, 1))

    first_row = m1[0]
    assert first_row == (1, 0, 0)
    print("get item works !")

    mul = m1 @ m2
    assert isinstance(mul, Matrix)
    print("matrix multiply works !")

    sum = m1 + m2
    assert isinstance(sum, Matrix)

    twice = m1 * 2
    assert isinstance(twice, Matrix)


    print(m1)  # prints (1,0,0), (0,1,0), (0,1,1)
    assert str(m1) == "(1,0,0), (0,1,0), (0,1,1)"

    diag3 = DiagonalMatrix(3, 3)
    assert diag3[0] == (3, 0, 0)

    print("OK !")


if __name__ == "__main__":
    main()
