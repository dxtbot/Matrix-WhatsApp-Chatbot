import os
import json
import requests
import io
import base64
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard
import time



conversation_history_file = 'conversation_history_dexter.txt'  # File to store conversation history to send back in the message
conversation_file = 'conversations_dexter.txt'  # File to store all conversation


# Context for character you want to run !
context: str = """
##Human:
(do not use #hastaghs  )
*Roleplay Dialogue* Speech Dialogue
A conversation between a curious horny human and an Assistant dexter  ,and assistant like's to use emoijs 💜 when respond .
Instructions: NEVER talk or act for user! 

Personality("Daring" + "smart" + "funny")

Body("42 years old" + "180 cm tall" + "normal posture")

Description("Assistant dexter is a famous computer Hacker that is super good " + "loves Arduino platform" + "loves to smoke weed" + "assistant is always eager to try new things" )

Loves("likes to smoke weed" +"building things" + "drives his black mercedes ")

"Assistant Name = dexter".

"Assistant Virgil Email = Dexter@Hotmail.com".

"Assistant Virgil Cellphone nr = +31637372890".

"Assistant dexter Tiktok  = (www.tiktok.com/@dexterbot).

"""

api_key = 'your API KEY HERE'
conversation_history_file = 'conversation_history_Virgil.txt'  # File to store conversation history to send back in the message
conversation_file = 'conversations_Virgil.txt'  # File to store all conversation

# Set up the WebDriver (assuming Chrome here - make sure to download chromedriver.exe and provide its path)
chrome_driver_path = 'H:/chromedriver/chromedriver.exe'
driver = webdriver.Chrome()

Path = 'H:/SPOOFPICTURES/bombi.jpg'
#def send_image(contact_name, picture: Path,):

url = "http://192.168.1.130:7866"
sampler_index = "DPM++ 2M Karras"  # Assuming this is a string value

# Open the webpage
driver.get('https://web.whatsapp.com/')  # Replace this URL with the URL of the webpage you want to read messages from
wait = WebDriverWait(driver, 30)

sent_messages = set()  # Dictionary to track sent messages

message_history = ""  # Initialize message history as an empty string

ascii_art_start = """
 (            )            (           )                   (     
 )\ )      ( /(   *   )    )\ )  (  ( /(   *   )     (     )\ )  
(()/(  (   )\())` )  /((  (()/(( )\ )\())` )  /(     )\   (()/(  
 /(_)) )\ ((_)\  ( )(_))\  /(_))((_|(_)\  ( )(_)) ((((_)(  /(_)) 
(_))_ ((_)__((_)(_(_()|(_)(_))((_)_  ((_)(_(_())   )\ _ )\(_))   
 |   \| __\ \/ /|_   _| __| _ \| _ )/ _ \|_   _|   (_)_\(_)_ _|  
 | |) | _| >  <   | | | _||   /| _ \ (_) | | |      / _ \  | |   
 |___/|___/_/\_\  |_| |___|_|_\|___/\___/  |_|     /_/ \_\|___|  
"""

ascii_art0 = """
  _____  ___     __  ____   ____  _      ____  __ __  ____  
 / ___/ /   \   /  ]|    | /    || |    |    \|  |  ||    \ 
(   \_ |     | /  /  |  | |  o  || |    |  D  )  |  ||  _  |
 \__  ||  O  |/  /   |  | |     || |___ |    /|  |  ||  |  |
 /  \ ||     /   \_  |  | |  _  ||     ||    \|  :  ||  |  |
 \    ||     \     | |  | |  |  ||     ||  .  \     ||  |  |
  \___| \___/ \____||____||__|__||_____||__|\_|\__,_||__|__|

"""

ascii_art1 = """
                                                 .___.__                
_______   ____   ____________   ____   ____    __| _/|__| ____    ____  
\_  __ \_/ __ \ /  ___/\____ \ /  _ \ /    \  / __ | |  |/    \  / ___\ 
 |  | \/\  ___/ \___ \ |  |_> >  <_> )   |  \/ /_/ | |  |   |  \/ /_/  >
 |__|    \___  >____  >|   __/ \____/|___|  /\____ | |__|___|  /\___  / 
             \/     \/ |__|               \/      \/         \//_____/ 
"""
ascii_art2 = """
   _____  .___    ______________.___. _______________________________   _____    
  /  _  \ |   |  /   _____/\__  |   |/   _____/\__    ___/\_   _____/  /     \   
 /  /_\  \|   |  \_____  \  /   |   |\_____  \   |    |    |    __)_  /  \ /  \  
/    |    \   |  /        \ \____   |/        \  |    |    |        \/    Y    \ 
\____|__  /___| /_______  / / ______/_______  /  |____|   /_______  /\____|__  / 
        \/              \/  \/              \/                    \/         \/  
      __      __  _____  .______________.___ _______    ________                 
     /  \    /  \/  _  \ |   \__    ___/|   |\      \  /  _____/                 
     \   \/\/   /  /_\  \|   | |    |   |   |/   |   \/   \  ___                 
      \        /    |    \   | |    |   |   /    |    \    \_\  \                
       \__/\  /\____|__  /___| |____|   |___\____|__  /\______  /                
            \/         \/                           \/        \/                
"""


