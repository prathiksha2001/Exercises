import pickle

# address = {'city': 'Bangalore', 'state': 'Karnataka'}
# details = {'name': 'ben', 'age': 10}

# Bio_data = {}
# Bio_data['datails'] = details
# Bio_data['address'] = address

# with open('pickle_output.txt','ab') as f:
#     pickle.dump(Bio_data, f)

# with open('pickle_output.txt', 'rb') as f:
#     content = pickle.load(f)
#     print(content)

ls1 = ['apple','orange','kiwi','banana']
ls2 = ['tomato','lemon','carrot']

ls3 = [ls1,ls2]

with open('pickle_output_2.txt','wb') as f:
    pickle.dump(ls3,f)

with open('pickle_output_2.txt','rb') as f:
    print(pickle.load(f))