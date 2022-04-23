import eel

def wipeoutresponse():
    with open("./storage/response.txt", "w") as file:
        file.write("-1")
        file.close()

def getStatus(aadhaar_no):
    with open("./storage/request.txt", "w") as file:
        file.write(aadhaar_no)
        file.close()

    content = ""
    while True:
        try:
            with open("./storage/response.txt", "r") as file:
                content = str(file.readline()).strip()
                if content == "" or content == "-1":
                    eel.sleep(1)
                else:
                    break
                file.close()
        except:
            wipeoutresponse()
    wipeoutresponse()
    if content == 'y' or content == 'Y' or content == 'true' or content == 'True' or content == True or content == '1' or content == 1:
        return True
    return False