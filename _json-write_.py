import json
#writing a csv
x = { }
x['tom'] = {'name':'tom','address':'USA','phone':'+178585' }
x['bob'] ={ 'name' : 'bob','address':'LOSANGLES','phone':'+74522245'}
s=json.dumps(x)
with open("D://S16-PFSD/json.txt","w") as f:
    f.write(s)

#read a json file
f = open("D://S16-PFSD/json.txt","r")
s=f.read()
print(s)
