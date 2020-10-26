import csv

fields = ['data', 'place', 'degrees', 'wind speed']
rows = [
    ['18.10.2020', 'Minsk', '20', '15'],
    ['19.10.2020', 'Minsk', '19', '10'],
    ['20.10.2020', 'Minsk', '15', '4'],
    ['21.10.2020', 'Minsk', '17', '6'],
    ['22.10.2020', 'Minsk', '13', '13'],
    ['23.10.2020', 'Minsk', '14', '3'],
    ['24.10.2020', 'Minsk', '16', '7'],
    ['25.10.2020', 'Minsk', '15', '4'],
    ['26.10.2020', 'Minsk', '13', '5'],
]

filename = "weather.csv"
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
    csv_rows = csv_rows[len(csv_rows)-7:]
    lst_degr = [int(i[2]) for i in csv_rows]
    lst_wind = [int(i[3]) for i in csv_rows]

    avg_derg = sum(lst_degr) / len(lst_degr)
    avg_wind = sum(lst_wind) / len(lst_wind)

print(f'avg degree: {round(avg_derg)}, avg wind speed: {round(avg_wind)}')