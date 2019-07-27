import tkinter
mtrx  = [[-1,-2,-3],[-5,-6,-7],[-8,-9,-10]]
cntr = 0

def row():
	global mtrx
	for i in range(3):
		if(mtrx[i][0] == mtrx[i][1] and mtrx[i][1] == mtrx[i][2]):
			return True
	return False

def colum():
	global mtrx
	for i in range(3):
		if(mtrx[0][i] == mtrx[1][i] and mtrx[1][i] == mtrx[2][i]):
			return True
	return False
	
def diag():
	global mtrx
	if(mtrx[0][0]==mtrx[1][1] and mtrx[1][1]==mtrx[2][2]):
		return True
	return false

def checkwin(b,r,c):
	global cntr
	if cntr%2 == 0:
		b.config(text="X",state="disabled")
		mtrx[r][c] = 1
	else:
		b.config(text="O",state="disabled")
		mtrx[r][c] = 0
	cntr += 1

	if(row()==1 or colum()==1 or diag==1 ):
		print("win")
		exit(0)


main_windows = tkinter.Tk()
main_windows.geometry("210x210")
main_windows.resizable(width=False, height=False)
main_windows.title("[ TIC TAC ]")


b1 = tkinter.Button(main_windows,borderwidth=1,height=3,width=6,command = lambda : checkwin(b1,0,0))
b1.place(x=0,y=0)
b2 = tkinter.Button(main_windows,borderwidth=1,height=3,width=6,command = lambda : checkwin(b2,0,1))
b2.place(x=75,y=0)
b3 = tkinter.Button(main_windows,borderwidth=1,height=3,width=6,command = lambda : checkwin(b3,0,2))
b3.place(x=150,y=0)
b4 = tkinter.Button(main_windows,borderwidth=1,height=3,width=6,command = lambda : checkwin(b4,1,0))
b4.place(x=0,y=75)
b5 = tkinter.Button(main_windows,borderwidth=1,height=3,width=6,command = lambda : checkwin(b5,1,1))
b5.place(x=75,y=75)
b6 = tkinter.Button(main_windows,borderwidth=1,height=3,width=6,command = lambda : checkwin(b6,1,2))
b6.place(x=150,y=75)
b7 = tkinter.Button(main_windows,borderwidth=1,height=3,width=6,command = lambda : checkwin(b7,2,0))
b7.place(x=0,y=150)
b8 = tkinter.Button(main_windows,borderwidth=1,height=3,width=6,command = lambda : checkwin(b8,2,1))
b8.place(x=75,y=150)
b9 = tkinter.Button(main_windows,borderwidth=1,height=3,width=6,command = lambda : checkwin(b9,2,2))
b9.place(x=150,y=150)
main_windows.mainloop()