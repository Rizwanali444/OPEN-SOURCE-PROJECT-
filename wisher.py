import os, random, time
from datetime import datetime
from gtts import gTTS
from colorama import Fore, init
import urllib.parse
import getpass

init(autoreset=True)

def typeprint(text, color=Fore.YELLOW):
    for ch in text:
        print(color + ch, end='', flush=True)
        time.sleep(0.01)
    print()

def speak(text, filename):
    tts = gTTS(text=text, lang='en', tld='co.in')
    tts.save(filename)
    os.system(f"mpv {filename} > /dev/null 2>&1")

def whatsapp_link(number, name, wishes):
    number = number.strip().replace("0", "92", 1)
    all_wishes = '\n'.join([f"• {wish}" for wish in wishes])
    message = f"🎂 Happy Birthday {name}!\n\n{all_wishes}\n\nStay happy & blessed! 💖"
    link = f"https://wa.me/{number}?text=" + urllib.parse.quote(message)
    os.system(f'termux-open-url "{link}"')

def confetti():
    symbols = "🎉✨💫🎁🎈"
    for _ in range(5):
        print("".join(random.choices(symbols, k=35)))
        time.sleep(0.1)

def countdown(sec=10):
    print(Fore.CYAN + "\n⏳ Starting Countdown...")
    for i in range(sec, 0, -1):
        print(Fore.MAGENTA + f"{i}...", end=' ', flush=True)
        time.sleep(1)
    print("\n")

# ✨ 50+ Unique Wishes
base_wishes = [
    "Wishing you the most magical birthday ever!",
    "May all your dreams come true this year!",
    "Sending lots of love and cake your way!",
    "You’re aging like fine wine – gracefully!",
    "Hope your birthday sparkles like you do!",
    "Your smile lights up everyone’s life!",
    "Wishing you strength, success, and happiness!",
    "May this birthday be your best yet!",
    "Keep shining like the star you are!",
    "Today is your day – make it amazing!",
    "You bring joy to everyone around you!",
    "Birthdays are nature’s way of celebrating you!",
    "One more year of being fabulous!",
    "Sending big birthday hugs your way!",
    "Stay strong, stay bright, stay blessed!",
    "Another year older, wiser, and cooler!",
    "Your heart makes the world a better place!",
    "So many candles, so much light!",
    "Wishing you adventure, laughter, and cake!",
    "Time to party and enjoy your special day!",
    "Let happiness surround you always!",
    "May your journey be filled with joy!",
    "Here's to love, laughter, and another year!",
    "You were born to do amazing things!",
    "Make a wish and blow out the candles!",
    "Thanks for being such an awesome soul!",
    "Stay the amazing person you are!",
    "Here’s to a day full of smiles!",
    "You deserve the best — and more!",
    "A day full of love and celebration awaits!",
    "Cheers to health, happiness, and fun!",
    "Glow up, grow up, and party on!",
    "No one does birthdays better than you!",
    "To the kindest soul – Happy Birthday!",
    "May your cake be sweet and your day sweeter!",
    "Level up! Happy Birthday gamer!",
    "Wishing you sunshine and sparkles!",
    "Today is your personal holiday – celebrate big!",
    "Hope your day is full of giggles and gifts!",
    "Age is just a number, joy is eternal!",
    "Your existence is a blessing – shine on!",
    "Let’s raise a toast to YOU today!",
    "Smiles, laughter, hugs – you deserve all!",
    "You’re officially older and cooler!",
    "Every year, you glow more!",
    "Life loves you – so do we!",
    "The party has started because of YOU!",
    "Wishing you happiness you can hug!",
    "Wishes wrapped in love for you!",
    "You’re proof that kindness is beautiful!"
]

# Start 🎉
os.system("clear")
print(Fore.MAGENTA + "\n🎂Birthday Wishing Tool (Unique Wishes Version)\n")

name = input(Fore.CYAN + "🎉 Enter birthday person's name: ")
print(Fore.CYAN + "📱 Enter WhatsApp number (e.g. 03XXXXXXXXX): ", end='')
number = getpass.getpass('')
now = datetime.now().strftime("%d %B %Y - %I:%M %p")
mp3_file = f"{name}_wish.mp3"

confetti()
countdown(10)

print(Fore.CYAN + "\n🎊 Showing Unique Wishes for 60 Seconds...\n")
unique_wishes = random.sample(base_wishes, 30)
for wish in unique_wishes:
    typeprint(f"➤ {wish}", Fore.YELLOW)
    time.sleep(2)

# ✅ Safe Final Wish Selection
remaining = [w for w in base_wishes if w not in unique_wishes]
final_wish = random.choice(remaining) if remaining else random.choice(base_wishes)

# 🖼️ Text Card
card = f"""
{Fore.LIGHTRED_EX}
╔══════════════════════════════════╗
║        🎂 HAPPY BIRTHDAY 🎂        ║
╠══════════════════════════════════╣
║  Name: {name}                    
║  Date: {now} 
╠══════════════════════════════════╣
║  {final_wish}
╚══════════════════════════════════╝
"""
print(card)

# 🔊 Voice
print(Fore.MAGENTA + "\n🔊 Playing Girl Voice...\n")
speak(f"Happy Birthday {name}! {final_wish}", mp3_file)

# 📤 WhatsApp Send
print(Fore.GREEN + "\n📤 Sending Wishes via WhatsApp...\n")
whatsapp_link(number, name, unique_wishes)

# ✅ Log
with open("wished.txt", "a") as f:
    f.write(f"{name} was wished on {now} at {number}\n")

print(Fore.GREEN + "\n✅ Done! All wishes sent successfully.")
