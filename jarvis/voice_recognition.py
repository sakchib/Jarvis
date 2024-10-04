import pyttsx3
import speech_recognition as sr
import requests

# Initialize TTS engine
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 150)
tts_engine.setProperty('volume', 1)

def speak(text):
    print("Speaking:", text)
    tts_engine.say(text)
    tts_engine.runAndWait()

def get_ai_response(query):
    # Replace this with your actual API call to get a response from the AI
    response = {
        'candidates': [{'content': {'parts': [{'text': 'नमस्ते! तुम्हाला काही मदत हवी आहे का?'}]}}]} 
    
    return response['candidates'][0]['content']['parts'][0]['text']

def main():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio, language='hi-IN')
        print("You said:", user_input)

        # Get response from AI
        ai_response = get_ai_response(user_input)
        print("AI Response:", ai_response)

        # Speak the AI response
        speak(ai_response)

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    main()
