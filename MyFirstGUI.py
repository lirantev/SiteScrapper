from tkinter import *
from lxml import html
import requests


#def printMe():
	#answer.config(text="Liran")
	#inputUrl = url.get()
	#answer.config(text=inputUrl)
#	text.insert(INSERT,"hello, ")
#	text.insert(INSERT,"world")


def scapper():
	scrap =''
	text.config(state=NORMAL)
	text.delete(1.0,END)
	inputUrl = url.get()
	page = requests.get(inputUrl, verify=False)
	tree = html.fromstring(page.content)
	#images = tree.xpath('//img/@src')
	links = tree.xpath('//a/@href')
	if len(links) == 0:
		#print("no links found")
		text.insert(INSERT,'No links found')
	else:
		newlinks = list(set(links))
		newlinks.sort()
		for x in newlinks:
			#answer.config(text=x)
			scrap += x + "\n"
	text.insert(INSERT,scrap)
	text.config(state=DISABLED)

root = Tk()
#root.geometry("800x600")
root.resizable(0,0)
root.title('The main title')

frame_1 = Frame(root,bd=5)
label = Label(frame_1, text="Please enter URL to scrap: ", fg="green")
url = Entry(frame_1)
button = Button(frame_1, text="Scrap",command=scapper)
label.grid(row=0, column=0, sticky=W)
url.grid(row=0, column=1, ipadx= 40, sticky=W)
button.grid(row=0,column=2,padx = 10,sticky=W)
frame_1.grid(row=0,column=0,sticky=W)

frame_2 = Frame(root, takefocus=1,height=500,width=800)
frame_2.grid_propagate(0)
xscrollbar = Scrollbar(frame_2, orient=HORIZONTAL)
xscrollbar.grid(row=1, column=0, sticky=E+W)
yscrollbar = Scrollbar(frame_2)
yscrollbar.grid(row=0,column=1,sticky=N+S)
text = Text(frame_2,wrap=NONE, yscrollcommand=yscrollbar.set,height=30,width=95)
text.grid(row=0,column=0, sticky = N+E+S+W)
xscrollbar.config(command=text.xview)
yscrollbar.config(command=text.yview)
frame_2.grid(row=1, sticky = N+E+S+W)

root.mainloop()