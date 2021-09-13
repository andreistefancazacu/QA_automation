"""
Dictionaries - (key:value)
"""

my_dict = {"a": "my data",
           "b": "hello",
           7: "Python",
           True: [0, 13, 2],
           "c": [dict(a=1, b="ciao"), dict(a=1, b="aloha"), dict(a=1, b="bonjour")]}

my_dict2 = dict(a=1, b="ciao")
print(my_dict["b"])
print(my_dict2["b"])
print(my_dict[True][1])

print(my_dict["c"][2]["b"])
print(my_dict.get(7))

print(my_dict)

print("---")
for k,v in my_dict.items():
    #print(k,v)
    if k == 7:
        print(v)
    elif k == "c":
        print(v)
    else:
        print("Key not found")