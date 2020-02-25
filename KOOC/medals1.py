countries = [ "Australia", "Austria", "Belarus", "Canada",
              "China", "Croatia", "Czech Republic", "Estonia",
              "Finland", "France", "Germany", "Great Britain",
              "Italy", "Japan", "Kazakhstan", "Korea", "Latvia",
              "Netherlands", "Norway", "Poland", "Russian Federation",
              "Slovakia", "Slovenia", "Sweden", "Switzerland",
              "United States" ]

gold = [2, 4, 1, 14, 5, 0, 2, 0, 0, 2, 10, 1, 1,
        0, 0, 6, 0, 4, 9, 1, 3, 1, 0, 5, 6, 9]

silver = [1, 6, 1, 7, 2, 2, 0, 1, 1, 3, 13, 0, 1, 3, 1,
          6, 2, 1, 8, 3, 5, 1, 2, 2, 0, 15]

bronze = [0, 6, 1, 5, 4, 1, 4, 0, 4, 6, 7, 0, 3, 2, 0,
          2, 0, 3, 6, 2, 7, 1, 1, 4, 3, 13]

totals = []
for i in range(len(countries)):
    totals.append((gold[i], silver[i], bronze[i], countries[i]))

print(totals)
totals.sort()
print(totals)
top_ten = totals[-10:]
print(top_ten)
top_ten.reverse()
print(top_ten)

for g, s, b, country in top_ten:
    print(country, g, s, b)

l = []
l.append(1)
print(l)
l.append(5)
print(l)
l.insert(1, 3)
print(l)
print(l.pop())
print(l)
l.pop(0)
print(l)
l = [1, 3, 5, 7, 1, 3, 5, 1]
l.remove(1)
print(l)
print(l.index(7))
print(l.count(3))
l2 = [99, 99, 99]
l.extend(l2)
print(l)
l.reverse()
print(l)
l.sort()
print(l)

goldset = set(gold)
print(goldset)
print(type(goldset))