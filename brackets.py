print ('fапfsdfgвпsвя проверю на правильность расстановки скобок. Все скобки должны быть закрыты в блоках')
s = input()

valid = True
i = 1
l = len ( s )
while l > 1 :
    s = s.replace('()', '')
    s = s.replace('{}', '')
    s = s.replace('[]', '')
    if l == len ( s ) or i > 99:
        valid = False
        break
    l = len ( s )
    i += 1
if valid :
    print (i, 'valid!')
else:
    print (i, 'not valid!')

