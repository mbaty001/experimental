from cmath import inf


l = [5000, 3,21,2,45,4365, 54]

max_one = -inf
max_two = -inf

for el in l:
    if el > max_one:
        max_two, max_one = max_one, el
    elif el > max_two:
        max_two = el

print(f"{max_one}, {max_two}")