import csv
import time

rows = [
    ['18.10.2020'],
    ['19.10.2020'],
    ['20.10.2020'],
    ['21.10.2020'],
    ['22.10.2020'],
    ['23.10.2020'],
    ['24.10.2020'],
    ['25.10.2020'],
    ['26.10.2020'],
]

filename = "data.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(rows)

csv_rows = []
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        csv_rows.append(*row)

    csv_rows = csv_rows[len(csv_rows) - 7:]
    lst = [time.strptime(i, '%d.%m.%Y') for i in csv_rows]
    print(time.strftime('%d.%m.%Y', min(lst)))
