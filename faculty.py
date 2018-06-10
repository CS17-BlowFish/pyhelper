import csv
import os

faculty_ids = []
faculty_names = []
faculty_dateofbirths = []
faculty_phonenumbers = []
faculty_placeofbirths = []
data_rows = []


def main():
    with open('faculty.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            faculty_ids.append(line[0])
            faculty_names.append(line[1])
            faculty_dateofbirths.append(line[2])
            phone_number = line[3]
            print(phone_number)
            # phone_number = phone_number[1:len(phone_number) - 1]
            faculty_phonenumbers.append(phone_number)
            faculty_placeofbirths.append(line[4])

    for i in range(len(faculty_ids)):
        data_rows.append([faculty_ids[i], faculty_names[i],
                         faculty_dateofbirths[i],
                         faculty_phonenumbers[i],
                         faculty_placeofbirths[i]])

    with open('faculty-new.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        for row in data_rows:
            writer.writerow(row)


if __name__ == "__main__":
    main()