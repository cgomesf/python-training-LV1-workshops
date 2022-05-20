# Workshop Module 5 - Class inheritance

We'll implement a matrix class

For reminder, a matrix has rows and columns of number, like a table:

|1|1|
|0|1|
|1|0|

Matrix can be added if they are compatible for addition (same width and height)

Matrix can be multiplied, M x N is allowed if M.height = N.width

Matrix have a "times" operator, which takes a real number: M x n


So we would like to use it like:

```python
m1 = Matrix( (1,0,0), (0,1,0), (0,1,1) )
m2 = Matrix( (1,0,0), (0,1,0), (0,1,1) )

mul = m1 @ m2
sum = m1 + m2
twice = m1 * 2

first_row = m1[0]

print(m1) # prints (1,0,0), (0,1,0), (0,1,1)
```


## 1 - Enter the matrix

1. Create the matrix class
2. Change the __str__ method to have a nice representation

## 2 - Math

1. Create the addition method and assign it to the + operator
2. Add the [] operator so we can use m[n] to get the nth row
3. Add the matmul (@) operation

## 3 - Inheritance

1. Create a DiagonalMatrix that can be used like DiagonalMatrix(3,7) and returns a 3x3 matrix filled with 0 except the diagonal filled with 7

