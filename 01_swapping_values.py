# 1
# a = 10
# b = 20
# print('sebelum pertukaran')
# print(f'a={a}, b={b}')
# c = a
# a = b
# b = c
# print('setelah pertukaran')
# print(f'a={a}, b={b}')

# 2
# a, b = 10, 20
# a, b = b,a
# print(f'a={a}, b={b}')

# 3
a, b, c, d, e = 10, 20, 30, 40, 50
print('sebelum pertukaran')
print(f'a={a}, b={b}, c={c}, d={d}, e={e}')
a= a, b, c, d, e = c, e, d, a, b
print('setelah pertukaran')
print(f'a={a}, b={b}, c={c}, d={d}, e={e}')