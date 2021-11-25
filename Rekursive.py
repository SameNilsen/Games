def fakultet(tall):
    if tall==0:
        return 1
    else:
        return tall*fakultet(tall-1)

fakultet(5)


def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n+recursive_sum(n-1)

print(recursive_sum(5))


def merge_sum(liste):
    if len(liste) == 1:
        return liste[0]
    else:
        return merge_sum(liste[:int((len(liste)/2))])+merge_sum(liste[int(len(liste)/2):])
    
merge_sum([1, 2, 3, 4, 5, 6])
