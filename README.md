# HandUI

### Using machine learning hand tracking to control mouse movement.

This project aimed to create a proof of concept that your hand can be used to interact with a desktop computer in place of a traditional mouse.

It's built on Google's [Mediapipe framework](https://developers.google.com/mediapipe) and uses the PyAutoGUI library to control mouse movement.

In the future, I aim to add a gesture recoginition feature (usihng Mediapipe) which allows users to interact with content on their screen, such as clicking or scrolling. 


## Features

#### Current features:

- Move your hand to move the cursor on a screen
- Visualise how the program interprets  

#### Future features:

- Control mouse clicks or scrolling using gestures
- Customise the way the program works (eg: which gestures activate which features)


## How it works

The program is quite simple. It tracks the position of your hand using the Mediapipe API, translates this into a single coordinate on the screen, then moves the cursor to the correct position. 

At the moment it is not possible to click or scroll using HandUI, this will be added in the future.

To run the main program which controls mouse movement, run:
`python main.py`

To run the tracking visualiser (and in the future the config mode) , run `python app.py`

## Prerequisites

All prerequisites can be seenm in `requirements.txt`

## Limitations

- When using OpenCV for the camera footage, the frame rate is too low to track hand movement smoothly. Therefore, mouse movement looks jagged and clunky.
- The program can only be used to move the cursor.
