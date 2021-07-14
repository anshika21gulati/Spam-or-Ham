import csv

reader = csv.reader(open("spam.csv", "rU"), delimiter=',')
writer = csv.writer(open("spam.txt", 'w'), delimiter=';')
writer.writerows(reader)

print("Delimiter successfully changed")
