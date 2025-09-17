Foundation task completed
stretch task completed
challenge task completed
bonus task completed
we can make a list and the elements in the list can be used as the key for value from another list or dicionary and evey thing inthe list or dict will be in value of the key for this we can use
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

res = dict.fromkeys(employees, defaults)
print(res)

# Individual data
print(res["Kelly"])
we can replace defaults with any one of the specified from default as res = dict.fromkeys(employees, defaults["designation"]) this can only be done if value are from dict
if we replace value dict with just a string it will be the value for all keys in new dict

res = dict(zip(employees, defaults)) {'Kelly': 'hi', 'Emma': 'hello'}

