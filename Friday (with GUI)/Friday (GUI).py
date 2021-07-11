# Friday Libraries
import threading
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import pywhatkit
import sys
import pyjokes
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import requests
import wolframalpha
import json


global j
j = 0

# tkinter Libraries
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import tkinter.scrolledtext as scrolledtext
from itertools import count
from threading import Thread

# Setup for the Engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
newVoiceRate = 180
engine.setProperty('rate',newVoiceRate)
engine.setProperty('voice', voices[1].id) 


# Invoke Friday
def friday():
    global name
    name = 'Friday'
    #chrome = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    firefox = 'C:/Program Files/Mozilla Firefox/firefox.exe %s'

    def speak(audio):
        txt.insert(INSERT,name + " : ")
        txt.insert(END, audio + "\n")
        # pady=(192,0)
        txt.pack(expand=True, fill='both',pady=(192,0))
        txt.tag_add("here", "1.0", "100.0")
        txt.tag_config("here", foreground="white")
        txt.yview(END)
        
        root.update_idletasks()
        root.update()

        engine.say(audio)
        engine.runAndWait()

    def wishMe():
        import time
        time.sleep(2)
        speak(name+" at your service. Tell me what can i do for you")
        


    def takeCommand():

        r = sr.Recognizer()
        with sr.Microphone() as source:
            txt.insert(INSERT,"\nListening... ")
            
            txt.pack(expand=True, fill='both')
            txt.tag_add("here", "1.0", "100.0")
            txt.tag_config("here", foreground="white")
            txt.yview(END)
            
            root.update_idletasks()
            root.update()
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source)


        try:
            txt.insert(INSERT,"\nRecognizing ... \n ")
            txt.pack(expand=True, fill='both')
            txt.tag_add("here", "1.0", "100.0")
            txt.tag_config("here", foreground="white")
            txt.yview(END)
            
            root.update_idletasks()
            root.update()
            query = r.recognize_google(audio, language = 'en-in')
            txt.insert(END,"\nYou said: " + query + "\n")
            txt.pack(expand=True, fill='both')
            txt.tag_add("here", "1.0", "100.0")
            txt.tag_config("here", foreground="white")
            txt.yview(END)
            
            root.update_idletasks()
            root.update()
            
        
        except Exception:
            txt.insert(END,"\nSay that again please...\n")
            txt.pack(expand=True, fill='both')
            txt.tag_add("here", "1.0", "100.0")
            txt.tag_config("here", foreground="white")
            txt.yview(END)
            
            root.update_idletasks()
            root.update()
            return "None"
        return query
    

    if __name__ == "__main__":
        if btn2['text'] == 'off':
            wishMe()

            i = 0

            while i<1:
                query = takeCommand().lower()

                if 'open youtube' in query:
                    speak("Opening Youtube")
                    webbrowser.get(firefox).open("youtube.com")

                elif 'open google' in query:
                    speak("Opening Google")
                    webbrowser.get(firefox).open("google.com")
                
                elif 'the time' in query:
                    time = datetime.datetime.now().strftime("%I:%M %p")
                    speak(f"The time is {time}")
                    

                elif 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("search for", "")
                    query = query.replace("search on", "")
                    query = query.replace("wikipedia", "")
                    res = wikipedia.summary(query, sentences = 1)
                    speak("According to Wikipedia"+"\n"+res)
                    
                
                elif 'play' in query and 'music' in query:
                    
                    speak("Which song do you want me to play?")
                    song = takeCommand().lower()
                    speak("Okay, playing "+song+ " from Youtube")

                    pywhatkit.playonyt(song)
                    i += 1
                
                elif 'netflix' in query :
                    speak(" What would you like to watch on Netflix ?")
                    series = takeCommand().lower()
                    speak("Okay, Playing "+series+ " on Netflix")
                    if 'friends' in series:
                        webbrowser.get(firefox).open("www.netflix.com/title/70153404")
                    elif 'brooklyn' in series:
                        webbrowser.get(firefox).open("www.netflix.com/title/70281562")
                    i += 1
                        
                elif 'joke' in query:
                    joke = pyjokes.get_joke()
                    speak(joke)
                    import time
                    time.sleep(1)

                elif 'search' in query and 'google' in query:
                    speak("Okay, What do you want me to search ?")
                    query = takeCommand().lower()
                    query = query.replace("search for", "")
                    speak("Okay. Searching for " +query)
                    pywhatkit.search(query)
                    speak('Here are the results')

                elif 'where is' in query:
                    query = query.replace("where is", "")
                    location = query
                    speak("Here is the location of " +location)
                    webbrowser.open("https://www.google.nl/maps/place/" + location + "")

                elif "write a note" in query:
                    speak("What should i write ?")
                    note = takeCommand()
                    file = open('mynotes.txt', 'w')
                    file.write(note)
                    
                    speak("Notes have been made. Say 'open my note' to see them")
                
                elif "open my note" in query:
                    speak("Showing Notes")
                    file = open("mynotes.txt", "r") 
                    n = file.read()
                    speak('You wrote the following -')
                    speak(n)

                elif 'news' in query:
                    try:
                        jsonObj = urlopen('''https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=YOUR_API_KEY''')
                        data = json.load(jsonObj)
                        ind = 1
                        
                        speak('here are some top news from the times of india')
                        print('''=============== TIMES OF INDIA ============'''+ '\n')
                        
                        news_list = data['articles']
                        for item in news_list[:3]:
                            
                            print(str(ind) + '. ' + item['title'] + '\n')
                            print(item['description'] + '\n')
                            speak(str(ind) + '. ' + item['title'] + '\n')
                            ind += 1
                    except Exception as e:
                        print(str(e))


                elif 'weather' in query:
                        api_key = "YOUR_API_KEY"
                        city = 'Pune'
                        loc = city.title()

                        data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")
                        speak(f"Location: "+loc)
                        speak(f"Temperature - {data.json().get('main')['temp']}° Celcius")
                        speak(f"Weather - {data.json().get('weather')[0].get('main')}")
                        speak(f"Humidity - {data.json().get('main')['humidity']}%")
                        speak(f"Wind - {data.json().get('wind')['speed']} km per hour")

                elif "what is" in query or "who is" in query or "calculate" in query or "how much" in query :
                    appId = 'API_ID'
                    client = wolframalpha.Client(appId)
                    query = query.lower()
                    res = client.query(query)
                    try:
                        answer = next(res.results).text 
                        speak(answer)
                    except StopIteration:
                        speak("Couldn't find the result!")  

                    except:
                        speak("Sorry Couldn't find it")                 

                elif 'how are you' in query:
                    speak("Thanks for asking, I'm great!")

                elif 'change' and 'voice' in query:
                    engine.setProperty('voice', voices[0].id) 
                    speak('Voice has been changed')

                elif 'change' and 'name' in query:
                    speak('what would you like to call me ?')
                    name = takeCommand().lower()
                    speak('Okay! from now on you can call me ' + name)

                elif 'thanks' in query or 'thank you' in query:
                    speak('The pleasure is mine!')

                elif 'sleep' in query:
                    speak("Okay, Going back to sleep now!")
                    i += 1
                    img2.unload()
                    func2()
                    import time
                    time.sleep(3)
                    img3.unload()
                    #bgImage1()
                    bgsleep()

        else:
            None
  

