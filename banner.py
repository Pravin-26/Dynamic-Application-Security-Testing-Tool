import pyfiglet

def banner():
    ascii_banner = pyfiglet.figlet_format("Web Scanner Software \n -by Pravin S")
    return ascii_banner

if __name__ == '__main__':
    banner()