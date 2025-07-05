import os
#Ajout commentaire sothy +1
"Ajout commentaire sothy +2"
print("************************")
print("  AGE   ")
print("*************************")
while True:
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        age = int(input("Quel âge avez-vous ? "))
        #try gestion d erreur, si une erreur ne pas planté
        
        if age <= 10:
            print("****** Vous êtes un enfant *******.")
        elif 11 <= age <= 17:
            print("*********** Vous êtes un adolescent*******.")
        elif 18 <= age <= 50:
            print("********* Vous êtes un adulte ************")
        else:
            print("************** Vous êtes âgé. ***********23")

    except ValueError:
        print("Veuillez entrer un nombre valide.")
        continue

    reponse = input("Voulez-vous quitter ? (O/N) ").strip().upper()
    
    if reponse == "O":
        print("Au revoir 👋")
        break
    elif reponse == "N":
        print("Très bien, on continue !")
    else:
        print("Réponse invalide. Veuillez taper 'O' ou 'N'.")