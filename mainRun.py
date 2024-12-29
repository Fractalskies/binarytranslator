import translatorMain

try:
    translatorMain.start()
except ValueError:
    print("Please enter only a binary code value.")