import base64
import requests
import cv2
import pyttsx3

engine = pyttsx3.init()
import speech_recognition as sr
r = sr.Recognizer()


# converting to female voice
converter = pyttsx3.init()
voices = converter.getProperty('voices')

for voice in voices:
# to get the info. about various voices in our PC
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

# Use female voice
converter.setProperty('voice', voice_id)
converter.runAndWait()


def hear():
    with sr.Microphone() as source:
        audio = r.listen(source,phrase_time_limit=5)
    try:
        text = r.recognize_google(audio)
        for j in range(0,len(check)):
            m=check[j]
            if m in text:
                engine.say("CONGRATULATIONS. YOU HAVE WON THE GAME")
                engine.say("THE OBJECT IS "+m)
                engine.runAndWait()
                return 6
        else:
            engine.say("THE ANSWER IS INCORRECT")
            engine.say("THE OBJECT IS NOT "+text)
            engine.runAndWait()
            return i
    except:  
        engine.say("sorry could not recognise that")
        engine.say("i repeat the clue")
        engine.say(clues[i])
        engine.runAndWait()
        with sr.Microphone() as source:
            audio = r.listen(source,phrase_time_limit=5)
        try:
            text = r.recognize_google(audio)
            for j in range(0,len(check)):
                m=check[j]
                if m in text:
                    engine.say("CONGRATULATIONS. YOU HAVE WON THE GAME")
                    engine.say("THE OBJECT IS "+text)
                    engine.runAndWait()
                    return 6
            else:
                engine.say("THE ANSWER IS INCORRECT")
                engine.say("THE OBJECT IS NOT "+text)
                engine.runAndWait()
                return i
        except:  
            engine.say("sorry could not recognise that")
            engine.runAndWait()
            return i
            

def play():
    global i
    i=0
    while i<5 :
       engine.say(clues[i])
       engine.runAndWait()
       i=hear()+1
       if i==5:
           engine.say("SORRY. YOU LOST THE GAME.")
           engine.runAndWait()

hl="1"          
    

while hl=="1":
    engine.setProperty("rate", 180)
    engine.say("Welcome to TECHREZA ")
    engine.say("I am riora")
    engine.say("Hope you have understood the rules. ")
    engine.say("Let us begin")
    engine.say("Now choose a box number")
    engine.runAndWait()

    t=0

    while t<2:
        with sr.Microphone() as source:
            audio = r.listen(source,phrase_time_limit=5)
        try:
            text = r.recognize_google(audio)
            one=["one","won","1","von"]
            two=["two","2","to","too"]
            three=["three","3","tree"]
            four=["four","for","4","fore"]
            five=["5","five","fi"]
            for k in range(0,len(one)):
                if one[k] in text:
                    engine.say("you chose box one")
                    engine.runAndWait()
                    t=2
                    y=1
                    break
            for k in range(0,len(two)):
                if two[k] in text:
                    engine.say("you chose box two")
                    engine.runAndWait()
                    t=2
                    y=2
                    break
            for k in range(0,len(three)):   
                if three[k] in text:
                    engine.say("you chose box three")
                    engine.runAndWait()
                    t=2
                    y=3
                    break
            for k in range(0,len(four)):
                if four[k] in text:
                    engine.say("you chose box four")
                    engine.runAndWait()
                    t=2
                    y=4
                    break
            for k in range(0,len(five)):
                if five[k] in text:
                    engine.say("you chose box five")
                    engine.runAndWait()
                    t=2
                    y=5
                    break
            
                
        except:  
               engine.say("sorry could not recognise that")
               engine.runAndWait()
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("TECHreza")

    while True:
        ret,frame = cam.read()
        img_name = "photo_1.png"
        cv2.imwrite(img_name, frame)
        break
     
    cam.release()
     
    cv2.destroyAllWindows()
        


    # Save string of image file path below
    img_filepath = "C:\\NAMRITHA CSE\\PROJECTS\\"+img_name

    # Create base64 encoded string
    with open(img_filepath, "rb") as f:
        image_string = base64.b64encode(f.read()).decode("utf-8")

    # Get response from POST request
    response = requests.post(url="http://localhost:38101/v1/predict/bf372681-9a87-4062-aaa8-cafad892f96f",json={"image": image_string},)
    data = response.json()

    top_prediction = data["predictions"][0]


    #engine.say("The object is : \t{}".format(top_prediction["label"]))

    engine.runAndWait()


    #DEFINITIONS
    BULB=["bulb","light bulb","light","tube","tube light","LED"]
    GAMING_CONSOLE=["gaming console","game console","joystick"]
    MODEM=["modem","router","modern","jio fi","model"]
    SPEAKER=["speaker","speakers","bluetooth speaker","bluetooth speakers","loud speaker","loud speakers","sticker"]
    SWITCH=["switch","switches","witch","switch board"]
    BULB_CLUE=["the pain in my heart brings forth warmth"," i shine when i am under trial"," i have 2 horns inside me","i am transparent but colourful", "i am useful when i burn"]
    GAMING_CONSOLE_CLUE=["i guide you to your destination","you touch me, you press me, you hurt me a lot ","you hold onto me but i do not have hands","i dont die i recharge","i can help you drive, run, chase and win"]
    MODEM_CLUE=["2 opposites make my name","as years passed by i became smaller","i am the supplier of your entertainment","the closer i am the  happier u are","u raise me up  when i am down"]
    SPEAKER_CLUE=["I look meshy but i dont sound messy","When I speak I'm the center of attention","I have no mouth, yet I speak to you","My heart vibrates a song for you","The way I speak is loud and clear"]
    SWITCH_CLUE=["my name means change","I can brighten the life around you","You tried balancing me when you were small","I have two invisible tails","i look like a sea saw and can work well with your fingers"]

    #CHANGE SPEED
    engine.setProperty("rate", 160)
    
    obj=top_prediction["label"]
    if obj=="BULB":
        engine.say("HERE GOES YOUR CLUES")
        engine.runAndWait()
        check=BULB
        clues=BULB_CLUE
        play()
    elif obj=="SPEAKER":
        engine.say("HERE GOES YOUR CLUES")
        engine.runAndWait()
        check=SPEAKER
        clues=SPEAKER_CLUE
        play()

    elif obj=="GAMING CONSOLE":
        engine.say("HERE GOES YOUR CLUES")
        engine.runAndWait()
        check=GAMING_CONSOLE
        clues=GAMING_CONSOLE_CLUE
        play()

    elif obj=="MODEM":
        engine.say("HERE GOES YOUR CLUES")
        engine.runAndWait()
        check=MODEM
        clues=MODEM_CLUE
        play()
    else:
        check=SWITCH
        engine.say("HERE GOES YOUR CLUES")
        engine.runAndWait()
        clues=SWITCH_CLUE
        play()

    engine.say("THANK YOU FOR PLAYING. ENJOY HESTIA")
    engine.runAndWait()
    hl=input()
