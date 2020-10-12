import requests
import json
import pyttsx3

url="https://official-joke-api.appspot.com/random_ten"
response= requests.get(url)
print(response.status_code)

jsonData=json.loads(response.text)
print(jsonData)

class Joke:
    def __init__(self, setup, punchline)->None:
        self.setup=setup
        self.punchline=punchline
        
        
    def __str__(self) -> str:
        return f"setup{self.setup} punchline {self.punchline}"

jokes = []

for j in jsonData:
    setup=j["setup"]
    punchline=j["punchline"]
    joke=Joke(setup, punchline)
    jokes.append(joke)
    
print(f"Got {len(jokes)} jokes")

for joke in jokes:
    print(joke)
    
pyttsx3.speak("Nelan Is A PascLover")