import speech_recognition as sr;
import webbrowser;
import pyttsx3;
import musicLibrary;


recognizer = sr.Recognizer();
def speak(text):
    engine = pyttsx3.init();
    print(text);
    engine.say(text)
    engine.runAndWait()
def processCommand(command):
    if "open google" in command.lower():
        webbrowser.open("https://google.com");
    elif "open youtube" in command.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "music" in command.lower():
        if("believer" in command.lower()):
            music = musicLibrary.music["believer"]
            webbrowser.open(music)
        elif("man" in command.lower()):
            music = musicLibrary.music["weller man"];
            webbrowser.open(music)
    else:
        speak("couldnot recognize")
if __name__=="__main__":
    speak("Initializing Jarvis")
    # Listen for the wake word "Jarvis"
    r = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=6,phrase_time_limit=3)

            print("recognizing....")
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Yeah");
                with sr.Microphone() as source:
                    print("Jarvis Activated...")
                    audio = r.listen(source,timeout=6,phrase_time_limit=3);
                    command = r.recognize_google(audio);
                    print(command)
                    processCommand(command);
        except Exception as e:
            print(e)
