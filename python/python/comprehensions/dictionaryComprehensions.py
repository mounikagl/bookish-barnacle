dict = {'a':1, 'b':2, 'c':3, 'd':4}
x = dict.keys()
# print(x)

y= dict.values()
print(y)

new_dict = {k:v*2 for (k,v) in dict.items()}
print(new_dict)

new_dict_keys = {k*2:v for (k,v) in dict.items()}
print(new_dict_keys)

# dict = {i:i**2 for i in range(10) if i%2==0}
# print(dict)

# Alternate to lambda functions

feh = {'temp1':10, 'temp2':20, 'temp3':30, 'temp4':40}

cel = list(map(lambda x: (float(5)/9)*(x-32),feh.values()))
cel_dict = dict(zip(feh.keys(),cel))

cel_dict = {k:(float(5)/9)*(v-32) for (k,v) in feh.items()}
print(cel_dict)


dict = {'a':1, 'b':2, 'c':3, 'd':4}

new_dict = {k:v for (k,v) in dict.items() if v>2}
print(new_dict)

dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7}

new_dict = {k:('Even num' if v%2==0 else 'Odd num') for (k,v) in dict.items()}
print(new_dict)

dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7}

new_dict = {k:v for (k,v) in dict.items() if v>3 if v%2==0}
print(new_dict)

# nested dictionary comprehension

dict = {'one':{'a':10}, 'two':{'b':20}, 'three':{'c':30}}

for (external_key, external_value) in dict.items():
    for(internal_key, internal_value) in external_value.items():
        external_value.update({internal_key: float(internal_value)})
dict.update({external_key:external_value})

print(dict)