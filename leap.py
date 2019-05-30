year=int(input())
if(year%100==0):
 if(year%400):
  print("Leap year")
 else:
  print("No")
elif(year%4==0):
 print("Leap year")
else:
 print("No")
