from tkinter import *
import random 

raiz = Tk()
raiz.title("Tic tac toe")
raiz.resizable(0,0)

frame = Frame(raiz)
frame.pack()
frame.config(bg = "#0da192")

turnoBandera = True

txtStatus = StringVar()

varBoton00 = StringVar()
varBoton01 = StringVar()
varBoton02 = StringVar()

varBoton10 = StringVar()
varBoton11 = StringVar()
varBoton12 = StringVar()

varBoton20 = StringVar()
varBoton21 = StringVar()
varBoton22 = StringVar()

#**************************************Turno**************************************#

def turno(nombreButton):

	txtStatus.set("")

	global turnoBandera

	if turnoBandera:

		if nombreButton.get() == "":
			pass

		else :
			txtStatus.set("Turno de X")
			raise Exception("Pauseo de programa") # Pausea el programa, hasta cuando el usuario vuelve a clickear una casilla valida


		txtStatus.set("")
		nombreButton.set("X")
		turnoBandera = False

	empateBandera = valEmp()

	if empateBandera != True:
		
		if turnoBandera == False:
	
			buttonRand = random.choice([varBoton00, varBoton01 , varBoton02 , varBoton10, varBoton11, varBoton12, varBoton20, varBoton21, varBoton22])

			if buttonRand.get() == "":
				pass

			else :
				while buttonRand.get() != "":
					buttonRand = random.choice([varBoton00, varBoton01 , varBoton02 , varBoton10, varBoton11, varBoton12, varBoton20, varBoton21, varBoton22])

			buttonRand.set("O")
			turnoBandera = True
	else :
		Limpiar()

	valWin()

#**************************************valWin**************************************#

def valWin():

		if varBoton00.get() == "X" and varBoton01.get() == "X" and varBoton02.get() == "X":
			txtStatus.set("¡ Ganaste Felicidades !")
			Limpiar()
		
		elif varBoton10.get() == "X" and varBoton11.get() == "X" and varBoton12.get() == "X":
			txtStatus.set("¡ Ganaste Felicidades !")
			Limpiar()

		elif varBoton20.get() == "X" and varBoton21.get() == "X" and varBoton22.get() == "X":
			txtStatus.set("¡ Ganaste Felicidades !")
			Limpiar()

		elif varBoton00.get() == "X" and varBoton10.get() == "X" and varBoton20.get() == "X":
			txtStatus.set("¡ Ganaste Felicidades !")
			Limpiar()

		elif varBoton01.get() == "X" and varBoton11.get() == "X" and varBoton21.get() == "X":
			txtStatus.set("¡ Ganaste Felicidades !")
			Limpiar()

		elif varBoton02.get() == "X" and varBoton12.get() == "X" and varBoton22.get() == "X":
			txtStatus.set("¡ Ganaste Felicidades !")
			Limpiar()

		elif varBoton00.get() == "X" and varBoton11.get() == "X" and varBoton22.get() == "X":
			txtStatus.set("¡ Ganaste Felicidades !")
			Limpiar()

		elif varBoton02.get() == "X" and varBoton11.get() == "X" and varBoton20.get() == "X":
			txtStatus.set("¡ Ganaste Felicidades !")
			Limpiar()


		if varBoton00.get() == "O" and varBoton01.get() == "O" and varBoton02.get() == "O":
			txtStatus.set("Perdiste, pero ¡ puedes volver a intentar !")
			Limpiar()
		
		elif varBoton10.get() == "O" and varBoton11.get() == "O" and varBoton12.get() == "O":
			txtStatus.set("Perdiste, pero ¡ puedes volver a intentar !")
			Limpiar()

		elif varBoton20.get() == "O" and varBoton21.get() == "O" and varBoton22.get() == "O":
			txtStatus.set("Perdiste, pero ¡ puedes volver a intentar !")
			Limpiar()

		elif varBoton00.get() == "O" and varBoton10.get() == "O" and varBoton20.get() == "O":
			txtStatus.set("Perdiste, pero ¡ puedes volver a intentar !")
			Limpiar()

		elif varBoton01.get() == "O" and varBoton11.get() == "O" and varBoton21.get() == "O":
			txtStatus.set("Perdiste, pero ¡ puedes volver a intentar !")
			Limpiar()

		elif varBoton02.get() == "O" and varBoton12.get() == "O" and varBoton22.get() == "O":
			txtStatus.set("Perdiste, pero ¡ puedes volver a intentar !")
			Limpiar()

		elif varBoton00.get() == "O" and varBoton11.get() == "O" and varBoton22.get() == "O":
			txtStatus.set("Perdiste, pero ¡ puedes volver a intentar !")
			Limpiar()

		elif varBoton02.get() == "O" and varBoton11.get() == "O" and varBoton20.get() == "O":
			txtStatus.set("Perdiste, pero ¡ puedes volver a intentar !")
			Limpiar()

