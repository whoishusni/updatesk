import csv
def main():
    with open('ppnpn.csv', 'r') as csv_file:
        file_data = csv.reader(csv_file, delimiter=';')
        next(file_data)
        for names in file_data:
            print(names[0])

if __name__ == '__main__':
    main()