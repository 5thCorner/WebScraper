# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']
dct = dict()


n_of_g = int(input())
for i in range(n_of_g):
    dct.update({groups[i]: int(input())})
for j in range(len(groups) - n_of_g):
    dct.update({groups[n_of_g + j]: None})
print(dct)
