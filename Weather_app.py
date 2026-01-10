from customtkinter import *
import requests
# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
# 5dc0e98469b82ca39646f0774b9d94f2
# https://api.weatherapi.com/v1/current.json?key=c2b24258866c4c22894145857251111&q={city}&aqi=no

def get_data():
    city = city_name.get()
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=5dc0e98469b82ca39646f0774b9d94f2").json()
    w_label1.configure(text=data["weather"][0]['main'])
    wd_label.configure(text=data['weather'][0]["description"],width=50)
    wd_label.place(x=295)
    temp_label1.configure(text=str(data['main']['temp']-273.15))
    pre_label1.configure(text=data['main']["pressure"])

root = CTk()
root.title('Weather App')
root.geometry('500x500')
root.resizable(False,False)
root._set_appearance_mode('dark')
list_name = [
    "Balochistan",
    "Khyber Pakhtunkhwa",
    "Punjab",
    "Sindh",
    "Gilgit-Baltistan",
    "Azad Jammu and Kashmir",
    "Islamabad Capital Territory"
]
weather_label = CTkLabel(root,text='Weather App',font=("Comic Sans MS",40,"bold"),height=50,width=450)
weather_label.place(x=25,y=50)
city_name = StringVar()
combo = CTkComboBox(root,values=list_name,corner_radius=15,font=("Comic Sans MS",30,"bold")
                    ,variable=city_name,height=50,width=300)
combo.place(x=100,y=150)



w_label = CTkLabel(root,text='Weather Climate: ',font=("Comic Sans MS",20)
                   ,height=50,width=200)
w_label.place(x= 70,y=310)

w_label1 = CTkLabel(root,text='',font=("Comic Sans MS",20)
                   )
w_label1.place(x=255,y=320)


wd_label = CTkLabel(root,text='Weather Discription: ',font=("Comic Sans MS",20)
                   ,height=20,width=200)
wd_label.place(x=89,y=350)

wd_label1 = CTkLabel(root,text='',font=("Comic Sans MS",20))
wd_label1.place(x=290,y=350)

temp_label = CTkLabel(root,text='Temprature: ',font=("Comic Sans MS",20)
                   ,height=20,width=200)
temp_label.place(x=50,y=378)

temp_label1 = CTkLabel(root,text='',font=("Comic Sans MS",20))
temp_label1.place(x=210,y=378)

pre_label = CTkLabel(root,text='Pressure: ',font=("Comic Sans MS",20)
                   ,height=20,width=200)
pre_label.place(x=40,y=405)

pre_label1 = CTkLabel(root,text='',font=("Comic Sans MS",20))
pre_label1.place(x=190,y=405)

done_btn = CTkButton(root,text="Done",font=("Comic Sans MS",20,"bold"),corner_radius=15
                     ,fg_color='skyblue',text_color='black',height=50,width=100,command=get_data)
done_btn.place(x=200,y=250)
root.mainloop()