import hashlib
char=input("Enter the character to be hasded by sha224 method:")
#hashed using sha224
h1char=hashlib.sha224(char.encode())
print("The hasded equivalent of input is (sha224 method) : ", end ="")
print(h1char.digest())

#hashed using sha1
h2char=hashlib.sha1(char.encode())
print("The hasded equivalent of input is (sha1 method) : ", end ="")
print(h2char.digest())

#hashed using sha512
h3char=hashlib.sha512(char.encode())
print("The hasded equivalent of input is (sha512 method) : ", end ="")
print(h3char.digest())