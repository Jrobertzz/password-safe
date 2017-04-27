#!/usr/bin/env python3
from PassSys import PassSys

ps = PassSys('u.txt')

ps.addUser('foobar0', 'password0')
ps.addUser('foobar1', 'password1')
ps.addUser('foobar2', 'password2')
ps.addUser('foobar3', 'password3')
ps.addUser('foobar4', 'password4')

users = ps.getUsers()
for u in users:
	print(u + '\n')

print('----------------')

ps.deleteUser('foobar2')

users = ps.getUsers()
for u in users:
	print(u + '\n')

print('----------------')

list = ps.getNames('foobar1', 'password1')
print(list)

print('----------------')

ps.addPassword('foobar4', 'password4', 'reddit4', 'mytree4')
ps.addPassword('foobar0', 'password0', 'sham0', 'mytree0')

ps.addPassword('foobar1', 'password1', 'reddit1', 'mytree1r')
ps.addPassword('foobar1', 'password1', 'sham1', 'mytree1s')

list = ps.getNames('foobar1', 'password1')

print(list)

print('----------------')

past = ps.getPassword('foobar0', 'password0', 'sham0')
past1 = ps.getPassword('foobar1', 'password1', 'sham1')
past2 = ps.getPassword('foobar4', 'password4', 'reddit4')

print(past)
print(past1)
print(past2)

print('----------------')

ps.deletePassword('foobar1', 'password1', 'sham1')
list = ps.getNames('foobar1', 'password1')
print(list)

