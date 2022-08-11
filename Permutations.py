from itertools import permutations

# print(list(set(map(''.join, permutations(input())))))
# print(list(map(''.join, permutations("113"))))

def to_string(List):
    return ''.join(List)


# a - String
# l - Starting index of the string
# r - Ending index of the string.

def permute(a, l, r):
    if l == r:
        print(to_string(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]  # backtrack


# Driver program to test the above function
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n)
