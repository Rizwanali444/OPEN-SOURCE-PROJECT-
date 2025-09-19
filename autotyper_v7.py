import time, sys, os, random
from colorama import init, Fore

init(autoreset=True)

# Line-by-line color cycle
line_colors = [Fore.GREEN, Fore.RED, Fore.BLUE, Fore.YELLOW]

# Slow realistic typing speed
def typing_simulator_line(line, color, speed=0.02):  # ← slowed down
    for char in line:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# Fake hacker log
def fake_log():
    logs = [
        "[+] AI shell injected...",
        "[*] Overclocking terminal...",
        "[+] Decoding matrix...",
        "[*] Mimicking terminal session...",
        "[+] Shadow mode active...",
        "[*] Injecting Nano Kernel..."
    ]
    typing_simulator_line(random.choice(logs), Fore.MAGENTA, 0.005)
    time.sleep(0.3)

# Fake typing prompt
def show_keyboard_typing(line):
    for char in line:
        sys.stdout.write(Fore.CYAN + f"\r⌨️ Typing: {char}   ")
        sys.stdout.flush()
        time.sleep(0.06)
    sys.stdout.write("\r" + " " * 40 + "\r")

def main():
    os.system("clear")
    typing_simulator_line("📁 Enter script file path (e.g. /sdcard/code.py): ", Fore.WHITE, 0.015)
    file_path = input().strip()

    if not os.path.exists(file_path):
        typing_simulator_line("❌ File not found. Exiting...", Fore.RED, 0.02)
        return

    os.system("clear")
    typing_simulator_line(f"🔓 Target Acquired: {file_path}", Fore.YELLOW, 0.02)
    time.sleep(1)

    for _ in range(3):
        fake_log()

    typing_simulator_line("\n⌨️ Starting hacker-style slow typing...\n", Fore.CYAN, 0.02)
    time.sleep(1)

    with open(file_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            color = line_colors[i % len(line_colors)]
            show_keyboard_typing(line.strip())
            typing_simulator_line(line, color, speed=0.02)
            if random.randint(1, 5) == 3:
                fake_log()

    typing_simulator_line("\n✅ ACCESS GRANTED — Script typed successfully", Fore.GREEN, 0.03)

if __name__ == "__main__":
    main()

