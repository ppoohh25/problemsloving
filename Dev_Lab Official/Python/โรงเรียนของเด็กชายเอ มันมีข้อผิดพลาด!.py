score = int(input())
if score < 0 :
  print("Error : Value must be greater than or equal to 0.")
if score > 100 :
  print ("Error : Value must be less than or equal to 100.")
if score <= 50 and score >= 0 :
  print ("F")
if score > 80 and score <= 100 :
  print("A")