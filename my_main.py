# my_main.py
# Author: Sebastian Cooper

from my_assistant import TournamentAssistant
from my_tool import TournamentLookup

TOURNAMENT_INFO = {
    "time": "The tournament starts at 9:00 AM.",
    "location": "The tournament takes place in Tampa, Florida.",
    "players": "The tournament allows up to 80 players.",
    "courts": "There will be 8 pickleball courts available.",
}

tournament_tool = TournamentLookup(TOURNAMENT_INFO)

bot = TournamentAssistant(
    "PickleBot",
    "You help customers find information about a pickleball tournament.",
    tournament_tool,
)

print("Welcome to PickleBot!")
print("Type quit to stop.")

user_message = input("You: ")

while user_message.lower() != "quit":
    print(f"{bot.name}: {bot.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(bot.history)}")
