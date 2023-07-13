"""
This project has been created for,
Establishment of IT/Hi-Tech Park at District Level (12 District) Project.
Bangladesh Hi-Tech Park Authority
ICT Ministry, ICT Tower, Agargaon, Dhaka.
Course Name: Introduction to Python Programming
"""

import speech_recognition as sr
from googletrans import Translator
from tabulate import tabulate
from colorama import init, Fore
import pyttsx3
import wikipedia
import webbrowser
import requests
import datetime
import pywhatkit
import pyjokes
import wolframalpha

init() # Initialize Colorama

search = pyttsx3.init()
print(Fore.CYAN + "Sk. Salahuddin - Khulna" + Fore.RESET)

def speak(text):
    voices = search.getProperty("voices")
    search.setProperty("voice", voices[3].id)
    search.setProperty("rate", 185)
    search.say(text)
    search.runAndWait()

# Define the supported voice commands and their corresponding actions
commands = {
    "The voice commands I support are given on your screen": "What can you do / Available commands / Help",
    "Bangabandhu Sheikh Mujibur Rahman, The Father of the Nation of Bangladesh": "Bangabandhu Sheikh Mujibur Rahman / Bangabandhu / Sheikh Mujibur Rahman / Father of the nation of Bangladesh",
    "Weather Report": "Weather / Weather Report / Today's Weather Report",
    "IP Address": "IP Address / Internet Protocol / IP",
    "Opening Wikipedia": "Opening Wikipedia",
    "Search on Wikipedia": "Search on Wikipedia",
    "Search on YouTube": "Search on YouTube",
    "Play on YouTube": "Play on YouTube / Play from YouTube / Play a song from YouTube / Play a movie from YouTube / play something on youtube / play something from youtube",
    "Opening YouTube": "Open YouTube / Opening YouTube",
    "Date and time": "Date and Time",
    "Local Time": "Today's time / Local Time / Time ",
    "Today's date": "Today's date / Today date / Date",
    "Opening Facebook": "Opening Facebook",
    "Opening Facebook profile": "Facebook Profile",
    "Opening Facebook settings": "Facebook Settings",
    "Opening Facebook reels": "Facebook Reels",
    "Opening Facebook messenger": "Facebook Messenger",
    "Opening Facebook video": "Facebook Video",
    "Opening Facebook notifications": "Facebook Notification",
    "Opening Google browser": "Opening Google",
    "Opening Gmail": "Opening Gmail",
    "Opening Google Earth": "Google Earth",
    "Search on Google Earth Specify City": "Google City / City on Google / City from Earth / City on Earth",
    "Opening Google Map": "Google Map / Map / Map on Google",
    "Search on Google Map": "City from Map / Map city / City on map / Google map city",
    "Translate specific sentence": "Translate to english / Translate into english / Word translate / Translate a sentence",
    "I can tell jokes": "Listen a joke / Tell me a joke",
    "Translate between two languages": "Translation between two language / Translated language / Translate from google / Language translation",
    "Who made me": "Who made you",
    "Computation and Geographical Question": "Ask",
    "Exit command": "Exit / Close / Off / Good Bye / Bye / OK Bye / Turn Off / Shut Down / No Thanks / Stop"
}

def takeCommand():
    lang_convert = Translator()
    record = sr.Recognizer()
    with sr.Microphone() as source:
        record.adjust_for_ambient_noise(source, duration=0.6)
        print(Fore.LIGHTYELLOW_EX + "Listening..." + Fore.RESET)
        audio = record.listen(source, timeout=None, phrase_time_limit=6)
        try:
            user_input = record.recognize_google(audio, language='en-IN')
            print(Fore.LIGHTGREEN_EX + f"User said: {user_input}\n" + Fore.RESET)
            speak("You said: " + user_input)
            translated = lang_convert.translate(user_input, dest='en').text

        except sr.UnknownValueError:
            print(Fore.LIGHTRED_EX + "I didn't hear you, please say that again" + Fore.RESET)
            speak("I didn't hear you, please say that again")
            return "none"
        
        except sr.RequestError:
            print(Fore.RED + "Sorry, I'm having trouble processing your request. Please try again later." + Fore.RESET)
            speak("Sorry, I'm having trouble processing your request. Please try again later.")
            return "none"
        
        except Exception as e:
            print(Fore.RED + "Sorry, an error occurred. Please try again;{0}".format(e) + Fore.RESET)
            speak("Sorry, an error occurred. Please try again;{0}".format(e))
            return "none"
        return translated.lower()

