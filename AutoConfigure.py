def gatherData():
    # DEFINE EMPTY DICTIONARY
    Settings = {}
    
    # CONFIGURATION
    
    hostname = input("What is the hostname? ")
    secret = input("What is the Priv Exec secret? ")
    banner = input("What is the banner? ")
    username = input("What is the username? ")
    password = input("What is the password? ")
    consolePass = input("Enter console line password or enter 'local' to enable login local: ")
    vtyPass = input("Enter vty line password or enter 'local' to enable login local: ")

    # ASSIGN GATHERED VALUES TO DICTIONARY
    Settings["hostname"] = hostname
    Settings["secret"] = secret
    Settings["banner"] = banner
    Settings["username"] = username
    Settings["password"] = password
    Settings["consolePass"] = consolePass
    Settings["vtyPass"] = vtyPass

    
    # RETURN DICTIONARY
    return Settings
    


    


def buildConfig(settings) :
    
    # BUILD CONFIG FILE
    config = f'''
en
conf t
no ip domain-lookup
service password-encryption
hostname {settings["hostname"]}
enable secret {settings["secret"]}
banner motd # {settings["banner"]} #
username {settings["username"]} password {settings["password"]}

'''
    
    # LINE CONSOLE CONFIG
    # CHECK FOR LOCAL LOGIN
    if settings["consolePass"] == "local":
        consoleConfig = f'''
line con 0
login local
logging sync
exit

        '''
    else :
        consoleConfig = f'''
line con 0
password {settings["consolePass"]}
login
logging sync
exit

        '''
    config = config + consoleConfig

    # VTY LINE CONFIG
    # CHECK FOR LOCAL LOGIN
    if settings["vtyPass"] == "local":
        vtyConfig = f'''
line vty 0 15
login local
logging sync
transport input ssh
exit

        '''
    else :
        vtyConfig = f'''
line vty 0 15
password {settings["vtyPass"]}
login
logging sync
transport input ssh
exit

        '''
    config = config + vtyConfig
    return config

def makeFile(string):
    fileName = input("What is the config file name? ") + ".txt"
    with open(fileName, "w") as file:
        file.write(string)

makeFile(buildConfig(gatherData()))
    