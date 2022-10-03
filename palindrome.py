s = input()
s = s.replace(' ', '')

l = len ( s )
lc = len(s) // 2

is_p = True
i = 0
while i < lc:
    if s[i] != s[l - i - 1] :
        is_p = False
        break
    i = i + 1
if is_p:
    print ( "true" )
else:
    print ( "false" )
    
    