def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=99e68c086c34059f58d3349bd4fb694c&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        weather = response.json()
        temperature = weather['main']['temp']
        feels_like = weather['main']['feels_like']
        humidity = weather['main']['humidity']
        pressure = weather['main']['pressure']
        wind_speed = weather['wind']['speed']
        wind_direction = weather['wind']['deg']
        visibility = weather['visibility']
        description = weather['weather'][0]['description']
        clouds = weather['clouds']['all']
        sea_level = weather['main']['sea_level'] if 'sea_level' in weather['main'] else None
        sunrise = weather['sys']['sunrise']
        sunset = weather['sys']['sunset']

        # Additional weather details
        rain_volume = weather['rain']['1h'] if 'rain' in weather else 0
        snow_volume = weather['snow']['1h'] if 'snow' in weather else 0

        weather_report = f"Weather in {city}:\n\nTemperature: {temperature} °C\nFeels like: {feels_like} °C\nHumidity: {humidity}%\nPressure: {pressure} hPa\nWind Speed: {wind_speed} m/s\nWind Direction: {wind_direction}°\nVisibility: {visibility} meters\nDescription: {description}\nCloud Cover: {clouds}%\nRain Volume: {rain_volume} mm\nSnow Volume: {snow_volume} mm\nSunrise: {sunrise}\nSunset: {sunset}"

        if sea_level:
            weather_report += f"\nSea Level: {sea_level} hPa"

        if rain_volume > 0 or snow_volume > 0:
            weather_report += "\n\nRain or snow is expected within the next 24 hours."

        return weather_report
    else:
        return "Unable to get the weather report. Please try again later."

def clockTime():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    elif hour >= 18 and hour < 19:
        speak("Good Evening")

def clockTime_night():
    hour = datetime.datetime.now().hour
    if hour >= 18 and hour < 24:
        speak("Good Night")

# The greatest respected personality of all time
# Father of the Nation of Bangladesh
def father_of_the_nation_of_bangladesh():
    print("The Father of the Nation Bangabandhu Sheikh Mujibur Rahman is the architect of independent Bangladesh. Sheikh Mujibur Rahman, known as Bangabandhu, often shortened as Sheikh Mujib or Mujib, also widely was the founder of Bangladesh. Bangabandhu Sheikh Mujibur Rahman is the 'Greatest Bengali of All Time'. He was born in a respectable Muslim family on 17 March, 1920, at Tungipara village under the Gopalganj district. He started his student life at Gimadanga Primary School at the age of seven. He passed the entrance examination from this school and got admitted to the Kolkata Islamia College. Then he took admission into Dhaka University and founded the Muslim Students League. He was one of the front-line leaders of the Language Movement and was arrested on March 11, 1948. In 1970, he was re-elected President of Awami League. Under his leadership, Awami League took part in the General Election of 1970 and gained absolute majority. On March 7, Bangabandhu Sheikh Mujibur Rahman addressed a mammoth public rally at the Race Course ground. On the fierce night of March 25, the Pakistani Army cracked down on the innocent unarmed Bangalees, and arrested Sheikh Mujib. All the Bangalees, jumped into a bloody battle against the occupation forces. On December 16, 1971, Bangladesh became a free nation and Bangabandhu was freed from the Pakistani jail on January 8, 1972 and returned to his beloved country on January 10. It is a matter of regret that, Bangabandhu, the founding father of the nation, was killed by a group of wayward army officers. An Egyptian journalist noted that Sheikh Mujibur Rahman does not belong to Bangladesh alone. He is the harbinger of freedom for all Bengalis. His Bengali nationalism is the new emergence of Bengali civilization and culture. Mujib is the hero of the Bengalis, in the past and in the times that are. Fidel Castro remarked that I have not seen the Himalayas. But I have seen Sheikh Mujib.")
    speak("The Father of the Nation Bangabandhu Sheikh Mujibur Rahman is the architect of independent Bangladesh. Sheikh Mujibur Rahman, known as Bangabandhu, often shortened as Sheikh Mujib or Mujib, also widely was the founder of Bangladesh. Bangabandhu Sheikh Mujibur Rahman is the 'Greatest Bengali of All Time'. He was born in a respectable Muslim family on 17 March, 1920, at Tungipara village under the Gopalganj district. He started his student life at Gimadanga Primary School at the age of seven. He passed the entrance examination from this school and got admitted to the Kolkata Islamia College. Then he took admission into Dhaka University and founded the Muslim Students League. He was one of the front-line leaders of the Language Movement and was arrested on March 11, 1948. In 1970, he was re-elected President of Awami League. Under his leadership, Awami League took part in the General Election of 1970 and gained absolute majority. On March 7, Bangabandhu Sheikh Mujibur Rahman addressed a mammoth public rally at the Race Course ground. On the fierce night of March 25, the Pakistani Army cracked down on the innocent unarmed Bangalees, and arrested Sheikh Mujib. All the Bangalees, jumped into a bloody battle against the occupation forces. On December 16, 1971, Bangladesh became a free nation and Bangabandhu was freed from the Pakistani jail on January 8, 1972 and returned to his beloved country on January 10. It is a matter of regret that, Bangabandhu, the founding father of the nation, was killed by a group of wayward army officers. An Egyptian journalist noted that Sheikh Mujibur Rahman does not belong to Bangladesh alone. He is the harbinger of freedom for all Bengalis. His Bengali nationalism is the new emergence of Bengali civilization and culture. Mujib is the hero of the Bengalis, in the past and in the times that are. Fidel Castro remarked that I have not seen the Himalayas. But I have seen Sheikh Mujib.")

