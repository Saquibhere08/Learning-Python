Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Formattting specifications symbols
#%c - Character
print("The letter that comes after d is %c" %('e',))
The letter that comes after d is e
#%d and %i - signed decimal integer
match=12553
site='e-Bay'
print("%s is so useless. I tried to look up lighters and they had was %d matches." %(site,match))
e-Bay is so useless. I tried to look up lighters and they had was 12553 matches.
#%u - unsigned decimal integer - %u is an obsolete type and is identical to %d
# %o - octal integer
print("83 is repr3esented in octal; as %o" %(0o123,))
83 is repr3esented in octal; as 123
# %x - hexadecimal integer
print("83 is represented in hexadecimal as %x" %(0*53,))
83 is represented in hexadecimal as 0
print("83 is represented in hexadecimal as %x" %(0X53,))
83 is represented in hexadecimal as 53
