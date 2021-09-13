"""
Learning List
"""
a = [1, 2, 3]
b = ["banane", "mere", "gutui"]
c = [4, "struguri", True]

print(a, b, c)
print(a[0], b[0], c[0])
print(a[-1], b[-1], c[-1])
# print(a[3])
print("doi", a[0:len(a)])
print(b.count("mere"))
c[-1]="portocale"
print(c)
print(sum(a))
a.clear()
print(a)
a.append(3)
print(a)