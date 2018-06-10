import csv
import os


# course_id, faculty_id, course_name, registered, slots
# course_id, course_code, course_name, faculty_id, semester_id, registered, slots


course_codes = []
course_names = []
faculty_ids = []
semester_ids = []
registered = []
slots = []
data_rows = []


def gen_id(i):
    res = chr(i + ord('0'))
    while len(res) < 6:
        res = '0' + res
    return res


def main():
    with open('course.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            course_codes.append(line[0])
            course_names.append(line[2])
            faculty_ids.append(line[1])
            semester_ids.append(172)
            registered.append(line[3])
            slots.append(line[4])

    for i in range(len(course_codes)):
        data_rows.append([gen_id(i), course_codes[i], course_names[i], faculty_ids[i], semester_ids[i], registered[i], slots[i]])

    if not os.path.isfile('course-new.csv'):
        with open('course-new.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            for row in data_rows:
                writer.writerow(row)


if __name__ == "__main__":
    main()