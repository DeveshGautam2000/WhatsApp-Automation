# This is a Console based WhatsApp Automation module
# that can be used to Send  Messages and Any Kind of Document(img, pdf, etc)
# by Devesh Gautam

# To run this module you need to install the selenium ,time ,pands module
# use command
# pip install selenium
# pip install time
# and
# pip install pandas
# in the terminal


# ----------------HOW TO USE IT------------------------------------------------
# scan the QR code
# then press enter or any other key

# ----------------FILE STRUCTURE OF THE CSV FILE----------------
# number row contains the number of users that we have to send to
# text row contains the text data to be sent
# document row contains the absolute path to the document(images,pdf files, etc)


from selenium import webdriver
from time import sleep
import pandas as pd

# Readind Data from the File
dataFrame = pd.read_csv("data/numbers.csv")

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

input('Enter anything after scanning QR code')


message = "0"
filepath = "0"

for i in range(0, len(dataFrame["number"])):
    # assert data
    recipient_name = str(dataFrame["number"][i])

    if dataFrame["text"][i] != "0":
        message = dataFrame["text"][i]

    if dataFrame["documents"][i] != "0":
        filepath = dataFrame["documents"][i]

    # Search for the recipient
    search_box = driver.find_element("xpath",
                                     '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.send_keys(recipient_name)
    sleep(1)

    dp_box = driver.find_element("xpath", '//div[@class="_13jwn"]')
    dp_box.click()

    sleep(4)

    if message != "0":
        message_box = driver.find_element(
            "xpath", '//div[@class="_3Uu1_"][@tabindex="-1"]')
        message_box.click()
        message_box.send_keys(message)

        send_button = driver.find_element("xpath", '//span[@data-icon="send"]')
        send_button.click()
        message = "0"
        sleep(2)

    if filepath != "0":
        attachment_box = driver.find_element(
            "xpath", '//div[@title = "Attach"]')
        attachment_box.click()

        image_box = driver.find_element("xpath",
                                        '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        image_box.send_keys(filepath)
        sleep(5)

        send_button = driver.find_element(
            "xpath", '//span[@data-icon="send"]')
        send_button.click()
        filepath = "0"
        sleep(2)

sleep(2)
