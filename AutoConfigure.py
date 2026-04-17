import re
ipv4_pattern = r"^(?:0|[1-9]\d?|1\d{2}|2[0-4]\d|25[0-5])(?:\.(?:0|[1-9]\d?|1\d{2}|2[0-4]\d|25[0-5])){3}$"

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
    while True:
        dhcp = input("Would you like to conifgure DHCP? y/n ")
        if dhcp == "y":
            dhcp = True
            break
        elif dhcp == "n":
            dhcp == False
            break
        else:
            print("ERROR: Invalid input detected. Please enter either 'y' or 'n'. ")
    while True:
            try:
                while True:
                    dhcpNumber = int(input("How many DHCP Pools are you configuring? "))
                    if dhcpNumber <= 0:
                        print("ERROR: Invalid input detected. Enter a number greater than 0. ")
                    else:
                          break
                
                break
            except ValueError:
                    print("ERROR: Invalid input detected. Enter an integer. ")
    for i in range(dhcpNumber):
        dhcpPool = input("What is the name of the DHCP Pool? ")
        while True:
            excludeStart = input("Where should the excluded address start? (xxx.xxx.xxx.xxx)")
            if re.fullmatch(ipv4_pattern,excludeStart):
                break
            else:
                print("ERROR: Input does not match the format for an ipv4 address.")
        while True:
            excludeEnd = input("Where should the excluded address end? (xxx.xxx.xxx.xxx)")
            if re.fullmatch(ipv4_pattern,excludeEnd):
                break
            else:
                print("ERROR: Input does not match the format for an ipv4 address.")
        while True:
            defaultRouter = input("What is the default router? (xxx.xxx.xxx.xxx)")
            if re.fullmatch(ipv4_pattern,defaultRouter):
                break
            else:
                print("ERROR: Input does not match the format for an ipv4 address.")
        while True:
            network = input("What is the network address? (xxx.xxx.xxx.xxx)")
            subnet = input("What is the subnet mask? (xxx.xxx.xxx.xxx)")
            if re.fullmatch(ipv4_pattern,network):
                break
            else:
                print("ERROR: Input does not match the format for an ipv4 address.")
            if re.fullmatch(ipv4_pattern,subnet):
                break
            else:
                print("ERROR: Input does not match the format for a subnet mask.")
        
        Settings["dhcpPool" + str(i)] = dhcpPool
        Settings["excludeStart" + str(i)] = excludeStart
        Settings["excludeEnd" + str(i)] = excludeEnd
        Settings["defaultRouter" + str(i)] = defaultRouter
        Settings["network" + str(i)] = network
        Settings["subnet" + str(i)] = subnet

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

#TEST OUTPUT    
#print(gatherData())

    


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

    dhcpNumber = 0
    while True:
        
        if "dhcpPool"+ str(dhcpNumber) in settings:
            dhcpConfig = f'''
ip dhcp exclude {settings["excludeStart"+str(dhcpNumber)]} {settings["excludeEnd"+str(dhcpNumber)]} 
ip dhcp pool {settings["dhcpPool"+str(dhcpNumber)]} 
network {settings["network"+str(dhcpNumber)]} {settings["subnet"+str(dhcpNumber)]} 
default-router {settings["defaultRouter"+str(dhcpNumber)]} 

    '''
            #DHCP CONFIGURATION
            dhcpNumber += 1
            config = config + dhcpConfig
        else:
            break

    return config


# MAKE THE CONFIGURATION FILE
def makeFile(string):
    fileName = input("What is the config file name? ") + ".txt"
    with open(fileName, "w") as file:
        file.write(string)

makeFile(buildConfig(gatherData()))
    