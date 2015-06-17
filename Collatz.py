#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_singleval
# ------------

# def collatz_singleeval (i) :
#     """
#     i the beginning of the range, inclusive
#     j the end       of the range, inclusive
#     return the max cycle length of the range [i, j]
#     """
#     # <your code>
#     return 1

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # <your code>

    # if i greater than j, switch
    if i > j:
        i, j = j, i

    max_length = 1

    for a in range(i, j+1):
        cycle_length = 1

        while (a > 1):
            if (a % 2 == 1):
                a = a + (a//2) + 1
                cycle_length += 2

            else:
                a = a // 2
                cycle_length += 1

        if cycle_length > max_length:
            max_length = cycle_length



    return max_length



    

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)
