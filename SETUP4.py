import os
import sys
import time
import threading
from colorama import Fore, Style, init

init(autoreset=True)

def slow(text, delay=0.01):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def spinner_loading(stop_event, text="Installing", delay=0.1):
    spinner = ['⠋','⠙','⠹','⠸','⠼','⠴','⠦','⠧','⠇','⠏']
    colors = [Fore.BLUE, Fore.RED, Fore.GREEN, Fore.YELLOW]
    i = 0
    while not stop_event.is_set():
        color = colors[i % len(colors)]
        sys.stdout.write(f"\r{color}{spinner[i % len(spinner)]} {text}{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(delay)
        i += 1
    sys.stdout.write('\r' + ' ' * (len(text) + 5) + '\r')
    sys.stdout.flush()

banner = f"""{Fore.MAGENTA}
████████ ███████ ██████  ███    ███ ██    ██ ██   ██ ███████ ███████ ████████ ██    ██ ██████  
   ██    ██      ██   ██ ████  ████ ██    ██  ██ ██  ██      ██         ██    ██    ██ ██   ██ 
   ██    █████   ██████  ██ ████ ██ ██    ██   ███   ███████ █████      ██    ██    ██ ██████  
   ██    ██      ██   ██ ██  ██  ██ ██    ██  ██ ██       ██ ██         ██    ██    ██ ██      
   ██    ███████ ██   ██ ██      ██  ██████  ██   ██ ███████ ███████    ██     ██████  ██      
                                                                                              
{Style.RESET_ALL}
{Fore.GREEN}╔════════════════════════════════════════════════════╗
║        Termux Ultimate Setup Tool - By Arnold Team ║
╚════════════════════════════════════════════════════╝
"""

def install_termux_packages():
    packages = [
        "python", "python3", "fish", "ruby", "git", "php", "perl", "nmap",
        "bash", "clang", "nano", "w3m", "hydra", "figlet", "cowsay", "curl",
        "tar", "zip", "unzip", "tor", "wget", "wcalc", "bmon", "golang",
        "openssl", "cmatrix", "openssh", "wireshark", "toilet", "sl", "vim",
        "zsh", "fortune"," tch"
    ]
    for pkg in packages:
        stop_event = threading.Event()
        loader_thread = threading.Thread(target=spinner_loading, args=(stop_event, f"Installing {pkg}", 0.08))
        loader_thread.start()
        os.system(f"pkg install {pkg} -y")
        stop_event.set()
        loader_thread.join()
        print(f"{Fore.CYAN}Installed {Fore.YELLOW}{pkg}{Style.RESET_ALL}")

def install_python_packages():
    packages = [
        "requests", "mechanize", "futures", "urllib3", "rich",
        "bs4", "certifi", "idna", "lolcat", "colorama",
        "termcolor", "httpx", "pyfiglet"
    ]
    for pkg in packages:
        stop_event = threading.Event()
        loader_thread = threading.Thread(target=spinner_loading, args=(stop_event, f"Pip installing {pkg}", 0.08))
        loader_thread.start()
        os.system(f"pip install {pkg}")
        stop_event.set()
        loader_thread.join()
        print(f"{Fore.CYAN}Pip installed {Fore.YELLOW}{pkg}{Style.RESET_ALL}")

def uninstall_and_reinstall_requests_stack():
    print(f"{Fore.BLUE}[{Fore.YELLOW}!{Fore.BLUE}] Rebuilding requests environment...")
    os.system("pip uninstall requests chardet urllib3 idna certifi -y")
    os.system("pip install chardet urllib3 idna certifi requests")

def termux_storage_setup():
    stop_event = threading.Event()
    loader_thread = threading.Thread(target=spinner_loading, args=(stop_event, "Setting up Termux storage", 0.08))
    loader_thread.start()
    os.system("termux-setup-storage")
    stop_event.set()
    loader_thread.join()
    print(f"{Fore.GREEN}Termux storage setup complete.{Style.RESET_ALL}")

def update_system():
    stop_event = threading.Event()
    loader_thread = threading.Thread(target=spinner_loading, args=(stop_event, "Updating system", 0.08))
    loader_thread.start()
    os.system("pkg update -y && pkg upgrade -y && apt update -y && apt upgrade -y")
    stop_event.set()
    loader_thread.join()
    print(f"{Fore.GREEN}System update & upgrade complete.{Style.RESET_ALL}")

def main():
    os.system("clear")
    print(banner)
    input(f"{Fore.YELLOW}Press Enter to start the Ultimate Termux Setup...{Style.RESET_ALL}")
    slow(f"{Fore.CYAN}Starting Ultimate Termux Setup...\n")
    update_system()
    install_termux_packages()
    install_python_packages()
    uninstall_and_reinstall_requests_stack()
    termux_storage_setup()
    slow(f"\n{Fore.GREEN}[✓] Setup completed successfully!")
    print(f"{Fore.CYAN}Follow {Fore.YELLOW}@B {Fore.CYAN}for more Termux tools and updates!")

if __name__ == "__main__":
    main()
