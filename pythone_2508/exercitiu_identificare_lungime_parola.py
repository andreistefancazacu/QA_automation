'''
Tema identificare lungime parola
'''

EXPECTED_USER = "andrei"
EXPECTED_PASSWORD = "*********"

user = input('enter password')
password = input('enter password')

assert user == EXPECTED_USER
assert password == EXPECTED_PASSWORD

print('Hello Andrei your password ' + password + ' is ' + str(len(password)) + ' character long')


