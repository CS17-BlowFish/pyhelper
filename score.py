import csv
import os


# Course_id,Student_id,Teacher_id,Score,semeter_id
# course_id, student_id, score


course_ids = []
student_ids = []
scores = []
data_rows = []

def gen_id(i):
    res = chr(i + ord('0'))
    while len(res) < 6:
        res = '0' + res
    return res

def main():
    with open('score.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            # course_ids.append(line[0])
            student_ids.append(line[1])
            scores.append(line[3])

    for i in range(len(scores)):
        data_rows.append([gen_id(i), student_ids[i], scores[i]])

    # if not os.path.isfile('course-new.csv'):
    with open('score-new.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        for row in data_rows:
            writer.writerow(row)


if __name__ == "__main__":
    main()