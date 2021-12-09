score = int(input())
if score >= 90:
  print('A')
elif score >= 85 and score <= 89:
  print('B+')
elif score >= 80 and score <= 84:
  print('B')
elif score >= 75 and score <= 79:
  print('C+')
elif score >= 70 and score <= 74:
  print('C')
elif score >= 65 and score <= 69:
  print('D+')
elif score >= 60 and score <= 64:
  print('D')
elif score < 60:
  print('F')