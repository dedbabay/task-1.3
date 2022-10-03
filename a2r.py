a = (int)(input())
print (a)

def a2r_r (c, r1, r5, r10) :
    if c == 4 : 
        return r1 + r5
    elif c == 9 :
        return r1 + r10
    elif c < 4 : 
        return (r1 * c)
    else :
        return r5 + ( r1 * (c - 5) )

r = ''

# 1000
n_t = a // 1000
r = r + 'M' * n_t
a = a - n_t * 1000

# 100
n_h = a // 100
r = r + a2r_r ( n_h, 'C', 'D', 'M')
a = a - n_h * 100

# 10
n_d = a // 10
r = r + a2r_r ( n_d, 'X', 'L', 'C')
a = a - n_d * 10

#1
r = r + a2r_r ( a, 'I', 'V', 'X')

print (r)