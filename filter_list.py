def filter_list(l):
    # new_l = []
    # for i in l:
    #     if type(i) == int:
    #         new_l.append(i)
    #
    # return new_l
    # return [i for i in l if not isinstance(i, str)]
    return [i for i in l if type(i) == int]

l = [1,2,'aasf','1','123',123]
new_l = filter_list(l)
print(new_l)

