list1 = [10, 20, 30, 20, 20]

dup = []

# for i in list1:
#     if list1.count(i) > 1 and i not in dup:
#         dup.append(i)

# print(dup)
list2 = []
for i in list1:
    if list1.count(i) > 1:
        list1.remove(i)

print(list1)
#         dup.append(i)
# res = [i for i in list1 if i not in dup]
# print(res)
# print(set(list1))

# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('',''),()]
# for item in tuples:
#     if len(item) == 0:
#         tuples.remove(item)

# print(tuples)