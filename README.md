# Fire-Detection-DL-Model

## Table of Contents
1. [Overview](#Overview)
1. [Product Spec](#Product-Spec)
1. [Wireframes](#Wireframes)
2. [Schema](#Schema)

## Overview
### Description
Deep Learning convolutional neural network model to detect fire using built-in/external web cam. The idea is to be able to detect fire without the need for any sensors, just a simple, low quality webcam!
The model plays alarm sound when fire is detected for 15 consecutive frames (1/4 of a second), ensuring that the alarm is not set off incorrectly for false positives.

*This application does NOT collect/send any user data. All frames of the camera video feed are collected and operated on for classification locally and are neither saved locally nor sent to a server for processing.*

//VIDO goes here

### Program Evaluation
- **Category:** Safety
- **Story:** Allows user to use an external camera attached to any usb port of a computer to monitor the air for smoke and fire. In case of a fire, the program sets a fire alarm off. We plan to integrate smarter action in the case of fire by integrating a fire alarm telegram bot with the software, which has been implemented dbut has yet to be integrated.
- **Market:** This is designed with the people of developing nations in mind. Tens of countries don't have access to sophisticated fire alarms and smoke detectors, and even if they do they are not affordable and not regulated. This piece of software allows users to salvage a webcam from an old laptop, add a usb connector to it, and use it without a problem. The app is not intended for profit and is available as an open source for anyone who can benefit from it.
- **Habit:** If to be used as intended, the app is meant to be run on a daily basis 24/7 for fire detection. It would be much more convenient to upload the software on a dedicated microcontroller then, which is what we are looking for at the moment!
- **Scope:** The scope of this app is local, as you don't need to have an account or internet access to use it. The usage and testing of this app doesn't require more than one user to undertake.

