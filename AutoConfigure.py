def gatherData():
    #Check for switch or router
    while True:
        device = input("Are you configuring a switch or a router? ")
        if device.strip().lower() == "switch" or device.strip().lower() == "router":
            break
        else:
            print("Invalid device entered. Please enter either router or switch.")
    # ROUTER CONFIGURATION
    if device.strip().lower() == "router":
        hostname = input("What is the hostname for the router? ")
        secret = input("What is the Priv Exec secret? ")
        while True:
            lookup = input("Disable DNS lookup? y/n ")
            if lookup == "y":
                lookup = True
                break
            elif lookup == "n":
                lookup = False
                break
            else:
                print("Invalid input entered. Enter either y or n. ")
        print(lookup)
        username = input("What is the username? ")
        password = input("What is the password? ")
        consolePass = input("Enter console line password or enter 'local' to enable login local: ")
        vtyPass = input("Enter vty line password or enter 'local' to enable login local: ")
        while True:
            ssh = input("Enable SSH? y/n ")
            if ssh == "y" or ssh == "n":
                break
            else:
                print("Invalid input entered. Enter either y or n. ")
        while True:
            encrypt = input("Encrypt passwords? y/n ")
            if encrypt == "y" or lookup == "n":
                break
            else:
                print("Invalid input entered. Enter either y or n. ")
        banner = input("What is the banner? ")

    # SWITCH CONFIGURATION
    if device.strip().lower() == "switch":
        hostname = input("What is the hostname for the switch? ")
        secret = input("What is the Priv Exec secret? ")
        while True:
            lookup = input("Disable DNS lookup? y/n ")
            if lookup == "y" or lookup == "n":
                break
            else:
                print("Invalid input entered. Enter either y or n. ")
        username = input("What is the username? ")
        password = input("What is the password? ")
        consolePass = input("Enter console line password or enter 'local' to enable login local: ")
        vtyPass = input("Enter vty line password or enter 'local' to enable login local: ")
        while True:
            ssh = input("Enable SSH? y/n ")
            if ssh == "y" or lookup == "n":
                break
            else:
                print("Invalid input entered. Enter either y or n. ")
        while True:
            encrypt = input("Encrypt passwords? y/n ")
            if encrypt == "y" or lookup == "n":
                break
            else:
                print("Invalid input entered. Enter either y or n. ")
        banner = input("What is the banner? ")
gatherData()
#def buildConfig() -> config(str):
    