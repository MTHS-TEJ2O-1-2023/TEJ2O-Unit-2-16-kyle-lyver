/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Kyle Lyver
 * Created on: Nov 2023
 * This program does bluetooth
*/

// variables
let distanceToObject: number = 0

// setup
radio.setGroup(76)
basic.showIcon(IconNames.Happy)

// on a button press, run the code
input.onButtonPressed(Button.A, function () {
  // finding the distance to the object
  distanceToObject = sonar.ping(
    DigitalPin.P1,
    DigitalPin.P2,
    PingUnit.Centimeters
  )

  // if the object is less than or equal to 10 cm away
  if (distanceToObject <= 10) {
    radio.sendString('Too Close')
    // if the object is more than 10 cm away
  } else {
    radio.sendString('Hi Clara')
  }
}
)

// receiving a message
radio.onReceivedString(function (receivedString) {
  basic.clearScreen()
  basic.showString(receivedString)
  basic.showIcon(IconNames.Happy)
})
