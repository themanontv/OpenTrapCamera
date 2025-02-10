# OpenTrapCamera
This repository is for an open source wildlife trap camera that sends files to an S3 bucket

## Required Equipment
 - [Raspberry Pi Zero 2 W](https://shop.pimoroni.com/products/raspberry-pi-zero-2-w?variant=42101934587987)
 - [Clipper Hat Mini Pimoroni](https://shop.pimoroni.com/products/clipper-hat-mini?variant=53509959876987)
 - [Adafruit Universal USB / DC / Solar Lithium Ion/Polymer charger - bq24074](https://www.adafruit.com/product/4755)
 - [Night vision camera module for Raspberry Pi](https://shop.pimoroni.com/products/night-vision-camera-module-for-raspberry-pi?variant=12516582817875)
 - [Lithium Ion Battery Pack](https://shop.pimoroni.com/products/high-capacity-lithium-ion-battery-pack?variant=32012684623955)

## Installation
To get this repository installed you will first need to set up the 4G module which will require getting a SIM card for your project. You should follow [this guide](https://learn.pimoroni.com/article/getting-started-with-clipper-hat) for setting up your Clipper HAT Mini. Personally I would reccommend not totally following the guide and using the `/etc/ppp/peers/provider` file itself rather than creating a `/etc/ppp/peers/clipper`. 

> Note: I am planning to automate the above guide

To install the project and its dependancies simply navigate to the repository root and run

```
sudo chmod +x install.sh
sudo ./install.sh
```