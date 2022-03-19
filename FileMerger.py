"""
dev: Costea Adrian
description: Program de merge-uit fisiere java pentru labu-ul de programare
GitHub link:
"""
import os
import time


def main(folder_path, student_name, student_group, student_year, lab, ex, save_path):
    inputs = []

    #luam fisierele care se termina cu .java
    for file in os.listdir(folder_path):
        if file.endswith(".java"):
            inputs.append(os.path.join(folder_path, file))

    #prelucram numele studentului
    student_name.replace(' ', "_")

    #facem numele fisierului noi
    new_file_name = student_name + '_G' + student_group + '_An' + student_year + '_Lab' + lab + '_Ex' + ex

    #bagam path-ul in numele fisierului
    completeName = os.path.join(save_path, new_file_name+".txt")

    #concatenam fisierele din path-ul dat
    with open(completeName, 'w') as outfile:
        outfile.write('/*\n*************************' + '\n' + '*Student: ' + student_name + '\n' + '*Grupa: ' + student_group + '\n' + '*Anul: ' + student_year + '\n' + '*Laboratorul: ' + lab + '\n' + '*Exercitiul: ' + ex + '\n******************\n*\\\n');
        for fname in inputs:
            with open(fname, encoding="utf-8", errors='ignore') as infile:
                outfile.write("//" + os.path.basename(fname) + "\n")
                outfile.write(infile.read())
            outfile.write('/*********************************\n')


if __name__ == '__main__':
    print("Merge de fisiere pentru lab" + '\n' + "Locatia fisierelor (folderul src): ")
    folder_path = input()
    print("Numele tau: ")
    user_name = input()
    print("Grupa: ")
    grupa = input()
    print("Laboratorul: ")
    lab = input()
    print("Exercitiul: ")
    ex = input()
    print("Locatia unde vrei sa salvezi fisierul: ")
    out_path = input()

    main(folder_path, user_name, grupa, '2' , lab, ex, out_path)

    print("Merge realizat cu succes!")
    time.sleep(2000)
