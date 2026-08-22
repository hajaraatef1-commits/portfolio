import json

fichier = "equipements.json"


# =========================
# CHARGER LES ÉQUIPEMENTS
# =========================

def charger_equipements():
    try:
        with open(fichier, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


# =========================
# SAUVEGARDER
# =========================

def sauvegarder_equipements(equipements):
    with open(fichier, "w") as file:
        json.dump(equipements, file, indent=4)


# =========================
# AJOUTER
# =========================

def ajouter_equipement(equipements):

    print("\n===== AJOUTER UN ÉQUIPEMENT =====")

    nom = input("Nom de l'équipement : ")
    type_equipement = input("Type : ")
    numero = input("Numéro : ")
    etat = input("État : ")

    equipement = {
        "nom": nom,
        "type": type_equipement,
        "numero": numero,
        "etat": etat
    }

    equipements.append(equipement)

    sauvegarder_equipements(equipements)

    print("\nÉquipement ajouté avec succès !")


# =========================
# AFFICHER
# =========================

def afficher_equipements(equipements):

    print("\n===== LISTE DES ÉQUIPEMENTS =====")

    if len(equipements) == 0:
        print("Aucun équipement disponible.")
        return

    for i, equipement in enumerate(equipements, start=1):

        print("\nÉquipement", i)

        print("Nom :", equipement["nom"])
        print("Type :", equipement["type"])
        print("Numéro :", equipement["numero"])
        print("État :", equipement["etat"])


# =========================
# RECHERCHER
# =========================

def rechercher_equipement(equipements):

    print("\n===== RECHERCHE =====")

    recherche = input("Donner le nom de l'équipement : ")

    trouve = False

    for equipement in equipements:

        if recherche.lower() in equipement["nom"].lower():

            print("\nÉquipement trouvé :")

            print("Nom :", equipement["nom"])
            print("Type :", equipement["type"])
            print("Numéro :", equipement["numero"])
            print("État :", equipement["etat"])

            trouve = True

    if not trouve:
        print("Aucun équipement trouvé.")


# =========================
# MODIFIER
# =========================

def modifier_equipement(equipements):

    print("\n===== MODIFIER =====")

    numero = input("Donner le numéro de l'équipement : ")

    for equipement in equipements:

        if equipement["numero"] == numero:

            print("Équipement trouvé.")

            equipement["nom"] = input("Nouveau nom : ")
            equipement["type"] = input("Nouveau type : ")
            equipement["etat"] = input("Nouvel état : ")

            sauvegarder_equipements(equipements)

            print("Équipement modifié avec succès.")

            return

    print("Équipement introuvable.")


# =========================
# SUPPRIMER
# =========================

def supprimer_equipement(equipements):

    print("\n===== SUPPRIMER =====")

    numero = input("Donner le numéro de l'équipement : ")

    for equipement in equipements:

        if equipement["numero"] == numero:

            equipements.remove(equipement)

            sauvegarder_equipements(equipements)

            print("Équipement supprimé avec succès.")

            return

    print("Équipement introuvable.")


# =========================
# PROGRAMME PRINCIPAL
# =========================

equipements = charger_equipements()


while True:

    print("\n")
    print("==============================")
    print("   GESTION DES ÉQUIPEMENTS")
    print("==============================")

    print("1. Ajouter un équipement")
    print("2. Afficher les équipements")
    print("3. Rechercher un équipement")
    print("4. Modifier un équipement")
    print("5. Supprimer un équipement")
    print("6. Quitter")

    choix = input("\nVotre choix : ")

    if choix == "1":

        ajouter_equipement(equipements)

    elif choix == "2":

        afficher_equipements(equipements)

    elif choix == "3":

        rechercher_equipement(equipements)

    elif choix == "4":

        modifier_equipement(equipements)

    elif choix == "5":

        supprimer_equipement(equipements)

    elif choix == "6":

        print("Programme terminé.")

        break

    else:

        print("Choix invalide.")