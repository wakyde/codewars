def find_uniq1(arr):
    """寻找唯一值的思路一:
                1.首先将数组排序,得出唯一值的位置,位置在第一个或最后一个
                2.判断这个位置与其他任意位置是否相等(除了第一个和最后一个)
                3.如果相等,返回另外一个位置的值

                """
    arr1 = sorted(arr)
    if arr1[0] == arr1[1]:
        return arr1[len(arr) - 1]
    elif arr1[len(arr) - 1] == arr1[1]:
        return arr1[0]

def find_uniq2(arr):
    """寻找唯一值的思路二:
                    1.首先根据python的语法特性,set的去重性,得到两个值
                    2.判断这两个值在原来数组的个数
                    3.返回个数唯一的值
    """
    a, b = set(arr)
    return a if arr.count(a) == 1 else b

# unique_number = find_uniq(['abc', 'abc', 'ade', 'abc', 'abc'])
# print(unique_number)