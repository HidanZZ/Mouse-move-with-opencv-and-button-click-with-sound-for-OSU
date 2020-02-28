# Mouse move And 'A' button click with sound

This is a fun project i did when i had free time.
this program uses opencv Hsv tresholding to differentiate the wanted object from the background and taking it's contour centre and translating it to mouse coordinates to move the mouse,
and then when to voice surpass a certain volume the button 'A' is pressed.

### Prerequisites

using python 3.6.9
all the dependencies are in requirements.txt

### How to use

To run the program, just simple run main.py .
You can find the HSV range using the script HsvRangeFinder.py and set the lowerBound and upperBound in the script objectDetection.py .
You can change the Key pressed in the script main.
