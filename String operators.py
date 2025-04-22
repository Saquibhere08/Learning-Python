# String Operators

# + Concatenation
a=' "Hello, ' #String a
b=' Saquib", ' #String b
print(a+b+ ' said Harry to Nearly Headless Nick.') #The = here appends the strings a and b to the string in quotes.

# * Repetition
c='I Must not tell lies...' #string c
print('Again and agian Harry wrote the words on the parchment in his own blood - ' +c*5)
#Here, The * joins or concatenates the strings a repeatedly for 5times

# []Slice
d='The Burrow' #string d
d[8] #here the index number in square brackets[] slices out the character at that index, which is o in this example

# [:] Range Slice
e='The Burrow' #string e
e[2:7]
#strarting index =2 = e, ending index =7-1 =r
e[:6]
#starting index = 5 = T , Ending index=6-1 =u

e[5:]
#Starting index = 5 =u, ending index = end of thestring =w


# in membership
f='Harry watched Dumbledore striding up and down in front of him, and thought. He thought of his mother,his Sirus. He thought of Cedric Diggory.'
#string f
'v' in f #checks if the charcter 'v' is present in the string, f
'dig' in f #checks if the characters 'digg' is present in the string, f
'Dig' in f # Note that this is case-sensitive.As 'Dig' is present in 'Diggory', This returns TRue.

#not in membership
g=''' "For Him?" shouted snape. "Expecto Patronum!"
From the tip of his wand burst the silver doe: She landed on the office floor, bounded once across
the office, and soared out of the window. Dumbledore watched her fly away, and as her silvery glow faded he turned
back to Snape, and his eyes were full of tears.
"After all this time?"
"Always," said snape.''' #Multi-line string, g
'v' not in g  #checks if the charcter 'v' is not present in the string,g 
'Red' not in g #checks if the charcter 'Red' is not present in the string,g
'red' not in g #This is case -sensitive checks if the charcter 'red' is not present in the string,g
