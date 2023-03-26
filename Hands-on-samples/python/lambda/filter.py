def odd(num):
    if num % 2 != 0:
        return num
    
print(list(filter(odd, [1,2,3,4,5,6,7,8,9])))

participant_list = [
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
]

print(sorted(participant_list, key=))