expected_usr = "Florina"
expected_password = "abcd"
exepected_sold = "1000"
user = input("enter user ")
password = input("password ")
sold = input("expected sold ")
expected_seconduser = "diana"
# TODO Comparatie pentru  password si sold date de la  tastatura, consola definire test case-uri figuri geometrice
assert user == expected_usr
assert password == expected_password
assert sold == exepected_sold
seconduser =input("seconduser")
assert seconduser == expected_seconduser
print("The password for Florina" (len(password)))