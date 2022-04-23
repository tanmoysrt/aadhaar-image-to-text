# Aadhar Kiosk

## Installation Guide

- Install Python
- Create a python virtual enviroment
- Activate enviroment
- Run  `pip install -r requirements.txt` to install all packages
- Run `python main.py`  to run the application


## Communication between Kiosk programme and database searching programme

- Under storage folder there is two files
    - /storage/request.txt
    - /storage/response.txt

- **/storage/request.txt** => hold the current aadhaar no
- **/storage/response.txt** => write the status of trasfer

## Content status guidelines for **/storage/response.txt**

#### If the transfer has been done, put **1**  **Y** in that file

#### If the transfer has not yet done, put **0** or **N** in that file

## Make communication between two programme clash proof

- After reading the aadhaar no from ***/storage/request.txt*** delete the content of the file to remove risk of inifnite loop

- Before writing value to ***/storage/response.txt*** , check existance of the file. If not exists first create the file, then write the fil

- Don't append any new line in the file# aadhaar-image-to-text
