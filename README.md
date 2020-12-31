# Zoom Bot

*It is a simple Python automation which will open Zoom app according to the time table given and join the meetings and wait till the the next meeting and repeat for whole day for every meeting.*

> **Disclaimer: This will only join the meeting and nothing else.**

## Prerequisites

- Python 3 Download [here](https://www.python.org/downloads)

- Zoom App
  - Login to your account

- In App Settings [🔵] [🟢]
  - Video > Turn off my video when joining meeting
  - Audio > Automatically join audio by computer when joining a meeting

# Installation and Requirements

- Clone the repo
  - Using HTTPS

      ```sh
      git clone https://github.com/DeeshanSharma/Zoom-Bot.git
      ```

  - Using SSH

      ```sh
      git clone git@github.com:DeeshanSharma/Zoom-Bot.git
      ```

OR

- Download as ZIP [here](https://github.com/DeeshanSharma/Zoom-Bot/archive/master.zip)

- Setup your Virtual Environment [🔵]

    ```sh
    python -m venv .venv
    ```

- Activate your Virtual Environment [⭐]
  - Windows (CMD)

      ```sh
      .venv/Scripts/activate.bat
      ```

- Install using requirements.txt [🟢]

    ```sh
    pip install -r requirements.txt
    ```

# Usage [⭐]

1. Add your time table in the [timetable.json](timetable.json) file 5 minutes late from the actual time (must be multiple of 5).
2. Add your meeting ID and meeting password in [link.py](link.py) file.
3. Change you Zoom app location according to your system in [main.py](main.py) file

## App Support

This app is tested and works on:

- Windows 10

# Future Plans

- Integrated voice engine that will recognise your name called and respond to it

- Function to send text in the chat box similar to what majority is sending

- Send you notification when joining a meeting with certain details (This is still possible but on Discord so not implemented)

- Auto exit the app after attending all the meetings

# Terminology

⭐ - Very Important

🟢 - Recommended

🔵 - Optional

[⭐]: #Terminology
[🟢]: #Terminology
[🔵]: #Terminology