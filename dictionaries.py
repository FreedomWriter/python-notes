# DICTIONARY METHODS


user = {
  'basket': [1,2,3],
  'greet': 'hello'
}


# .get(key, default value)

print("\n  user = {\n  'basket': [1,2,3],\n  'greet': 'hello'\n  }\n")
print('  user["age"] ----> # throws an arrow as there is no key "age" in the user dictionary (errors interrupt execution)\n')
print(f"  print(user.get('age')) ----> # {user.get('age')}\n  print(user.get('greet')) ----> # {user.get('greet')} - .get() allows for checking whether a key exists in a dictionary without interruption execution, it will return the value or the default value, but it will not add a key that didn't exist to a dict")
print("\n# .get() also allows for providing a default value\n")
print(f"  print(user.get('age', 40)) ----> # {user.get('age', 40)}")
print(f"\n# if user had an 'age' key already, user.get('age', 40) would return the value of age in the dictionary, not the default value provided to .get()")
print("\n# .keys() - can be used on a dictionary to check if a key exists, returns a boolean\n")
print(f"  print('name' in user.keys()) ----> # {'name' in user.keys()}")
print(f"  print('basket' in user.keys()) ----> # {'basket' in user.keys()}")
print("\n# .values() - can be used on a dictionary to check if a value exists, returns a boolean\n")
print(f"  print('hello' in user.values()) ----> # {'hello' in user.values()}")
print(f"  print('goodbye' in user.values()) ----> # {'goodbye' in user.values()}")
new_user = dict(name='Natalie')
print("\n# using built in function dict()\n" )
print("  new_user = dict(key=value)")
print(f"  print(new_user) ----> # {new_user}")

print("\n# the `in` keyword can also be used to find keys in dictionaries\n")
print(f"  'name' in new_user ----> # {'name' in new_user}")
print(f"  'location' in new_user ----> # {'location' in new_user}")
print("\n# .items()\n")
print(f"  print(user.items() ----> # {user.items()}")
newest_user = new_user.copy()
print("\n# .clear()\n")
print("  new_user.clear()\n  print(new_user) ----> # {}")
print("\n# .copy()\n")
print("  newest_user = new_user.copy()\n  print(newest_user) ----> # {name: 'Natalie'}")
print("\n# .pop(key)\n")
print(f"  print(new_user.pop('name')) ----> # 'Natalie' - .pop() takes in a key, removes it, and returns the value of what got removed")
print("\n# .popitem()\n")
print(f"  print(new_user.popitem('name')) ----> # .popitem() removes SOME key, value pair and returns a tupple. Since dicts are not orderded, it cannot be predicted which one gets removed")
print("\n# .update({key, updated value})\n##  if a key that didn't exist gets passed to .update, it will update the object with the new key and value")
print("  newest_user.update({'last_name': 'Davis'})")
newest_user.update({'last_name': 'Davis'})
print(f"  print(newest_user) ----> # {newest_user}")


print('\n############################################################################################\n')