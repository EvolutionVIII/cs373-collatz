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

    # m = (e/2)+1, if b<m, then max_length(b,e) = max_length(m,e)
    # example from class
    if (i < (j//2 + 1)):
        i = (j//2 + 1)



    max_length = 1

    # adds cache optimization, when program computes cycle length for a number (a)
    # it is stored in cache 
    cache = {}

    for a in range(i, j+1):
        cycle_length = 1

        while (a > 1):
            # checks the cache to see if a is already calculated
            # if found, add it to the current cycle length and subtract 1 (b/c of initial cycle_length)
            if (a in cache):                
                cycle_length += cache[a] - 1
                break

            else:
                if (a % 2 == 1):
                    a = a + (a//2) + 1
                    cycle_length += 2

                else:
                    a = a // 2
                    cycle_length += 1

        cache [a] = cycle_length

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
