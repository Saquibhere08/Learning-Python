Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Deleting a Data in the  Dictionary
schoolname={"KVN":01,"CJS":15,"KKV":100}
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
schoolname={"KVN":100,"CJS":15,"KKV":100}
scoolname
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    scoolname
NameError: name 'scoolname' is not defined. Did you mean: 'schoolname'?
schoolname
{'KVN': 100, 'CJS': 15, 'KKV': 100}
del schoolname["CJS"]
schoolname
{'KVN': 100, 'KKV': 100}
#Deleting the entire VAriable
del schoolname
schoolname
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    schoolname
NameError: name 'schoolname' is not defined
schoolname={"KVN":100,"CJS":15,"KKV":100}
schoolname
{'KVN': 100, 'CJS': 15, 'KKV': 100}
schoolname.pop("KKV")
100
#deleting an key value pair

schoolname
{'KVN': 100, 'CJS': 15}
schoolname.clear
<built-in method clear of dict object at 0x000001E6B4AEC840>
schoolname
{'KVN': 100, 'CJS': 15}
# item() it returns a list of tuples with each tuple containing one key and the corresponding one key-
schoolname.items()
dict_items([('KVN', 100), ('CJS', 15)])
#keys()
#it delivers an list of objects comparising keys in the dictionary
schoolname.keys()
dict_keys(['KVN', 'CJS'])
#values() - This methods returns a list comparising values in the dictionary
schoolname.values()
dict_values([100, 15])
