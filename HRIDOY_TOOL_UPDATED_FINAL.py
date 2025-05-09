
import os
import time

def logo():
    os.system("clear")
    print("""\033[1;35m
██╗  ██╗██████╗ ██╗██████╗  ██████╗ ██╗   ██╗
██║  ██║██╔══██╗██║██╔══██╗██╔═══██╗╚██╗ ██╔╝
███████║██████╔╝██║██║  ██║██║   ██║ ╚████╔╝ 
██╔══██║██╔══██╗██║██║  ██║██║   ██║  ╚██╔╝  
██║  ██║██║  ██║██║██████╔╝╚██████╔╝   ██║   
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═════╝  ╚═════╝    ╚═╝  
       WELCOME TO HRIDOY TOOLS
\033[0m""")

def speak_and_play():
    os.system("termux-tts-speak 'Welcome to HRIDOY Tools'")
    print("\033[1;34m[+] Downloading & Playing Music...\033[0m")
    if not os.path.exists("song.mp3"):
        os.system("yt-dlp -x --audio-format mp3 -o 'song.%(ext)s' 'https://youtu.be/NKZrXd9tw-Y?si=Bq3F2JdO0KbAXROc'")
    os.system("mpv song.mp3")

def menu():
    print("""\033[1;33m
[1] BASIC SETUP
[2] FULL SETUP (All Tools for Facebook, Termux etc.)
[3] CONTACT-BOSS HRIDOY (WhatsApp)
[0] EXIT
\033[0m""")

def basic_setup():
    print("\n\033[1;36m[+] Running Basic Setup...\033[0m")
    os.system("pkg update -y && pkg upgrade -y")
    os.system("pkg install -y python git curl wget nano neofetch termux-api ffmpeg mpv")
    os.system("pip install yt-dlp")
    print("\033[1;32m[✓] Basic setup complete.\033[0m")

def full_setup():
    print("\n\033[1;36m[+] Running Full Termux Setup (Custom Commands)...\033[0m")
    
    commands = [
        "pkg update && pkg upgrade -y",
        "pkg install git python python2 -y",
        "pkg install wget ruby proot clang -y",
        "termux-setup-storage",
        "apt install php git golang -y",
        "apt install nano cmatrix -y",
        "pkg install figlet cowsay toilet -y",
        "gem install lolcat",
        "pkg install curl unzip openssh tor net-tools unrar w3m proot -y",
        "pip2 install wget requests",
        "pkg install pacman4console vim -y",
        "pip install colorama bundle",
        "gem install bundle bundler",
        "pip install --upgrade pip",
        "pkg install texinfo -y",
        "info > commands.txt && cat commands.txt",
        "pkg --check-mirror update",
        "pkg install fish -y",
        "apt install ruby php golang clang dart -y",
        "pkg clean",
        "apt autoremove"
    ]

    for cmd in commands:
        print(f"\033[1;34m[+] Executing:\033[0m {cmd}")
        os.system(cmd)

    print("\033[1;32m[✓] Full setup complete with all custom tools!\033[0m")

def contact_boss():
    print("\033[1;36m[+] Opening WhatsApp chat with Boss HRIDOY...\033[0m")
    os.system("xdg-open https://wa.me/8801768787067")

# --- Main Execution ---
logo()
speak_and_play()

while True:
    menu()
    choice = input("\n\033[1;36mEnter your choice:\033[0m ")

    if choice == "1":
        basic_setup()
    elif choice == "2":
        full_setup()
    elif choice == "3":
        contact_boss()
    elif choice == "0":
        print("\n\033[1;31m[!] Exiting... Boss HRIDOY signing off!\033[0m")
        break
    else:
        print("\033[1;31m[!] Invalid choice! Try again.\033[0m")

    input("\n\033[1;33mPress Enter to return to menu...\033[0m")
