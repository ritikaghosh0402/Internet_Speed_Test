from tkinter import *
from speedtest import Speedtest

def check_speed():
    speed_test = Speedtest()
    download = speed_test.download()
    upload = speed_test.upload()
    download_speed = round(download / (10**6), 2)
    upload_speed = round(upload / (10**6), 2)
    down_label.config(text= "Download Speed - " + str(download_speed) + "Mbps")
    up_label.config(text= "Upload Speed - " + str(upload_speed) + "Mbps")

root = Tk()
root.title("Internet Speed Test")
root.geometry("400x500")
root.resizable(False,False)
root.configure(bg="#1a212d")
Button = Button(root, text="Check the Speed", width=20, command=check_speed,background = '#2278CC')
Button.place(x=120,y=90)
down_label = Label(root,text="",width=25)
down_label.place(x=105,y=150)
up_label = Label(root,text="",width=25)
up_label.place(x=105,y=185)

root.mainloop()
