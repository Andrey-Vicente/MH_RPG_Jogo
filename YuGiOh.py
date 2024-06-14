from tkinter import *

jan = Tk()
jan.title("YuGiOh Card Game")
jan.geometry("700x650+250+0")                   
#repetição de codigo, sera que da pra fazer uma função?
#função(text) - para os de texto
#função(variavel, linha, coluna) - posição - so em uma talvez de na função de cima

#fonte "Century Gothic"
fb = "Century Gothic"

#Linha de texto
nomel = Label(jan, text = "Nome: ", font=(fb, 16) )
nomel.grid(row=0, column=0)

#Entrada de dados
nomecard = Entry(jan, width=30)
nomecard.grid(row=0, column=1)


imageml = Label(jan, text="Imagem:", font=(fb, 16))
imageml.grid(row=1, column=0)

imagemb = Button(jan, text="Escolher", font=(fb, 16), bg="white", fg="black")
imagemb.grid(row=1, column=1)
#Linha de texto
tipo = Label(jan, text="Tipo", font=(fb, 16, "bold")) 
tipo.grid(row=2, column=0)

#caixa que gira? [to] e o maximo 
tipoe = Spinbox(jan, values=("Monstro", "Magica", "Armadilha"), to=3, width=10, bg="blue", buttonbackground="red", fg="white" ) 
tipoe.grid(row=2, column=1)










jan.mainloop()