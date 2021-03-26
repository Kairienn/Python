my_dict = {}
with open("my_file_6.txt", "r") as my_file:
    for l in my_file:
        subject_name, lecture, practice, lab = l.split()
        my_dict[subject_name] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество занятий - \n {my_dict}')
