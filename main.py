import asyncio
import random
import os
import subprocess
import datetime
import sys
import requests
import subprocess
from fastapi import FastAPI
from typing import Union
app = FastAPI()
subprocess.run(["ollama", "serve"]) #make sure that our ollama server is started

from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.llms import Ollama

# replace model with the downloaded model you want to use
llm = Ollama(
    model="sparksammy/samai",
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
)

completeContext = ""
# Define URLs for requirements.txt and main.py
REQS_URL = 'https://raw.githubusercontent.com/The-AI-Brain/ai-brain/main/requirements.txt'
MAIN_URL = 'https://raw.githubusercontent.com/The-AI-Brain/ai-brain/main/main.py'

# Define paths for local requirements.txt and main.py files
REQS_PATH = 'requirements.txt'
MAIN_PATH = 'main.py'
List = {}


# Check for updates
def check_updates():
    # Download remote requirements.txt file
    remote_reqs = requests.get(REQS_URL).text
    
    # Compare local and remote requirements.txt files
    with open(REQS_PATH, 'r') as f:
        local_reqs = f.read()
        
    if local_reqs != remote_reqs:
        # Install updated requirements
        subprocess.run(['pip', 'install', '-r', REQS_PATH])
        
        # Download updated main.py file
        remote_main = requests.get(MAIN_URL).text
        
        # Write updated main.py file
        with open(MAIN_PATH, 'w') as f:
            f.write(remote_main)
        
        # Restart the script
        os.execv(sys.argv[0], sys.argv)


emotions = [
    "happy", "sad", "angry", "surprised", "disgusted", "fearful",
    "excited", "nostalgic", "hopeful", "anxious", "relaxed", "curious",
    "confused", "amused", "bored", "ecstatic", "exhausted", "grateful",
    "guilty", "embarrassed", "envious", "proud", "ashamed", "content",
    "depressed", "fascinated", "frustrated", "inspired", "irritated",
    "jealous", "lonely", "melancholic", "optimistic", "overwhelmed",
    "peaceful", "playful", "reflective", "remorseful", "restless",
    "satisfied", "sympathetic", "tense", "terrified", "triumphant",
    "uncomfortable", "vulnerable", "wistful", "yearning", "zealous"
]

# Array of human actions
actions = [
    "walked the dog",
    "cooked dinner",
    "read a book",
    "went swimming",
    "played soccer",
    "listened to music",
    "watched a movie",
    "painted a picture",
    "wrote a story",
    "rode a bike",
    "danced in the rain",
    "visited a museum",
    "went on a road trip",
    "went to a concert",
    "built a sandcastle",
    "went to the beach",
    "played video games",
    "climbed a mountain",
    "played with a pet",
    "went for a run",
    "did yoga",
    "went camping",
    "visited a new city",
    "went to a party",
    "took a nap",
    "had a picnic",
    "played a musical instrument",
    "tried a new food",
    "went on a hike",
    "took a bath",
    "visited a friend",
    "went to a theme park",
    "went to a zoo",
    "went to a sporting event",
    "went to a play",
    "went to a comedy show",
    "went to a ballet",
    "went to a musical",
    "went to a poetry reading",
    "went to a book club meeting",
    "went to a cooking class",
    "went to a painting class",
    "went to a wine tasting",
    "went to a beer festival",
    "went to a farmers' market",
    "went to a flea market",
    "went shopping",
    "went to a garage sale",
    "went to a thrift store",
    "volunteered at a charity",
    "went to a political rally",
    "went to a religious service",
    "attended a wedding",
    "attended a funeral",
    "graduated from school",
    "started a new job",
    "retired from a job",
    "got married",
    "got divorced",
    "had a baby",
    "raised a child",
    "adopted a pet",
    "moved to a new city",
    "bought a house",
    "rented an apartment",
    "remodeled a home",
    "gardened",
    "landscaped a yard",
    "went on a cruise",
    "went on a safari",
    "went on a skiing trip",
    "went on a snowboarding trip",
    "went on a fishing trip",
    "went on a hunting trip",
    "went on a scuba diving trip",
    "went on a surfing trip",
    "went on a kayaking trip",
    "went on a canoeing trip",
    "went on a rafting trip",
    "went on a hot air balloon ride",
    "went on a helicopter ride",
    "went on a plane ride",
    "went on a train ride",
    "went on a road trip",
    "went skydiving",
    "went bungee jumping",
    "went zip lining",
    "went rock climbing",
    "went to a spa",
    "got a massage",
    "got a facial",
    "got a manicure",
    "got a pedicure",
    "went to a chiropractor",
    "went to a physical therapist",
    "went to a dentist",
    "went to a doctor",
    "got surgery",
    "recovered from an illness",
    "overcame an addiction",
    "learned a new skill",
    "learned a new language",
    "took a class",
    "ate",
    "played the piano",
    "went for a walk"
]


# Array of places for the actions
places = [
    "in the park",
    "at home",
    "in the library",
    "on the beach",
    "in the movie theater",
    "at the doctor's office",
    "at school",
    "at the spa",
    "at the airport",
    "at the gym",
    "in a cafe",
    "in a museum",
    "in a grocery store",
    "in a restaurant",
    "at a concert",
    "at a stadium",
    "in a hospital",
    "in a church",
    "in a mosque",
    "in a temple",
    "in a theater",
    "in a nightclub",
    "in a casino",
    "at a zoo",
    "at a theme park",
    "at a water park",
    "in a shopping mall",
    "in a department store",
    "at a gas station",
    "in a parking lot",
    "in a hotel",
    "in a motel",
    "in a hostel",
    "in a campground",
    "in a forest",
    "on a mountain",
    "in a desert",
    "in a valley",
    "by a river",
    "by a lake",
    "at sea",
    "in the ocean",
    "in a cave",
    "at a train station",
    "at a bus station",
    "at a subway station",
    "at a ferry terminal",
    "at a harbor",
    "in a space station",
    "in a laboratory"
]



# Asynchronous function to print actions
def createContext():
    action = random.choice(actions)
    place = random.choice(places)
    completeContext = f"you just did \"{action}\" and did it \"{place}\""
    return complete

@app.get("/context")
async def get_emote():
    return await createContext()

@app.get("/chatin/{chatText}")
async def get_chatin(chatText: str):
    return await main(chatText)

# Main function to run the program
def main(chatin):
    chatin = "Guest:" + chatin
    
    # Get response from ollama
    message = llm(f"(Additional context for reply: {completeContext}), reply to this: {chatin}")
    
    # Print ollama response and what it said
    print(f"You: {chatin}")
    print(f"AI: {message}")
    
    return f"You: {chatin}\n${name}: ${message}"

# Run the cli function

def cli():
    while True:
        check_updates()
        toChat = input("brain@localhost:~$ ")
        main(f"{toChat}")
cli()
