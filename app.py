import csv
from PersonFile import PersonFile

filename = 'Persons.csv'
persons = []  # Tühi list
line = 0

if __name__ == '__main__':
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if line > 0:
                persons.append(PersonFile(row[0], row[1], row[2]))

            line += 1

    #print(persons)  # Objektid listis ei paista ilusad
    print(len(persons))  # Listi suurus (2004 isikut)
    print(persons[0].first_name)  # Esimese isiku eesnimi
    print(persons[len(persons)-1].last_name)  # Viimase isiku perenimi
    print(persons[1].__str__())  # Teise isiku kogu info
    line = 1
    for person in persons:
        #print(str(line) + '. ' + person.__str__())  # Õpsi variant
        line += 1
        print(f'{line}. {person.__str__()}')  # Raido variant
        #print(f'{line:04}. {person.__str__()}')  # Raido variant. Paneb ette kolm nulli.