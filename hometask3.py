a = input('Назови свое имя и фамилию: ')
b, c = a.split(' ')

d = '!%s %s?' % (c.upper(), b.capitalize())
d_1 = '!{} {}?'.format(c.upper(), b.capitalize())
d_2 = f'!{c.upper()} {b.capitalize()}?'

my_file = open('hometask3.txt', 'w')
print(a, d, d_1, d_2, sep='<<<>>>', file=my_file)