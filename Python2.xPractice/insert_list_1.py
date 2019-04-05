names = []

names.append("Frank")
names.append("Alexis")
names.append("Erika")
names.append("Ludmila")

print names
names.append("Mokter")
names.append("Mahdi")
names.append("Munim")
print names

names.insert(0, "Mosaddesk")

print names
names.insert(1, "Hossain")
print names
names.insert(2, "Mahdi")
print names
names.insert(3, "Muhaimin Hossain Munim")
print names
#del names[5]
print names
del names[5]
print names
print len(names)
print names.count("Mahdi")
print names.count("Mosaddek Hossain Munim")
print names.count("Muhaimin Hossain Munim")
print names.count("Rahima Mokter")
names.insert(0, "Kakakak ")
print names
y = names.sort()

print y


names.remove("Ludmila")
print names

print names.index("Mokter")
print names.index("Mahdi", 5, 8)

x = names.pop(4)

print "names.pop(4): ", x

