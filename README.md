# webhook-screen
I wrote a little python script that has 3 buttons to control stuff about my Home Assistant. 

It also has a clock and it has a little greeting.

## demo
{{video link here}}

## how
- webhook: edit the webhooks in the script to your own ha webhooks, it'll send a post request to the webhook when you click the button
- clock: it uses the worldtimeapi to get the time and display it on the screen
- greeting: just a text lol

It auto starts using boot.py, where it also configures the WiFi. A boot.py example is at boot.py.example, you can copy it to boot.py and edit it to your own WiFi stuff

## what's mpremote
why do I have this title lol. install mpremote with `pip install --user mpremote`, close all terminals and open a new one. connect your TulipCC and use `mpremote` to get a terminal/shell/whatever it's called. use `mpremote resume fs cp boot.py :boot.py` to copy the boot.py file to your Tulip (it's always the order `local` `tulip` in the command, the : sets wich one is the truth). if you do the : at the first file, it'll copy _from_ the Tulip to your computer. 

## nice I made a readme

-Matthias