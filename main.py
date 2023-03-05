import os
from replit import db
import random
boucle = True
print("note : ce programme est en développement, il n'y a pas encore beaucoup de blagues, mais vous pouvez en proposer")
print("outil blagues")
print("")
print("que voulez-vous faire ?")
print("1 : regarder une blague")
print("2 : proposer une blague")
print("3 : modération")
option = input()
print("")
if option == "1":
  print("option 1")
  print("attention, les blagues peuvent être parfois vulgaires")
  print("appuyez sur une touche pour continuer")
  continuer = input()
  while boucle == True:
    liste_blague = db.prefix("bl :")
    blague_choisie = random.choice(liste_blague)
    blague_choisie = blague_choisie.removeprefix("bl : ")
    print(blague_choisie)
    print("voulez-vous en regarder une autre ? 1 = oui, 2 = non")
    option = input()
    print("")
    if option == "1":
      "nouvelle blague"
    else:
      break
elif option == "2":
  print("option 2")
  print("proposez votre blague, elle sera analysée puis ajoutée au programme. S'il vous plaît, ne spammez pas, proposer une seule fois suffit.")
  proposition = input()
  db["pr : " + proposition] = "proposition"
  print("votre blague a bien été envoyée, merci de votre participation")
elif option == "3":
  print("option 3")
  print("veuillez entrer le mot de passe")
  mdp = input()
  if mdp == os.environ['mdp']:
    print("mot de passe bon")
    while boucle == True:
      print("")
      print("que voulez-vous faire ?")
      print("1 : voir les propositions")
      print("2 : supprimer proposition / blague")
      print("3 : accepter proposition")
      print("4 : voir toutes les blagues disponibles")
      print("5 : ajouter une blague")
      option = input()
      print("")
      if option == "1":
        keys = db.prefix("pr : ")
        print(keys)
      elif option == "2":
        print("quelle proposition / blague voulez-vous supprimer ? veuillez entrer le nom exact sans les guillemets")
        option = input()
        print("")
        print("êtes vous vraiment sûr de vouloir supprimer la proposition '" + option +"' ? 1 = oui, 2 = non")
        option2 = input()
        if option2 == "1":
          del db[option]
          print("proposition '" + option + "' supprimée ")
        elif option2 == "2":
          print("action annulée")
        else:
          print("erreur")
          print("action annulée")
      elif option == "3":
        print(" quelle proposition voulez-vous accepter ? veuiller entrer le nom exact sans les guillemets. Note : le 'pr :' ne sera pas visible, ne mettez surtout pas une blague ayant pour préfixe bl")
        option = input()
        print("")
        print("êtes vous vraiment sûr de vouloir accepter la proposition '" + option +"' ? 1 = oui, 2 = non")
        option2 = input()
        if option2 == "1":
          blague = option
          del db[option]
          blague = blague.removeprefix("pr : ")
          blague = "bl : " + blague
          db[blague] = "blague acceptée"
          print(" proposition '" + option + "' acceptée, elle est maintenant visible par tous. ")
        elif option2 == "2":
          print("action annulée")
      elif option == "4":
        keys = db.keys()
        print(keys)
      elif option == "5":
        print("quelle blague voulez-vous ajouter ?")
        ajout_blague = input()
        print("êtes-vous vraiment sûr d'ajouter '" + ajout_blague + "' ? le préfixe 'bl' sera ajouté pour le différencier des propostions. 1 = oui, 2 = non")
        option2 = input()
        if option2 == "1":
          ajout_blague = "bl : " + ajout_blague
          db[ajout_blague] = "blague ajoutée"
          print("blague ajoutée")
        elif option2 == "2":
          print("action annulée")
      else:
        print("erreur")
else:
  print("erreur")