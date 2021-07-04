import hashlib
char=input("Enter the character to be hasded by MD5 method:")
hchar=hashlib.md5(char.encode())
print("The hasded equivalent of input is : ", end ="")
print(hchar.digest())