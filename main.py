import string
import random
s1=string.ascii_letters
s2=string.ascii_lowercase
s3=string.ascii_uppercase
s4=string.digits
s5=string.punctuation
plen=int(input("Enter the length of password"))
s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
s.extend(list(s5))
random.shuffle(s)
print("".join(s[0:plen]))
