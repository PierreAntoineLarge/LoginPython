import tkinter as tk


fenetre = tk.Tk()

fenetre.title("Ma premier")
etiquette = tk.Label(fenetre,text="Pseudo")
etiquette.pack()

champ_texte_nom = tk.Entry(fenetre)
champ_texte_nom.pack()

etiquette = tk.Label(fenetre,text="email")
etiquette.pack()

champ_texte_Password = tk.Entry(fenetre)
champ_texte_Password.pack()

etiquette = tk.Label(fenetre,text="Mot de passe")
etiquette.pack()

champ_texte_email = tk.Entry(fenetre)
champ_texte_email.pack()

def action_bouton():
    print(champ_texte_nom.get())
    print(champ_texte_email.get())
    print(champ_texte_Password.get())

bouton =  tk.Button(fenetre, text="Valider", command=action_bouton)
bouton.pack()

fenetre.geometry("400x300")

fenetre.mainloop()