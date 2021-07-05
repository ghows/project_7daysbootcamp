import hashlib
char=input("Enter the character to be hasded by MD5,sha224,sha1,sha516 method:")
char='a'+char
char=char+'b'
print(char)

#salting
#hased using md5
hchar=hashlib.md5(char.encode())
print("The hasded equivalent of input is : ", end ="")
print(hchar.digest())

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

#iteration
for i in range(4):
    hchar = hashlib.md5(char.encode())

print("The hasded equivalent of input is (iterated for using MD5) : ", end ="")
print(hchar.digest())