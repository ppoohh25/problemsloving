n300 = float(input())
n100 = float(input())
n50 = float(input())
n0 = float(input())
Accuracy = ((50 * n50) + (100 * n100) + (300 * n300)) / (300 * (n0 + n50 + n100 + n300))
percent = Accuracy*100
percent2 = "{:.2f}".format(percent)
print('{}%'.format(percent2))