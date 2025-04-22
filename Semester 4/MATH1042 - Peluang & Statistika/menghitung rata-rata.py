year1 = [105, 141, 188, 190, 200, 210, 223, 241, 241, 247, 300, 306, 359, 380, 435, 494, 880, 882, 940, 940]
year2 = [20, 20, 20, 58, 60, 65, 70, 85, 95, 140, 160, 175, 200, 217, 220, 223, 235, 360, 380, 400]

avg1 = sum(year1) / 20
avg2 = sum(year2) / 20
# print(sum(year1))
print(avg1)
print(avg2)
x1 = 395.1
x2 = 160.15

deviasi1 = []
for a in year1:
    result = (a - x1) ** 2
    deviasi1.append(result)

deviasi2 = []
for a in year2:
    result = (a - x2) ** 2
    deviasi2.append(result)

standar_deviasi1 = (sum(deviasi1) / 20) ** 0.5
print(sum(deviasi1))
standar_deviasi2 = (sum(deviasi2) / 20) ** 0.5
print(sum(deviasi2) / 20)
print("==================")
print(standar_deviasi1)
print(standar_deviasi2)

print((26/36)**8)