#**************************************valEmp**************************************#

def valEmp():

	if varBoton00.get() != "" and varBoton01.get() != "" and varBoton02.get() != "" and varBoton10.get() != "" and varBoton11.get() != "" and varBoton12.get() != "" and varBoton20.get() != "" and varBoton21.get() != "" and varBoton22.get() != "":
		txtStatus.set("Empate,¡ vuelve a intentarlo !")
		Limpiar()
		return True

#**************************************Limpiar**************************************#

def Limpiar():
	turnoBandera = True
	varBoton00.set("")
	varBoton01.set("")
	varBoton02.set("")

	varBoton10.set("")
	varBoton11.set("")
	varBoton12.set("")

	varBoton20.set("")
	varBoton21.set("")
	varBoton22.set("")

#**************************************Fila0**************************************#

labelTurno = Label(frame, textvariable = txtStatus, bg = "#0da192", fg = "white", font = ("Roboto")).grid(row = 0, column = 1, padx = 10, pady = 10, columnspan = 2, sticky = "w")

#**************************************Fila1**************************************#

boton00 = Button(frame, bd = 0, textvariable = varBoton00, fg = "#f2ebd3", bg = "#14bdac", width = 7, height = 3, font = ("Roboto", 28), command = lambda: turno(varBoton00)).grid(row = 1, column = 0, padx = 5, pady = 5)

boton01 = Button(frame, bd = 0, textvariable = varBoton01, bg = "#14bdac", width = 7, fg = "#f2ebd3",height = 3, font = ("Roboto", 28), command = lambda: turno(varBoton01)).grid(row = 1, column = 1, padx = 5, pady = 5)

boton02 = Button(frame, bd = 0, textvariable = varBoton02, bg = "#14bdac", width = 7, fg = "#f2ebd3",height = 3, font = ("Roboto", 28), command = lambda: turno(varBoton02)).grid(row = 1, column = 2, padx = 5, pady = 5)

#**************************************Fila2**************************************#

boton10 = Button(frame, bd = 0, textvariable = varBoton10, bg = "#14bdac", width = 7, fg = "#f2ebd3",height = 3, font = ("Roboto", 28), command = lambda: turno(varBoton10)).grid(row = 2, column = 0, padx = 5, pady = 5)

boton11 = Button(frame, bd = 0, textvariable = varBoton11, bg = "#14bdac", width = 7, fg = "#f2ebd3",height = 3, font = ("Roboto", 28), command = lambda: turno(varBoton11)).grid(row = 2, column = 1, padx = 5, pady = 5)

boton12 = Button(frame, bd = 0, textvariable = varBoton12, bg = "#14bdac", width = 7, fg = "#f2ebd3",height = 3, font = ("Roboto", 28), command = lambda: turno(varBoton12)).grid(row = 2, column = 2, padx = 5, pady = 5)

#**************************************Fila3**************************************#

boton20 = Button(frame, bd = 0, textvariable = varBoton20, bg = "#14bdac", width = 7, fg = "#f2ebd3",height = 3, font = ("Roboto", 28), command = lambda: turno(varBoton20)).grid(row = 3, column = 0, padx = 5, pady = 5)

boton21 = Button(frame, bd = 0, textvariable = varBoton21, bg = "#14bdac", width = 7, fg = "#f2ebd3",height = 3, font = ("Roboto", 28), command = lambda: turno(varBoton21)).grid(row = 3, column = 1, padx = 5, pady = 5)

boton22 = Button(frame, bd = 0, textvariable = varBoton22, bg = "#14bdac", width = 7, fg = "#f2ebd3",height = 3, font = ("Roboto", 28), command = lambda: turno(varBoton22)).grid(row = 3, column = 2, padx = 5, pady = 5)


#**************************************Colores**************************************#


raiz.mainloop()