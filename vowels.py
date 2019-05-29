ch=input()
ch=ch.lower()
c=["a","e","i","o","u"]
if(ch>='a' and ch<='z'):
 if ch in c:
  print("Vowel")
 else:
  print("Consonant")
else:
 print("Invalid")
