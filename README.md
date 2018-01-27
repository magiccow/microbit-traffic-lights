# microbit-traffic-lights
Micropython code to drive LED traffic lights

See the YouTube build & coding video at: 

[https://youtu.be/IC3vtI0BbbQ](https://youtu.be/IC3vtI0BbbQ)

Implements the UK traffic light pattern:
  Red (stop)
  Red + amber
  Green (go)
  Amber (stop)
  Red   etc
  
You need a red LED on P0, yellow LED on P1 and green on P2. I used 39R resistors in series with the LED,
which gives good brightness on the 3V micro:bit.
