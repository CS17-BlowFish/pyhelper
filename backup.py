import os
import shutil


old_files = [
    'course.csv',
    'object.csv',
    'student.csv',
    'teacher.csv',
    'user.csv'
]

new_files =  [
    'course.csv',
    'score.csv',
    'student.csv',
    'faculty.csv',
    'user.csv'
]


def rename():
    for i in range(len(old_files)):
        file = old_files[i]
        name, extension = file.split('.')
        extension = '.' + extension
        new_name = name + '-old'
        if os.path.isfile(name + extension):
            os.rename(name + extension, new_name + extension)
        old_files[i] = new_name + extension


def backup():
    for i in range(len(old_files)):
        old_file = old_files[i]
        new_file = new_files[i]
        if not os.path.isfile(new_file):
            shutil.copyfile(old_file, new_file)


def main():
    rename()
    for file in old_files:
        print(file)
    backup()


if __name__ == "__main__":
    main()