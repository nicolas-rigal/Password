########################################################################
# je fais renseigne le mdp 
# puis temps que le mdp n'est pas valide je boucle dessus en affichant quil n'est pas valide. 
# pui si il est valide je verifier si le user exciste 
#       si il exiciste je le rajoute a sont profil sinon je le crée 
######################################################################## 
import string, hashlib, json
#import des librairie preinplementer a python ou directement télécharger
#string = pour manipuler les chaines de caractere
#haslib = fonction de hachage sha256 mauvais pk dechifrable a cause matrice 
#json = gestionnaire de donnée equivalent sql like


#try 
try:
    with open("user-mdp.json", "r") as f:
        repertoire_user_mdp = json.load(f)

except:
    repertoire_user_mdp = {}
    
#----------------------------------------------------------#
#                   pack des fonctions                     #
#----------------------------------------------------------#
# fonction de verification et gestion des erreur
def verif_mdp(mdp):
    
    while True:
        lettre_en_miniscule = 0
        lettre_en_miniscule = 0
        caractere_numérique = 0
        chiffres = 0
        caractere_speciaux = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~."
#longeur 
        if len(mdp) >= 8:
#majuscule 
            for x in string.ascii_uppercase:
                if x in mdp :
                    lettre_en_miniscule += 1   
#minuscule 
            for i in string.ascii_lowercase:
                if i in mdp :
                    lettre_en_miniscule += 1          
#numbre  
            for y in string.digits:
                if y in mdp :
                    chiffres += 1
#spéciale 
            for z in caractere_speciaux:
                if z in mdp :
                    caractere_numérique += 1            
#gestion de la reussite 🎉🎉🎉
            if lettre_en_miniscule > 0 and lettre_en_miniscule > 0 and caractere_numérique > 0 and chiffres > 0:
                return "Valide"
#gestion erreur caractere manquant         
            else:
                return "Le mot de pass renseigner n'est pas valide ."
#gestion erreur longeur
        else:
            return "Le mot de pass renseigner n'est pas assez long il doit être superieur à 10 caractére ."

#initialisationde ma boucle de saisi d'un mot de pass et verification--
#temps le mot de passe n'est pas valide je boucle dessus 
#sinon je print que tous est ok je le dit 
def saisi_mdp():
    while True:
        mdp = input("Veuillez saisir un mot de passe contenant(une majuscule, une minuscule, un chiffre et un caractère spécial :")
        verif = verif_mdp(mdp)
        if verif != "Valide":
            print(verif)
        else:
            print("Le mot de pass renseigner est valide 👍")
            crypte = hashlib.sha256(mdp.encode()).hexdigest()
            return crypte

#----------------------------------------------------------#
#              recuperation nom du user                    #
#       rapelle de la fontion de veriffication             #
#     et verification/ajout dans le dossier json           #
#----------------------------------------------------------#
#interaction avec l'utilisateur et ces consequence🐱‍🐉 1 je verifie si le nom existe et que mdp est different 
nom = input("Veuillez renseigner votre nom d'utilisateur : ")
mot_de_passe = saisi_mdp()
if nom in repertoire_user_mdp:
    if mot_de_passe in repertoire_user_mdp[nom]:
        print("Mot de passe déjà existants !")
    elif mot_de_passe not in repertoire_user_mdp[nom]:
        repertoire_user_mdp[nom] += [mot_de_passe]
        print("Mot de passe ajouté avec succès")
else: 
    repertoire_user_mdp[nom] = [mot_de_passe]
    print("Mot de passe ajouté au fichier historique")
    
#----------------------------------------------------------#
#   demande si on doit retournée tous le dossier du user   #
#----------------------------------------------------------#
affich_mot_de_passe = input("Souhaitez-vous afficher l'ensemble de vos mots de passe ? (oui ou non) ")
if affich_mot_de_passe.lower() ==  "oui":
    print(repertoire_user_mdp[nom])

with open("user-mdp.json", "w") as f:
    json.dump(repertoire_user_mdp, f, separators=(",", " : "), indent=5)