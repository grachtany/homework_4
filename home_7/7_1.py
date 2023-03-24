_list = [len([i for i in el if i.lower() in "уеёэоаыяию"]) for el in input().split()]
if all([i == _list[0] for i in _list]):
    print("Парам пам-пам")
else:
    print("Пам парам")