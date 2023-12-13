import customtkinter
from PIL import Image
from tkinter import filedialog
import pytesseract as tess

app = customtkinter.CTk()
app.geometry('500x400')
app.title("Text_Recognizer")

# creating a frame
frame =customtkinter.CTkFrame(app,corner_radius=20,border_width=2)
frame.pack(padx=20,pady=20,fill='both')

# text
txt=customtkinter.CTkLabel(frame,text="Extract text from image",font=('Arial',20))
txt.pack(pady=20)

# ADD IMAGE 
img= customtkinter.CTkImage(Image.open('galary.png'),size=(42,42))

# function to open img
def open_img():
    filename= filedialog.askopenfilename()
    img1=Image.open(filename)
    get_txt= tess.image_to_string(img1)
    # print(get_txt,"txt")
    txt_box.insert('0.0',get_txt) 
# button
btn = customtkinter.CTkButton(frame,text='Add image',text_color='#FFFFFF',corner_radius=8,image=img,width=200,height=30,font=('Arial',20),border_spacing=10,hover_color='#900C3F',compound='right',command=open_img)
btn.pack(padx=20,pady=20)

# #  ADD A PROGRESS BAR
# progress_bar=customtkinter.CTkProgressBar(frame)
# progress_bar.pack()
# progress_bar.set(0)

# # #  PROGRESS BAR txt
# progress_bar_txt=customtkinter.CTkLabel(frame,text='0%')
# progress_bar_txt.place(x=340,y=160)
# text box
txt_box= customtkinter.CTkTextbox(frame,font=('Arial',18),width=520,height=420,corner_radius=20)
txt_box.pack(pady=20,padx=20)

app.mainloop()