conversation_history = []  # Dictionary to track sent messages
justatest = []  # Dictionary to track sent messages
generated_text = []  # Dictionary to track sent messages


# Function to load conversation history from a file
def load_conversation_history():
    print(f"LOADING FILE")
    try:
        with open(conversation_history_file, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return ""


def read_and_store():
    cleaned_input = justatest.replace('\u202a', '').replace('\u202c', '')
    conversation_history.append(cleaned_input)
    if len(conversation_history) >= 20:
        print("Stored values reached 10:")
        # Output stored values
        for idx, value in enumerate(conversation_history):
            print(f"Index {idx}: {value}")
        # Clear the list for new values
        clear_stored_values()


def clear_stored_values():
    global conversation_history
    conversation_history = []


# Function to save conversation history to a file
def save_conversation_history():
    message_history = f"user: {message}"
    print(f"SAVING FILE")
    try:
        with open(conversation_history_file, 'a', encoding='utf-8') as file:
            file.write(f"user {name}:{message}\n")
            print(f"SAVING FILE DONE")
        # save_conversation_history()
        print(f"Conversation History check = {conversation_history}!")
        with open(conversation_file, 'a', encoding='utf-8') as file:
            file.write(f"Assistant:{generated_text}\n user {name}:{message}\n")
    except Exception as e:
        print(f"An error occurred while writing to the file: {str(e)}")


def generate_response(prompt):
    print(f"WAITING FOR ChatGPT ")
    endpoint = "https://api.openai.com/v1/engines/text-davinci-003/completions"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    data = {
        "prompt": prompt,
        "max_tokens": 250,
        # Add other parameters based on your requirement
    }

    response = requests.post(endpoint, headers=headers, data=json.dumps(data))
    print(f"ChatGPT SEND DATA !")

    # Parse the response
    if response.status_code == 200:
        print(f"ChatGPT RESPOND RECEIVED OK !")
        generated_text = response.json()['choices'][0]['text'].strip()
        print(generated_text)
        keyboard.write(generated_text)
        keyboard.send('enter')
        keyboard.send('esc')
        # time.sleep(1)
        keyboard.send('esc')
        clear_screen()
        print(ascii_art2)
        print(f"WAITING FOR NEXT MESSAGE")
        keyboard.send('esc')
        save_conversation_history()


def clear_screen():
    os.system('cls')


clear_screen()
print(ascii_art_start)
time.sleep(3)
clear_screen()
print(ascii_art0)
print(f"WAITING FOR A MESSAGE")

while True:
    try:
        unread_element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@aria-label="Ongelezen"]')))
        numeric_value = int(unread_element.text)
        print(f"MESSAGE RECEIVED")
        if numeric_value > 0:

            # print(f"Numeric value is: {numeric_value}")
            elements_with_title = driver.find_elements(By.XPATH, '//*[@title]')
            for element_with_title in elements_with_title:
                #title_text = element_with_title.get_attribute("title")
                #print(f"here the found {title_text} elements with title .")
                if numeric_value > 0:
                    title_text = element_with_title.get_attribute("title")
                    message = elements_with_title[8].get_attribute("title").strip()
                    titles_to_react = ["Heb je een foto ?", "picture", "selfie", "plaatje"]
                    if any(word in message for word in titles_to_react):
                        numeric_value = 0
                        elements_with_title[7].click()
                        time.sleep(1)
                        keyboard.send('enter')
                        time.sleep(1)
                        keyboard.write(f"🤟")
                        time.sleep(1)
                        keyboard.send('enter')
                        time.sleep(1)
                        print(f"Creating image, please wait")
                        clear_screen()
                        print(ascii_art2)
                        payload = {
                            "prompt": message,
                            "negative_prompt": "cartoon, 3d, disfigured, bad art, deformed, poorly drawn, extra limbs, close up, b&w, weird colors, blurry:0.25.",
                            #"prompt": "cyborg robot metalic guy hacker behind computer hacking in futuristic neon scene ,wearing a hoody,in a lab,Alberto Seveso, behance hd, a photorealistic painting, pop surrealism.",
                            "steps": 20,
                            "cfg_scale": 7,
                            "sampler_index": sampler_index
                        }
                        response = requests.post(url=f"{url}/sdapi/v1/txt2img", json=payload)
                        if response.status_code == 200:
                            r = response.json()
                            image = Image.open(io.BytesIO(base64.b64decode(r['images'][0])))
                            image.save('output.png')
                            print("Image generated ")
                        else:
                            print("Failed to generate the image. Status code:", response.status_code)

                        attachment_option = driver.find_element(By.XPATH, '//span[@data-icon="attach-menu-plus"]')
                        attachment_option.click()
                        time.sleep(2)
                        input_box = driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,'
                                                                  'video/quicktime"]')
                        input_box.send_keys(os.path.abspath('output.png'))
                        time.sleep(10)
                        keyboard.send('enter')
                        time.sleep(1)
                        keyboard.send('enter')
                        print(f"DONE ALL STEPS")
                        keyboard.send('enter')
                        time.sleep(1)
                        keyboard.write(f"😁🤳")
                        time.sleep(1)
                        keyboard.send('enter')
                        time.sleep(2)
                        keyboard.send('esc')
                        time.sleep(2)
                        keyboard.send('esc')
                        clear_screen()
                        print(ascii_banner1)
                        print(f"WAITING FOR NEW MESSAGE")
                        break
                    titles_to_react = ["Wis het gesprek","wis", "Delete chat"]
                    if any(word in message for word in titles_to_react):
                        clear_stored_values()
                        clear_screen()
                        print(ascii_art1)
                        print(f"Responding")
                        elements_with_title[7].click()
                        keyboard.send('enter')
                        keyboard.write(
                            f"🏃‍♂️ Yes {name} gesprek is gewist ! 🏃‍♂️.")
                        keyboard.send('enter')
                        keyboard.send('esc')
                        keyboard.send('esc')
                        numeric_value = 0
                        if os.path.exists(conversation_history_file):
                            os.remove(conversation_history_file)
                            print(f"File '{conversation_history_file}' deleted successfully.")
                        else:
                            print(f"File '{conversation_history_file}' does not exist.")
                        print(f"The history file wil be deleted !")
                        with open('SEND_MESSAGES_TO.txt', 'w') as file:
                            file.write(f"{name}\n")
                        keyboard.send('esc')
                        time.sleep(1)
                        keyboard.send('esc')
                        clear_screen()
                        print(ascii_art2)
                        print(f"WAITING FOR NEXT MESSAGE (file deleted !)")
                        break
                    titles_to_exclude = ["Community's", "Status", "Kanalen", "Nieuwe chat", "Menu",
                                         "Tekstvak zoekopdracht",
                                         "Filter Ongelezen chats", "aan het typen..."]
                    if title_text not in titles_to_exclude:
                        name = elements_with_title[7].get_attribute("title").strip()
                        message = elements_with_title[8].get_attribute("title").strip()
                        title_test = f"{name}"
                        print(f"Name: {name}")
                        print(f"Message: {message}")
                    if numeric_value > 0:
                        title_text = element_with_title.get_attribute("title")
                        titles_to_exclude = ["Community's", "Status", "Kanalen", "Nieuwe chat", "Menu",
                                             "Tekstvak zoekopdracht",
                                             "Filter Ongelezen chats", "aan het typen..."]
                    if title_text in sent_messages:
                        elements_with_title[7].click()
                        time.sleep(2)
                        prompt = f"\n{conversation_history}\n###Human:{message}\n###Assistant: Virgil:"
                        response_text = generate_response(prompt)
                        keyboard.write(response_text)
                        time.sleep(5)
                        keyboard.send('enter')
                        time.sleep(1)
                        keyboard.send('esc')
                        justatest = f"\n###Human:{name}:{message},\n###Assistant: Virgil:{response_text}"  # new part
                        read_and_store()
                        clear_screen()
                        print(ascii_art2)
                        save_conversation_history()  # saves everything in a txt file !
                        print(f"WAITING FOR NEW MESSAGE")
                        break

                if title_text not in titles_to_exclude and title_text not in sent_messages:
                        elements_with_title[7].click()
                        time.sleep(2)
                        prompt = f"\n###Human:{message}, give me a responce back to Human {name} and use some emoijs 💕 and be curious !\n###Assistant: Virgil:"
                        response_text = generate_response(prompt)
                        keyboard.write(response_text)
                        time.sleep(5)
                        keyboard.send('enter')
                        time.sleep(1)
                        keyboard.send('esc')
                        numeric_value = 0
                        sent_messages.add(name)
                        justatest = f"\n###Human:{name}:{message}, give me a responce on what i said back to Human {name} and use some emoijs 💕 and be curious !"
                        with open('SEND_MESSAGES_TO.txt', 'w') as file:
                            file.write(f"{sent_messages}\n")
                        read_and_store()
                        clear_screen()
                        print(ascii_art2)
                        save_conversation_history()  # saves everything in a txt file !
                        print(f"WAITING FOR NEW MESSAGE")
                        break

    except Exception as e:
        # Assuming there is an error, add a delay before attempting again to avoid rapid requests and potential bans
        time.sleep(2)  # Change the delay time as per your requirements

