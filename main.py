# ------- STEPS ------
# Step 1 : Show guide to put aadhaar card & show video feed in display
# Step 2 : Show page that will show Aadhaar no in masking XXXX XXXX 3456 and show message to wait for status checking
# Step 3 : Show status and display it for like 10 seconds and then back to step 1

# Upgrade : 
# Add voice feature

# CONFIGURATIONS
SHOW_MASKED_AADHAAAR_NO = False
VIDEO_INPUT = 1
LAUNCH_IN_KIOSK_MODE = True


import eel
import cv2
import pytesseract
from utils import getAdhaarNo, image_to_base64_jpeg
from status_checker import getStatus




eel.init("web")


@eel.expose
def scanAdhaarCard():
    eel.goToPage(0)
    aadhaar_no = ''
    vid = cv2.VideoCapture(VIDEO_INPUT)
    vid.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    vid.set(cv2.CAP_PROP_FRAME_WIDTH, 240)


    while(True):
        _, frame = vid.read()
        frame = cv2.medianBlur(frame,1)

        # Convert to base64 and send to browser
        eel.updateVideoFrame(image_to_base64_jpeg(frame))
    
        # Convert to grayscale for better OCR
        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(grayscale, config='-l eng --dpi 70 -c  tessedit_char_whitelist="0123456789 "')
        ocr_response = getAdhaarNo(text)
        if ocr_response[0]:
            aadhaar_no = str(ocr_response[1])
            vid.release()
            break
    
    # Notify system
    if SHOW_MASKED_AADHAAAR_NO:
        eel.updateAadhaarNoDetailsForKiosk("XXXXXXXX"+aadhaar_no[-4:])
    else:
        eel.updateAadhaarNoDetailsForKiosk(aadhaar_no)

    # Now check for status 
    getAndUpdateStatus(aadhaar_no)




def getAndUpdateStatus(aadhaar_no):
    status = getStatus(aadhaar_no)
    eel.updateStatusFromServer(status)
    

if __name__ == '__main__':
    if LAUNCH_IN_KIOSK_MODE:
        eel.start("main.html",  mode='chrome', cmdline_args=['--kiosk'])
    else:
        eel.start("main.html")
