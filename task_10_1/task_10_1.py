import csv

fields = ['firstname', 'lastname', 'age']
rows = [
    ['Alex', 'Varkalov', '3'],
    ['Max', 'Ivanov', '45'],
    ['Ivan', 'Korolev', '90'],
    ['Max', 'Maximov', '12'],
    ['Ola', 'Olovich', '17'],
    ['Mlor', 'Mlorovich', '25'],
    ['Ola', 'Milevich', '34'],
    ['Kola', 'Kalevich', '23'],
    ['Solo', 'Versh', '15'],

]
filename = "people.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

csv_rows = []
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        csv_rows.append(row)

    lst = [int(i[2]) for i in csv_rows]
    ls11 = []
    ls12 = []
    ls13 = []
    ls14 = []
    ls15 = []

    for i in lst:
        if i in range(1, 13):
            ls11.append(i)
        elif i in range(13, 19):
            ls12.append(i)
        elif i in range(19, 26):
            ls13.append(i)
        elif i in range(26, 41):
            ls14.append(i)
        elif i > 40:
            ls15.append(i)


with open('final_file.txt', 'w') as new_file:
    new_file.write(f'Age 1-12: {len(ls11)}\n')
    new_file.write(f'Age 13-18: {len(ls12)}\n')
    new_file.write(f'Age 19-25: {len(ls13)}\n')
    new_file.write(f'Age 26-40: {len(ls14)}\n')
    new_file.write(f'Age 40+: {len(ls15)}')

