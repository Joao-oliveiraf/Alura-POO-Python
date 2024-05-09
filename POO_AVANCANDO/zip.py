username = ['João', 'Dude', 'Admin']
passwords = ('123456789', 'theman@', 'admin', 'onemoreinfo')

if len(username) < len(passwords):
    username.append(None)

elif len(username) > len(passwords):
    passwords.append(None)

myzip = zip(username, passwords)
match_logins = [i for i in myzip]
mydict = dict(zip(username, passwords))

print(mydict)
print(match_logins)