def ip_address():
    print("Checking your Internet Protocol (IP) address, please wait for a moment!")
    speak("Checking your Internet Protocol (IP) address, please wait for a moment!")
    url = "https://checkip.amazonaws.com"
    response = requests.get(url)
    ip = response.text
    print(f"Your IP Address is: {ip}")
    speak(f"Your IP Address is: {ip}")

# There are two ways to check the IP address:
# def ip_address():
#     print("Checking your Internet Protocol (IP) address, please wait for a moment!")
#     speak("Checking your Internet Protocol (IP) address, please wait for a moment!")
#     response = requests.get("https://api.ipify.org")
#     ip_address = response.text
#     print(f"Your IP Address is: {ip_address}")
#     speak(f"Your IP address is {ip_address}.")

def open_weather_report(city):
    speak(f"Opening the weather report for {city}.")
    print(f"Opening weather report for {city}.")
    weather_report = get_weather(city)
    print(f"Information of {city} city today's Weather report is {weather_report}.")
    speak(weather_report)

def open_wikipedia():
    print("Opening Wikipedia")
    speak("Opening Wikipedia")
    webbrowser.open("https://www.wikipedia.org/")

def search_on_wikipedia():
    speak('What do you want to search from Wikipedia?')
    search_wiki_keyword = takeCommand().lower().replace("wikipedia", "")
    results = wikipedia.summary(search_wiki_keyword, sentences=3)
    print(f"Your search item from Wikipedia is {search_wiki_keyword}")
    speak('Here are your search results from Wikipedia')
    webbrowser.open(f"https://en.wikipedia.org/w/index.php?search={results}")

def search_on_youtube():
    speak("What do you want to search on YouTube?")
    search_youtube_items = takeCommand().lower()
    print(f"Opening search results on YouTube for {search_youtube_items}")
    speak("Opening your search items on YouTube, please wait for a moment!")
    webbrowser.open(f"https://www.youtube.com/results?search_query={search_youtube_items}")

def play_on_youtube():
    speak("What do you want to play on YouTube?")
    song = takeCommand().lower()
    print(f"Playing on YouTube: {song}")
    speak("You want to play on YouTube: " + song)
    pywhatkit.playonyt(song)

def open_youtube():
    print("Opening YouTube")
    speak("Opening YouTube, please wait for a moment!")
    webbrowser.open("https://www.youtube.com/")

def tell_joke():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)

def get_date_and_time():
    now = datetime.datetime.now()
    date = now.strftime('%Y-%m-%d')
    clock = now.strftime('%I:%M %p')
    print(f"Today's date is {date} and the current time is {clock}")
    speak(f"Today's date is {date} and the current time is {clock}")

def get_local_time():
    clock = datetime.datetime.now().strftime('%I:%M %p')
    print(f"Your local time is {clock}")
    speak(f"Your local time is {clock}")

