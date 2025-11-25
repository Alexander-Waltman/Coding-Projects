True = True
False = False


expected = 0
actual = neighbor_count([[False,False,False],
                         [False,False,False],
                         [False,False,False]]], 0, 2)
assert actual == expected, f"FAILED test 7: Top right corner cell with 0 neighbors. \n Expected {expected}.\nGot {actual}."

expected = 2
actual = neighbor_count([[False,False,False],
                         [True,True,False],
                         [False,False,False]]], 2, 0)
assert actual == expected, f"FAILED test 8: Bottom left corner cell with 2 neighbor N and NE. \n Expected {expected}.\nGot {actual}."

expected = 1
actual = neighbor_count([[False,False,False],
                         [False,False,False],
                         [False,True,False]]], 2, 2)
assert actual == expected, f"FAILED test 9: Bottom right corner cell with 1 neighbor W. \n Expected {expected}.\nGot {actual}."


T =True

[
[T,T,F,T,F],
[T,F,T,T,T],
[F,F,F,T,F],
[F,F,F,F,F],
[F,F,F,F,F],
]