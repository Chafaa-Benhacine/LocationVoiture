# premier pas avec python

import tkinter as tk

racine = tk.Tk()
label = tk.Label(racine, text = "J'adore Python !")
bouton = tk.Button(racine, text="Quitter", command=racine.quit)
bouton["fg"] = "red"
label.pack()
bouton.pack()
racine.mainloop()
print("C'est fini !, je vous remercie !")



