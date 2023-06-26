# pip install pyttsx3
# pip install googletrans
# pip install --upgrade googletrans==4.0.0-rc1
# install kalpana voice for hindi :)

# After install Kalpana voice you must need to check your voice list
# Also install Hindi from your computer " Language Settings "

# import pyttsx3
# engine = pyttsx3.init()
# voices = engine.getProperty("voices")
# for voice in voices:
#     print(voice)

"""
Establishment of IT/Hi-Tech Park at District Level (12 District) Project.
Bangladesh Hi-Tech Park Authority
ICT Ministry, ICT Tower, Agargaon, Dhaka.
Course Name: Introduction to Python Programming
"""

import pyttsx3 
import webbrowser
import datetime
import requests
import speech_recognition as sr
from googletrans import Translator
import sys

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.setProperty("rate", 185)
    engine.say(text)
    engine.runAndWait()

def clockTime():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("शुभ प्रभात")
    elif hour >= 12 and hour < 18:
        speak("अभी दोपहर")
    elif hour >= 18 and hour < 20:
        speak("अभी शाम")
    else:
        speak("शुभ रात्रि")

lang_convert = Translator()
audio = sr.Recognizer()

if __name__ == '__main__':
    clockTime()
    speak("हैलो मेरा नाम शेख सलाहुद्दीन है, बताइये में आपकी क्या मदद कर सक्ती हूं")
    while True:
        # speak("बोलिए और क्या मदद चाहिए")
        with sr.Microphone() as source:
            audio.adjust_for_ambient_noise(source, duration=0.6)
            speak("आपकी आवाज सुनी जा रही है")
            print("Listening...")
            record = audio.listen(source, timeout=None, phrase_time_limit=6)

            try:
                command = audio.recognize_google(record, language='hi-IN')
                speak("आपने कहा: " + command)
                translated = lang_convert.translate(command, dest='en').text

                if "time" in translated.lower() or "date" in translated.lower() or "time and date" in translated.lower():
                    now = datetime.datetime.now()
                    date = now.strftime('%Y-%m-%d')
                    clock = now.strftime('%I:%M %p')
                    speak(f"आज की तिथि है {date} और वर्तमान समय है {clock}")

                elif "ip address" in translated.lower():
                    speak("अपने इंटरनेट प्रोटोकॉल (आईपी) पते की जाँच कर रहे हैं, कृपया एक पल के लिए प्रतीक्षा करें!")
                    response = requests.get("https://api.ipify.org")
                    ip_address = response.text
                    print(f"Your IP address is: {ip_address}.")
                    speak(f"आपका इंटरनेट प्रोटोकोल (आई पी) है: {ip_address}")

                elif "youtube" in translated.lower():
                    print("Opening Youtube")
                    speak("youtube.com खोला जा रहा है")
                    webbrowser.open("https://www.youtube.com/")

                elif "date and time" in translated.lower():
                    now = datetime.datetime.now()
                    date = now.strftime('%Y-%m-%d')
                    clock = now.strftime('%I:%M %p')
                    print(f"Today's date is {date} and the current time is {clock}")
                    speak(f"आज की तिथि है {date} और वर्तमान समय है {clock}")

                elif "google" in translated.lower():              
                    print("Opening Google")
                    speak("गूगल खोला जा रहा है")
                    webbrowser.open("https://www.google.com/")

                elif "wikipedia" in translated.lower():
                    print("Opening Wikipedia")
                    speak("विकिपीडिया खोला जा रहा है")
                    webbrowser.open("https://wikipedia.org/")

                elif "who made you" in translated.lower() or "creator" in translated.lower():
                    print("Full Name: Sk. Salahuddin,\nAddress: House/Holding No. 173,\nVillage/Road: Maheshwar Pasha Kalibari,\nPost Office: KUET, \nPostal Code: 9203,\nPolice Station: Daulatpur,\nDistrict: Khulna, \nCountry: Bangladesh, \nMobile No. +8801767902828\nEmail: sksalahuddin2828@gmail.com")
                    speak("नाम: शेख सलाहुद्दीन ने मुझे बनाया। वह जिला स्तर (12 जिला) परियोजना में आईटी/हाई-टेक पार्क की स्थापना का छात्र है। बांग्लादेश हाई-टेक पार्क अथॉरिटी। आईसीटी मंत्रालय, आईसीटी टावर, अगरगांव, ढाका। उनके कोर्स का नाम है: पायथन प्रोग्रामिंग का परिचय। उन्होंने इसे सिटी आईटी पार्क, खलीशपुर, खुलना से पूरा किया। उसका विवरण स्क्रीन पर छपा हुआ है। चलिए मैं आपको उसका गिठूब अकाउंट पर लेकर जा रहा हूं, ताकि आप उसको पहचान सके।")
                    webbrowser.open("https://github.com/sksalahuddin2828")

                elif "close" in translated.lower() or "exit" in translated.lower() or "good bye" in translated.lower() or "ok bye" in translated.lower() or "turn off" in translated.lower() or "shut down" in translated.lower():
                    speak("अपना ध्यान रखना, बाद में मिलते हैं! धन्यवाद")
                    print("Stopping Program")
                    sys.exit()

            except sr.UnknownValueError:
                speak("में आपकी आवाज समझ नहीं पा रहा हूं। कृपा फिर से बोलिए")
                print("Unrecognized Voice, Say that again please.")

            except sr.RequestError as e:
                speak("Google स्पीच रिकग्निशन सर्विस से परिणाम नहीं प्राप्त कर सका;{0}".format(e))
                print("Could not request results from Google Speech Recognition service;{0}".format(e))
