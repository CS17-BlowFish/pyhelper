import csv

user_ids = []
passwords = []
user_types = []
data_rows = []


def main():
    with open('user.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            user_ids.append(line[0])
            passwords.append(line[1])
            user_types.append(line[2])

    for i in range(len(user_ids)):
        if user_types[i] == "teacher":
            data_rows.append([user_ids[i],
                             passwords[i],
                             "faculty"])
        else:
            data_rows.append([user_ids[i],
                             passwords[i],
                             user_types[i]])            

    with open('user-new.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        for row in data_rows:
            writer.writerow(row)


if __name__ == "__main__":
    main()