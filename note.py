j = []
l = []

def note_x_coeff(j):
    nombre_matiere = int(input("\nEntrer nombres des matieres: "))
    k = 0
    z = 0
    while z < nombre_matiere:
        s = 0
        n = int(input('Entrer nombre des devoirs dans ce matier: '))
        for i in range(n):
            note = float(input("Entrer une note: "))
            if(note < 0 or note > 20):
                print("Erreur de saisie !")
                break
            else:
                l.append(note)
                s = s + note
        moyen = s / n
        coef = int(input('Entrer le coefficiant: '))
        total = moyen * coef
    
        k += coef
        z = z + 1
        j.append(total)
    somme = 0
    for h in j:
        somme = h + somme
    moyenne_generale = somme / k
    return moyenne_generale


print(note_x_coeff(j))