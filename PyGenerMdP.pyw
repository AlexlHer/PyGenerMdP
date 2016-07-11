# -*- coding: utf-8 -*-
# Auteur : Alexandreou
print("----------------------------------------------------------------------")
print("PyGenerMdP v1.0")
print("----------------------------------------------------------------------")

from tkinter import *
import random

def alea_mdp():
	global mdp
	global plus1
	global plus
	global plus2
	global plus3
	global nb
	choix = []
	fin = ""
	minu = plus.get()
	maj = plus1.get()
	sym = plus2.get()
	chi = plus3.get()
	nb_selec = minu+maj+sym+chi
	if minu == 1:
		choix.append(1)
	if maj == 1:
		choix.append(2)
	if sym == 1:
		choix.append(3)
	if chi == 1:
		choix.append(4)
	liste_minu = ["a","z","e","r","t","y","u","i","o","p","q","s","d","f","g","h","j","k","l","m","w","x","c","v","b","n"]
	liste_maj = ["A","Z","E","R","T","Y","U","I","O","P","Q","S","D","F","G","H","J","K","L","M","W","X","C","V","B","N"]
	liste_chi = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
	liste_sym = ["&", "é", "'", '"', "(", "-", "è", "_", "ç", "à", ")", "=", "~", "#", "{", "[", "|", "`", "\\", "^", "@", "]", "}", "¨", "$", "£", "¤", "ù", "%", "*", "µ", ",", "?", ";", ".", ":", "/", "!", "§", "<", ">", "°", "+", "â", "ê", "î", "ô", "ñ", "ä", "ë", "ï", "ö", "A", "E", "I", "O", "Ñ", "Ä", "Ë", "Ï", "Ö"]
	for i in range(nb.get()):
		alea = random.choice(choix)
		if alea == 1:
			alea2 = random.choice(liste_minu)
			fin += alea2
		if alea == 2:
			alea2 = random.choice(liste_maj)
			fin += alea2
		if alea == 3:
			alea2 = random.choice(liste_sym)
			fin += alea2
		if alea == 4:
			alea2 = random.choice(liste_chi)
			fin += alea2
	mdp.set(fin)

def main():
	fenetre = Tk()
	fenetre.title("PyGenerMdP v1.0")
	plus = IntVar()
	plus1 = IntVar()
	plus2 = IntVar()
	plus3 = IntVar()
	nb = IntVar()
	mdp = StringVar()
	mdp.set("Mettre les caractères voulu et appuyer sur OK.")
	global mdp
	global plus1
	global plus
	global plus2
	global plus3
	global nb

	et_0 = Label(fenetre, text = "PyGenerMdP", font=('Arial', 20, 'italic', 'bold'))
	et_0.grid(row=0, column=0, columnspan=10)
	et_01 = Label(fenetre, text = "Mot de passe généré :")
	et_01.grid(row=1, column=0, columnspan=10)
	et_1 = Entry(fenetre, width=50, textvariable=mdp)
	et_1.grid(row=2, column=0, columnspan=10)
	et_2 = Checkbutton(fenetre, text = "Lettres minuscule", variable = plus)
	et_2.grid(row=3, column=0)
	et_3 = Checkbutton(fenetre, text = "Lettres majuscule", variable = plus1)
	et_3.grid(row=3, column=1)
	et_4 = Checkbutton(fenetre, text = "Symboles", variable = plus2)
	et_4.grid(row=4, column=0)
	et_5 = Checkbutton(fenetre, text = "Chiffres", variable = plus3)
	et_5.grid(row=4, column=1)
	et_6 = Label(fenetre, text = "Nb de caractères du mot de passe :")
	et_6.grid(row=5, column=0)
	et_7 = Entry(fenetre, width=20, textvariable=nb)
	et_7.grid(row=5, column=1)
	et_8 = Button(fenetre, text = "OK", command=alea_mdp)
	et_8.grid(row=6, column=1, columnspan=2)
	fenetre.mainloop()
main()

"""
Changelog :

v1.1 :
Correction temporaire d'un bug de fermeture 
(le 2eme thread ne se fermai pas, maintenant, 
il plante lorsque l'on quitte le logiciel, et donc se ferme).

v1.0 :
Ajout d'un pourcentage avec le module threading.
Outil de cryptage amélioré.
Rapidité accru.
Ajout du support du jpeg.
Interface complétée.
Erreurs corrigées.
Programme renommé en PyCryptImage ou PyCI.

v0.5 :
Code fonctionnel, basé sur l'exercice "cache_image".
"""