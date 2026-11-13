students = {
    'Alice': {
        'Mathematiques': 90,
        'Francais': 80,
        'Histoire': 95
    },
    'Bob': {
        'Mathematiques': 75,
        'Francais': 85,
        'Histoire': 70
    },
    'Charlie': {
        'Mathematiques': 88,
        'Francais': 92,
        'Histoire': 78
    }
}

name = input("Entrez le nom de l’étudiant : ")

if name in students:
    print(f"Notes de {name} : ")
    total = 0
    for subject in students[name]:
        grade = students[name][subject]
        print(f"{subject} : {grade}")
        total = total + grade
    average = total / len(students[name])
    print(f"Moyenne de {name} : {average}")
else:
    print(f"L'étudiant {name} n'existe pas dans la liste.")
