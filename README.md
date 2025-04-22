# ChatMaster_WhatsApp
Automation using python and neural networks to receive messages and send responses automatically. Uses pyperclip, pyautogui and os modules for automated keyboard operations, automated mouse operations and opening WhatsApp web.

Requirements:

  1. Python
     Recommended version : 3.10.11 

  2. Required modules
     inside the ChatMaster_WhatsApp directory, the requirements.txt file contains all the required modules (might be more than required) with exact versions.
     Run the following command in Command prompt or any terminal(worked for command prompt):     pip install -r requirements.txt



Directory System or structure:

   Model/Dataset/    : contains the dataset in a json format. Populary known as intents file which consists of tags(class), patterns(queries) and responses(replies).
   Model/files/      : contains processed data and saved model to eliminate the duration for re-training the same model on same data.
   Model/images/     : contains all the images for image detections in WhatsApp web. These images are of the WhatsApp web version 2.2212.8.
                       These images might need changes in further updates

Python Files inside Model Directory:
  1. trainer.py : for processing the dataset and training the Sequential model of mainly 3 layers.
  2. bot_model.py : Extract and work on processed data and saved model.
  3. GUIApp.py : Basic GUI program to check the responses accuracy.
  4. Opener1.py : Program for defining automation functions of opening WhatsApp web, detecting new messages, copying the whole message and sending a response if possible(can not send messages where messaging is not enabled).
  5. Main.py : GUI implementation of the automation functions.

Execution:
1. Run the trainer.py for processing the dataset and training the model.
2. Run the GUIApp.py for testing the accuracy of the model.
3. Run the Main.py to start working with your whatsapp web account. You will need to login in the whatsapp web while the program has a sleep time of 40 to 45 seconds.
4. After a complete execution, click on the start button again if needed.
