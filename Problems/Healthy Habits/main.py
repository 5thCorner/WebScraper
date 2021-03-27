for i in range(len(walks)):
    if i == 0:
        res = walks[i]['distance']
    else:
        res += walks[i]['distance']
print(res // len(walks))
