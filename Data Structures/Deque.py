from collections import deque

d = [1, 2, 3, 4, 5]
q = deque(d)
print(q)

q.appendleft(6)
print(q)

q.pop()
print(q)