def get_today_date():
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    print(f"Today's date is {date}")
    speak(f"Today's date is {date}")

def open_facebook():
    print("Opening Facebook")
    speak("Opening Facebook, please wait for a moment!")
    webbrowser.open("https://www.facebook.com/")

def open_facebook_profile():
    print("Opening Facebook profile")
    speak("Opening Facebook profile, please wait for a moment!")
    webbrowser.open(f"https://www.facebook.com/profile.php?=facebook%20{user_input}")

def open_facebook_settings():
    print("Opening Facebook settings")
    speak("Opning Facebook settings, please wait for a moment!")
    webbrowser.open(f"https://www.facebook.com/settings/?tab=account{user_input}")

def open_facebook_reel():
    print("Opening Facebook Reels")
    speak("Opening Facebook Reels, please wait for a moment!")
    webbrowser.open(f"https://www.facebook.com/reel/?s=ifu{user_input}")

def open_facebook_messenger():
    print("Opening Facebook Messenger")
    speak("Opening Facebook Messenger, please wait for a moment!")
    webbrowser.open(f"https://www.facebook.com/messages/t/{user_input}")

def open_facebook_video():
    print("Opening Facebook Videos")
    speak("Opening Facebook Videos, please wait for a moment!")
    webbrowser.open(f"https://www.facebook.com/video/")

def open_facebook_notification():
    print("Opening Facebook notifications")
    speak("Opening Facebook notifications, please wait for a moment!")
    webbrowser.open(f"https://www.facebook.com/notifications{user_input}")

def open_google_browser():
    print("Opening Google")
    speak("Opening Google, please wait for a moment!")
    webbrowser.open(f"https://www.google.com/")

def open_google_mail():
    print("Opening Gmail")
    speak("Opening Gmail, please wait for a moment!")
    webbrowser.open(f"https://accounts.google.com/ServiceLogin?service=mail")

def opening_google_earth():
    print("Opening Google Earth")
    speak("Opening Google Earth, please wait for a moment!")
    webbrowser.open("https://earth.google.com/web/")

def google_earth_specify_city():
    print("Which city?")
    speak("Which city?")
    search_city_from_earth = takeCommand().lower()
    print(f"Opening google earth {search_city_from_earth}, please wait for a moment!")
    speak(f"Opening google earth {search_city_from_earth}, please wait for a moment!")
    webbrowser.open(f"https://earth.google.com/web/search/{search_city_from_earth}")

def opening_google_map():
    print("Opening Google Map")
    speak("Opning Google Map, please wait for a moment!")
    webbrowser.open(f"https://www.google.com/maps/")

def google_map_specify_city(): 
    print("Which city?")    
    speak("Which city:")
    map_city_name = takeCommand().lower()
    print(f"Opening your specify {map_city_name} city")
    speak(f"Opening your specific {map_city_name} city, please wait for a moment!")
    webbrowser.open(f"https://www.google.com/maps/place/{map_city_name}")

def google_translate_specify_word():
    print("What word do you want to translate from English to Bengali?")
    speak("What word do you want to translate from English to Bengali?")
    translate_speak = takeCommand().lower()
    print("Opning Google translate")
    speak("Opning Google translate, please wait for a moment!")
    webbrowser.open(f"https://translate.google.com.bd/?hl=bn&sl=en&tl=bn&text={translate_speak}&op=translate")

