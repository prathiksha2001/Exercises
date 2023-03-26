
#control flow with modulus in list comprehension
res = [ d**3 for d in range(20) if d > 10 and d % 2 == 0]
print(res)

# Create two nested list comprehensions inside a dictionary

d2 = { 'k1': [g + 20*g for g in range(10) if g < 5], 'k2': [g*g for g in range(20) if g < 10] }
print(d2)

d3 = {'k3' : [sum(d2['k1']) + sum(d2['k2'])]}

print(d3)