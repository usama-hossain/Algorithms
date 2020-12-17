import random


def merge(X, Y):
    """merge two sorted lists"""
    p1 = p2 = 0
    out = []
    while p1 < len(X) and p2 < len(Y):
        if X[p1] < Y[p2]:
            out.append(X[p1])
            p1 = p1 + 1
        else:
            out.append(Y[p2])
            p2 = p2 + 1

    out = out + X[p1:] + Y[p2:]

    return out


def merge_sort(A):
    if len(A) <= 1:
        return A
    if len(A) == 2:
        return sorted(A)

    mid = int(len(A) / 2)
    return merge(merge_sort(A[:mid]), merge_sort(A[mid:]))


A = [random.randint(1, 100) for i in range(1, 21)]
print(merge_sort(A))