def translate_languages(source_language, target_language):
    translations = {
        "afrikaans": "af",
        "albanian": "sq",
        "amharic": "am",
        "arabic": "ar",
        "armenian": "hy",
        "azerbaijani": "az",
        "basque": "eu",
        "belarusian": "be",
        "bengali": "bn",
        "bosnian": "bs",
        "bulgarian": "bg",
        "catalan": "ca",
        "cebuano": "ceb",
        "chichewa": "ny",
        "chinese (simplified)": "zh-CN",
        "chinese (traditional)": "zh-TW",
        "corsican": "co",
        "croatian": "hr",
        "czech": "cs",
        "danish": "da",
        "dutch": "nl",
        "english": "en",
        "esperanto": "eo",
        "estonian": "et",
        "filipino": "tl",
        "finnish": "fi",
        "french": "fr",
        "frisian": "fy",
        "galician": "gl",
        "georgian": "ka",
        "german": "de",
        "greek": "el",
        "gujarati": "gu",
        "haitian creole": "ht",
        "hausa": "ha",
        "hawaiian": "haw",
        "hebrew": "he",
        "hindi": "hi",
        "hmong": "hmn",
        "hungarian": "hu",
        "icelandic": "is",
        "igbo": "ig",
        "indonesian": "id",
        "irish": "ga",
        "italian": "it",
        "japanese": "ja",
        "javanese": "jv",
        "kannada": "kn",
        "kazakh": "kk",
        "khmer": "km",
        "kinyarwanda": "rw",
        "korean": "ko",
        "kurdish (kurmanji)": "ku",
        "kyrgyz": "ky",
        "lao": "lo",
        "latin": "la",
        "latvian": "lv",
        "lithuanian": "lt",
        "luxembourgish": "lb",
        "macedonian": "mk",
        "malagasy": "mg",
        "malay": "ms",
        "malayalam": "ml",
        "maltese": "mt",
        "maori": "mi",
        "marathi": "mr",
        "mongolian": "mn",
        "myanmar (burmese)": "my",
        "nepali": "ne",
        "norwegian": "no",
        "odia": "or",
        "pashto": "ps",
        "persian": "fa",
        "polish": "pl",
        "portuguese": "pt",
        "punjabi": "pa",
        "romanian": "ro",
        "russian": "ru",
        "samoan": "sm",
        "scots gaelic": "gd",
        "serbian": "sr",
        "sesotho": "st",
        "shona": "sn",
        "sindhi": "sd",
        "sinhala": "si",
        "slovak": "sk",
        "slovenian": "sl",
        "somali": "so",
        "spanish": "es",
        "sundanese": "su",
        "swahili": "sw",
        "swedish": "sv",
        "tajik": "tg",
        "tamil": "ta",
        "tatar": "tt",
        "telugu": "te",
        "thai": "th",
        "turkish": "tr",
        "turkmen": "tk",
        "ukrainian": "uk",
        "urdu": "ur",
        "uyghur": "ug",
        "uzbek": "uz",
        "vietnamese": "vi",
        "welsh": "cy",
        "xhosa": "xh",
        "yiddish": "yi",
        "yoruba": "yo",
        "zulu": "zu"
    }

    if source_language not in translations:
        speak("Invalid First language specified.")
        return

    if target_language not in translations:
        speak("Invalid Second language specified.")
        return

    source_code = translations[source_language]
    target_code = translations[target_language]
    webbrowser.open(f"https://translate.google.com/?sl={source_code}&tl={target_code}&op=translate")

def available_commands():
    available_commands = [[key, str(value)] for key, value in commands.items()]
    headers = ["Action", "Voice Commands"]
    print(tabulate(available_commands, headers, tablefmt="rounded_grid"))
    speak("Here are some things I can do:")
    for key in commands.keys():
        speak(key)
    
    # using tablefmt = rounded_grid / mixed_grid / fancy_grid

def who_made_you():
    print("Full Name: Sk. Salahuddin,\nAddress: House/Holding No. 173,\nVillage/Road: Maheshwar Pasha Kalibari,\nPost Office: KUET, \nPostal Code: 9203,\nPolice Station: Daulatpur,\nDistrict: Khulna, \nMobile No. +8801767902828\nEmail: sksalahuddin2828@gmail.com")
    speak("Name: Sheikh Salahuddin made me. He is a student of Establishment of IT/Hi-Tech Park at District Level (12 District) Project. Bangladesh Hi-Tech Park Authority. ICT Ministry, ICT Tower, Agargaon, Dhaka. His Course Name is: Introduction to Python Programming. He completed it from City IT Park, Khalishpur, Khulna. His details are printed on the screen. And I have a link to his GitHub account and I'll take you there.")
    webbrowser.open("https://github.com/sksalahuddin2828")

def what_is_your_name():
    print("Sorry! I don't have a specific name. I'm just a digital assistant, that can act on certain commands given here.")
    speak("Sorry! I don't have a specific name. I'm just a digital assistant, that can act on certain commands given here.")

def computational_geographical_question():
    api_key = 'ALG3XA-2R3PGRGHR6' 
    client = wolframalpha.Client(api_key)
    speak('I can answer computational and geographical questions. What question do you want to ask now?')
    question = takeCommand().lower()
    res = client.query(question)
    answer = next(res.results).text
    print(answer)
    speak(answer)

