import re
import cv2
import base64

spaced_aadhaar_no_regex = '\d\d\d\d \d\d\d\d \d\d\d\d'
no_spaced_aadhaar_no_regex = '\d\d\d\d\d\d\d\d\d\d\d\d'


def getAdhaarNo(text:str):
    list1 = re.findall(spaced_aadhaar_no_regex, text)
    list2 = re.findall(no_spaced_aadhaar_no_regex, text)

    final_list = list1 + list2
    if len(final_list) > 0:
        return True, str(final_list[0]).replace(" ","")

    return False, ""

def image_to_base64_jpeg(frame):
    # Convert to base64 and update in webpage
    _, buffer = cv2.imencode('.jpg', frame)
    jpg_as_text = base64.b64encode(buffer)
    return "data:image/jpeg;base64,"+str(jpg_as_text)[2:][:-1]