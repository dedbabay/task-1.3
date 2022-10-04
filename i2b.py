def d2b ( d ) :
    i = 0
    r = ''
    while d > 0 : 
        r = (str) (d % 2) + r
        d = d // 2
        i += 1
    return r

def b2d ( b ) :
    i = len ( b )
    r = 0
    while i > 0 :
        offset = len ( b ) - i
        if b[i-1] == '1' :
            r += 2 ** offset
        i -= 1
    return r

print ('Введите числа в двоичном виде X1 и X2, я перемножу их и выведу результат в двоичном виде')
print ('input X1')
x1 = input()
print ('input X2')
x2 = input()

y = b2d(x1) * b2d(x2)
print ('result: ', d2b(y))