def main(user_input):
    if "weather" in user_input or "weather report" in user_input or "today's weather report" in user_input:
        print("Sure, which city?")
        speak("Sure, which city?")
        city = takeCommand().lower()
        open_weather_report(city)

    elif "bangabandhu sheikh mujibur rahman" in user_input or "bangabandhu" in user_input or "sheikh mujibur rahman" in user_input or "father of the nation of bangladesh" in user_input or "father of the nation" in user_input:
        father_of_the_nation_of_bangladesh()

    elif "ip address" in user_input or "internet protocol" in user_input or "ip" in user_input:
        ip_address()

    elif "opening wikipedia" in user_input:
        open_wikipedia()
        
    elif "search on wikipedia" in user_input:
        search_on_wikipedia()

    elif "search on youtube" in user_input:
        search_on_youtube()

    elif "play on youtube" in user_input or "play from youtube" in user_input or "play a song from youtube" in user_input or "play a movie from youtube" in user_input or "play something from youtube" in user_input or "play something on youtube" in user_input:
        play_on_youtube()

    elif "open youtube" in user_input or "opening youtube" in user_input:
        open_youtube()

    elif "date and time" in user_input:
        get_date_and_time()

    elif "today's time" in user_input or "local time" in user_input or "time" in user_input:
        get_local_time()

    elif "today's date" in user_input or "today date" in user_input or "date" in user_input:
        get_today_date()

    elif "opening facebook" in user_input:
        open_facebook()

    elif "facebook profile" in user_input:
        open_facebook_profile()

    elif "facebook settings" in user_input:
        open_facebook_settings()

    elif "facebook reels" in user_input:
        open_facebook_reel()

    elif "facebook messenger" in user_input:
        open_facebook_messenger()

    elif "facebook video" in user_input:
        open_facebook_video()

    elif "facebook notification" in user_input:
        open_facebook_notification()

    elif "opening google" in user_input:
        open_google_browser()

    elif "opening gmail" in user_input:
        open_google_mail()

    elif "google earth" in user_input:
        opening_google_earth()

    elif "google city" in user_input or "city on google" in user_input or "city from earth" in user_input or "city on earth" in user_input:
        google_earth_specify_city()

    elif "google map" in user_input or "map" in user_input or "map on google" in user_input:
        opening_google_map()

    elif "city from map" in user_input or "map city" in user_input or "city on map" in user_input or "google map city" in user_input:
        google_map_specify_city()

    elif "translate to english" in user_input or "translate into english" in user_input or "word translate" in user_input or "translate a sentence" in user_input:
        google_translate_specify_word()

    elif "listen a joke" in user_input or "tell me a joke" in user_input:
        tell_joke()

    elif "translation between two language" in user_input or "translated language" in user_input or "translate from google" in user_input or "language translation" in user_input or "language" in user_input:
        speak("Please specify the First language")
        source_language = takeCommand().lower()
        print(f"Please specify the First language: {source_language}")

        speak("Please specify the Second language")
        target_language = takeCommand().lower()
        print(f"Please specify the Second language: {target_language}")

        translate_languages(source_language, target_language)

    elif "what can you do" in user_input or "available commands" in user_input or "help" in user_input:
        available_commands()

    elif "who made you" in user_input:
        who_made_you()
    
    elif "what is your name" in user_input or "your name" in user_input: 
        what_is_your_name()

    elif "ask" in user_input or "askew" in user_input:
        computational_geographical_question()

    else:
        print(Fore.LIGHTRED_EX + "Sorry, I didn't understand that command. Please try again!" + Fore.RESET)
        speak("Sorry, I didn't understand that command. Please try again!")

if __name__ == '__main__':
    clockTime()
    speak("Welcome, I'm your Digital Assistant")

    while True:
        print(Fore.LIGHTGREEN_EX + "How may I assist you?" + Fore.RESET)
        speak("How may I assist you?")
        user_input = takeCommand().lower()
        
        if any(exit_word in user_input for exit_word in ["exit", "close", "off", "good bye", "bye", "ok bye", "turn off", "shutdown", "no thanks", "stop"]):
            print(Fore.LIGHTGREEN_EX + "Assistant Shut Down" + Fore.RESET)
            speak('Take care and see you later')
            clockTime_night()
            speak('Bye!')
            break

        speak("Please wait")
        main(user_input)