def shutDown():
    engine.say("Powering Off")
    engine.runAndWait()
    img2.unload()
    func2()
    img3.unload()
    bgImage1()
    # bgsleep()

    


# ToolTip Class for Hover Effect
class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="white", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)



class ImageLabel(tk.Label):
    """a label that displays images, and plays them if they are gifs"""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

# Setting tkinter up
root = tk.Tk()
root.geometry("850x1040")  
root.title('Friday')
root.configure(bg="black")

photo = PhotoImage(file = "img/logo.png")
root.iconphoto(False, photo)

# Image
def bgImage():

    img = Image.open("img/mf.png")
    load = img.resize((512, 512), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    img = tk.Label(root,image=render,background="black")
    img.image = render
    img.pack(pady = 20)

    # global img5
    # img5 = ImageLabel(root,text = 'on',background="black")
    # img5.place(relx = 0.5, rely = 0.303, anchor = CENTER)
    # img5.load('rbg.gif')

def bgImage1():
    img = Image.open("mf.png")
    load = img.resize((512, 512), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    img = tk.Label(root,image=render,background="black")
    img.image = render
    img.place(relx = 0.5, rely = 0.3, anchor = CENTER)

def bgsleep():
    global img4
    img4 = ImageLabel(root,text = 'on',background="black")
    img4.place(relx = 0.5, rely = 0.303, anchor = CENTER)
    img4.load('img/sleep2.gif')

def func1():
    global img2
    img2 = ImageLabel(root,background="black")
    img2.place(relx = 0.5, rely = 0.303, anchor = CENTER)
    img2.load('img/robo.gif')

def func2():
    global img3
    img3 = ImageLabel(root,background="black")
    img3.place(relx = 0.5, rely = 0.303, anchor = CENTER)
    img3.load('img/fri.gif')

    
def robo():
    e = Thread(target = func1)
    e.start()

def roboOff():
    e = threading.Event()
    e.wait(timeout=100)
 
def toggle():

    if btn2['text']== 'on':
        btn2.config(image=imagetest3)
        btn2['text'] = 'off'
        robo()
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            engine.say("Good Morning Sir!")

        elif hour >= 12 and hour < 17:
            engine.say("Good Afternoon Sir!")
        else:
            engine.say("Good Evening Sir!")
        engine.runAndWait()
        
    else:
        btn2.config(image=imagetest2)
        btn2['text'] = 'on'
        shutDown()

bgImage()

# Image Button
# lambda: [robo() ,Thread(target = friday).start()]

img1 = Image.open("img/microphone.png")
load1 = img1.resize((100, 100), Image.ANTIALIAS)
imagetest = ImageTk.PhotoImage(load1)       
     

btn = tk.Button(root, text="True", image=imagetest, command=lambda: Thread(target = friday).start(), activebackground="black", background="black",highlightthickness = 0, bd = 0)
btn.place(relx = 0.35, rely = 0.658, anchor = CENTER)

CreateToolTip(btn, text = '\n Press to give commands \n')

img3 = Image.open("img/poweron.png")
load3 = img3.resize((100, 100), Image.ANTIALIAS)
imagetest3 = ImageTk.PhotoImage(load3)

img2 = Image.open("img/poweroff.png")
load2 = img2.resize((100, 100), Image.ANTIALIAS)
imagetest2 = ImageTk.PhotoImage(load2)

global btn2
btn2 = tk.Button(root, text="on", image=imagetest2, command=toggle, activebackground="black", background="black",highlightthickness = 0, bd = 0)
btn2.place(relx = 0.65, rely = 0.658, anchor = CENTER)

CreateToolTip(btn2, text = '\n Turn ON/OFF the Assistant \n')




# Scrollable Window
txt = scrolledtext.ScrolledText(root, undo=True)
txt['font'] = ('consolas', '12','bold italic')
txt['background'] = "black"
    

root.mainloop()





