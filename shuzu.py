#list
l = ['dsf', 'fd', 12, 'a']
l.append(20)
l.pop()
print(l)
print(l[-2])

#tuple
t = ('sddf', 'as', [12, 'df'])
t[2][1] = 43
print(t)

#dict
d = {'Michael':89, 'bobo':56}
d['yyp'] = 98
print('wf' in d)
print(d.get('bob'))
print(d)

#set
s = set(list(range(3)))
s.add(6)
s.remove(2)
print(s)