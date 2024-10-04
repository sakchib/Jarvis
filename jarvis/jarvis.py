import google.generativeai as genai
import os
import pyttsx3
import speech_recognition as sr

# Set up the API key from the environment variable
genai.configure(api_key=os.environ["API_KEY"])

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def set_voice_by_name(name):
    """Set the TTS voice to one matching the given name."""
    voices = engine.getProperty('voices')
    for voice in voices:
        if name.lower() in voice.name.lower():
            engine.setProperty('voice', voice.id)
            print(f"Using voice: {voice.name}")
            return
    print("Voice not found, using default.")

def speak(text, rate=150):  # Default rate is set to 150 words per minute
    """Convert text to speech."""
    engine.setProperty('rate', rate)  # Set the speech rate
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listen for a command and return it as text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError:
        print("Could not request results from the service.")
        return None

def change_voice(command):
    """Change the voice based on user command."""
    if "change voice to" in command.lower():
        # Extract the desired voice name from the command
        voice_name = command.lower().replace("change voice to ", "")
        set_voice_by_name(voice_name)

def main():
    # Set initial voice
    set_voice_by_name("Microsoft Zira Desktop")  # Default voice

    while True:
        # Get user input for content generation via voice
        print("Please say your command (type 'exit' to quit):")
        command = take_command()
        if command is None:
            continue  # Retry if command was not understood
        if command.lower() == "exit":
            break

        # Change voice if the command is recognized
        change_voice(command)

        # Generate content using the Gemini API
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(command)

        # Print and speak the generated content
        print("Generated Content:")
        print(response.text)
        speak(response.text, rate=160)  # Adjust the speech rate here as needed

if __name__ == "__main__":
    # Configure API key from the environment variable
    os.environ["API_KEY"] = "AIzaSyC0FNQOHqTazdwwsO669_VuNyCMgBrKVQU"  # Replace with your API key if needed
    main()
