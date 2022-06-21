dic = {'a': ['abc', 'cba']}
a = 'apple'
b = ['abc', 'cba']
for each in b:
    if each[0] not in dic:
        print('x')
    else:
        if each in dic[each[0]]:
            print(each)