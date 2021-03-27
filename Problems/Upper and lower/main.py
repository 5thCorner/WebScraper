some_iterable = input().split()
new_iterable = dict()
for i in range(len(some_iterable)):
    lst = {some_iterable[i].upper(): some_iterable[i].lower()}
    new_iterable.update(lst)
print(new_iterable)
