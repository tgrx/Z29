import platform

SEP = "\\" if platform.system() == "Windows" else "/"

COINAGE = {
    "Penny": 1,
    "Nickel": 5,
    "Dime": 10,
    "Quarter": 25,
    "Half dollar": 50,
    "1$ Bill": 100,
    "2$ Bill": 200,
    "5$ Bill": 500,
    "10$ Bill": 1000,
    "20$ Bill": 2000,
    "50$ Bill": 5000,
    "100$ Bill": 10000,
}
