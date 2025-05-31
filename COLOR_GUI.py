from tkinter import *

class MyButton:
	def __init__(self,root):
		self.f=Frame(root,height=400,width=500)
		self.f.propagate(0)
		self.f.pack()

		self.b1=Button(self.f,text='Red', width=15,height=2,command=lambda:self.buttonClick('Red'))

		self.b2=Button(self.f,text='Green',width=15,height=2,command=lambda:self.buttonClick('Green'))

		self.b3=Button(self.f,text='Blue',width=15,height=2,command=lambda:self.buttonClick('Blue'))

		self.b1.pack()
		self.b2.pack()
		self.b3.pack()
	def buttonClick(self,color):
		self.f.config(bg=color)
		print(f"You have click the {color} button")

root=Tk()
root.title("Color_GUI")
mb=MyButton(root)
root.mainloop()