import bisect
L = [10, 20, 30, 50, 60, 70, 90]

# Inserting inbetween
bisect.insort(L, 25)
print(L)

# Insert an existing number to the right
bisect.insort_left(L, 90)
print(L)

# Inserting element with bisect.bisect
print(bisect.bisect(L, 5))
