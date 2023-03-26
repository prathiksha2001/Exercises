import requests


#r = requests.get('https://imgs.xkcd.com/comics/python.png')
# r = requests.get('https://images.pexels.com/photos/863963/pexels-photo-863963.jpeg')
# with open('flower.jpeg','wb') as f:
#     f.write(r.content)

# r = requests.get("http://webcache.googleusercontent.com/search?q=cache:edureka.co")
# print(r.content)
# print(r.text)
#get method
#payload = {'page':2, 'count':25}
#r = requests.get('https://httpbin.org/get', params=payload)

#post method
payload = {'username':'prathiksha', 'password':'something'}
r = requests.post('https://httpbin.org/post', data=payload)
# print(r)

r_dict  = r.json()
# print(r_dict)
print(r_dict['form'])
# with open("comic.png", "wb") as f:
#     f.write(r.content)

# basic authentication 
# r = requests.get('https://httpbin.org/basic-auth/prathiksha/something', auth=('prathiksha','something'))
# print(r.text)
# print(r.headers)
