# Command line test tool for HC-SR04 ultrasinoc sensor

## What is this

This ` python ` srcipt is a small test tool to demonstrate how to use the HC-SR04 or similar ultrasonic sensor connected with Raspberry Pi via GPIO ports.

The goal of this project is to play with the sensor as simply as possible but you can use it for more serious calibration purposes as well. It's only up to you.

## Installation

1. Download or clone this repository.

2. Get ` python3-rpi.gpio ` if you don't already have it.

3. Wire your ultrasonic sensor according to its documentation. You can ` ECHO ` and ` TRIG ` constants as the pin of **echo** and **trigger** wires (respecitvely) to follow your real-life wiring.

## Usage

Just run the script without any command-line argument and enjoy what you're seeing.

## Fine tuning

You can set some variables to personalyse the script or to measure your sensor's performance.

- ` GPIO_STYLE ` The style of identifying the pins. We're using ` GPIO.BOARD ` but any other style is just fine. If you change this value keep in mind to change the pin Ids too.
- ` ECHO ` Echo signal receiver pin's Id.
- ` TRIG ` Trigger signal sender pin's Id. 
- ` TRIGGER_CALM_DOWN ` Duration in seconds till no signal is sent to the sensor before the measurement cycle. You might experience smaller values lead to unexpected inaccuracy or even to unsuccessful measurment.
- ` TRIGGER_SIGNAL ` Duration of the trigger signal in senconds.
- ` SENSOR_SCALER ` Scaler value to multiply the measured time interval with. The ground of this value is the speed of sound but different circumstances may validates much different values as well.
