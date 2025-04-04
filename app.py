import speech_recognition as sr #SpeechRecognition module
import pyttsx3
import webbrowser
from song_playlist import playlists, songs
from flask import Flask,render_template
import threading
import google.generativeai as genai


genai.configure(api_key="Your-GOOGLE-API-KEY") #removes my API key due to security reasons in my public repo

def generate_reply(user_input):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(user_input)
    return response.text

# Initialize the recognizer
r = sr.Recognizer()
def listen():
        with sr.Microphone() as source:
            print('listening...')
            r.pause_threshold = 1
            audio = r.listen(source)
            print('Loading...')
        text_speech = r.recognize_google(audio)
        print(text_speech)
        return text_speech
def speak(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(command)
    engine.runAndWait()

# Tasks
def work(text):
    if 'google' in text.lower():
        speak('Opening Google')
        if 'search' in text.lower():
            speak('What to search?')
            try:
                AtT2 = listen()
                webbrowser.open(f'https://www.google.com/search?q={AtT2}')
            except Exception as e:
                print(e)
        else:
            webbrowser.open('https://www.google.com')
    elif 'youtube' in text.lower():
        speak('Opening Youtube')
        if 'search' in text.lower():
            speak('Channel name?')
            try:
                AtT2 = listen()
                webbrowser.open(f'https://www.youtube.com/results?search_query={AtT2}')
            except Exception as e:
                print(e)
        else:
            webbrowser.open('https://www.youtube.com')
    elif 'instagram' in text.lower():
        speak('Opening Instagram')
        webbrowser.open('https://www.instagram.com')
    elif 'play' in text.lower():
        speak('Opening Youtube')
        if 'playlist' in text.lower():
            try:
                for elem in text.lower().split():
                    if elem in playlists:
                        webbrowser.open(playlists[elem])
            except Exception as e:
                print(e)
        elif 'song' in text.lower():
            speak('Which song?')
            try:
                AtT2 = listen()
                print(AtT2)
                if AtT2 in songs:
                    webbrowser.open(songs[AtT2])
                else:
                    webbrowser.open(f'https://www.youtube.com/results?search_query={AtT2}')
            except Exception as e:
                print(e)
    else:
        return False
app = Flask(__name__)

running=False
def iris():
    global running
    speak('Your virtual assistant "Iris" is ready')
    while running:
        try:
            AtT = listen()
            if AtT.lower() in ['break', 'finish', 'end','stop']:
                speak('See you soon!')
                running = False
            elif (AtT.lower()==['iris']) or 'hello' in AtT.lower():
                speak('Yes, how may I help you?')
                AtT1 = listen()
                w = work(AtT1)
                print(w)
                if w is False:
                    response = generate_reply(AtT1)
                    speak(response)
        except Exception as e:
             print('Error:', e)

@app.route('/iris', methods=['POST'])
def start_iris():
    global running, assistant_thread
    if not running:
        running = True
        assistant_thread = threading.Thread(target=iris)
        assistant_thread.start()
    return render_template('index_listening.html')

@app.route('/')
@app.route('/', methods=['POST'])
def stop_iris():
    global running, assistant_thread
    if running:
        running = False  
        if assistant_thread and assistant_thread.is_alive():
            assistant_thread.join()  
        return render_template('index.html') 
    return render_template('index.html')  

app.run(debug=True)
