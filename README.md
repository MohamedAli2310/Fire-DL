# Fire-Detection-DL-Model

## Table of Contents
1. [Overview](#Overview)
1. [Product Spec](#Product-Spec)
1. [Wireframes](#Wireframes)
2. [Schema](#Schema)

<p align="center">
  <a href="https://github.com/MohamedAli2310/Fire-Detection-DL-Model" target="_blank">
    <img alt="GitHub release" src="firedl.png">
  </a>

  <a href="https://github.com/navendu-pottekkat/nsfw-filter/commits/master" target="_blank">
    <img src="https://img.shields.io/github/last-commit/navendu-pottekkat/nsfw-filter?style=flat-square" alt="GitHub last commit">
  </a>

  <a href="https://github.com/MohamedAli2310/Fire-Detection-DL-Model/issues" target="_blank">
    <img src="https://img.shields.io/github/issues/navendu-pottekkat/nsfw-filter?style=flat-square&color=red" alt="GitHub issues">
  </a>

  <a href="https://github.com//MohamedAli2310/Fire-Detection-DL-Model/pulls" target="_blank">
    <img src="https://img.shields.io/github/issues-pr/navendu-pottekkat/nsfw-filter?style=flat-square&color=blue" alt="GitHub pull requests">
  </a>

  </br>

  <a href="https://standardjs.com" target="_blank">
    <img alt="ESLint" src="https://img.shields.io/badge/code_style-standard-brightgreen.svg?style=flat-square">
  </a>

  <a href="https://ctt.ac/4e4Jt" target="_blank">
    <img src="https://img.shields.io/twitter/url?style=flat-square&logo=twitter&url=https://ctt.ac/4e4Jt" alt="GitHub tweet">
  </a>
</p>
<hr>

## Overview
### Description
Deep Learning convolutional neural network model to detect fire using built-in/external web cam. The idea is to be able to detect fire without the need for any sensors, just a simple, low quality webcam!
The model plays alarm sound when fire is detected for 15 consecutive frames (1/4 of a second), ensuring that the alarm is not set off incorrectly for false positives.

*This application does NOT collect/send any user data. All frames of the camera video feed are collected and operated on for classification locally and are neither saved locally nor sent to a server for processing.*

<p align="center">
  <img src="firedl.png" alt="logo"/>
</p>

//VIDO goes here

### Program Evaluation
- **Category:** Safety
- **Story:** Allows user to use an external camera attached to any usb port of a computer to monitor the air for smoke and fire. In case of a fire, the program sets a fire alarm off. We plan to integrate smarter action in the case of fire by integrating a fire alarm telegram bot with the software, which has been implemented dbut has yet to be integrated.
- **Market:** This is designed with the people of developing nations in mind. Tens of countries don't have access to sophisticated fire alarms and smoke detectors, and even if they do they are not affordable and not regulated. This piece of software allows users to salvage a webcam from an old laptop, add a usb connector to it, and use it without a problem. The app is not intended for profit and is available as an open source for anyone who can benefit from it.
- **Habit:** If to be used as intended, the app is meant to be run on a daily basis 24/7 for fire detection. It would be much more convenient to upload the software on a dedicated microcontroller then, which is what we are looking for at the moment!
- **Scope:** The scope of this app is local, as you don't need to have an account or internet access to use it. The usage and testing of this app doesn't require more than one user to undertake.

