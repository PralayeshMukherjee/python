import pyttsx3;

engine = pyttsx3.init();
def speek(text):
    engine.say(text);
    engine.runAndWait();
speek("hey raj my name is pyttsx3, I convert your python text to speech");
speek("hello")