/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Kyle Lyver
 * Created on: Dec 2023
 * This program sends bluetooth messages
*/

let distanceToObject: number = 0
radio.setGroup(1)

while (true) {
  if (input.buttonIsPressed(Button.A) === true) {
    // find distance from sonar
    basic.clearScreen()
    distanceToObject = sonar.ping(
      DigitalPin.P1,
      DigitalPin.P2,
      PingUnit.Centimeters
    ) 
    basic.showNumber(distanceToObject)
    basic.showIcon(IconNames.Happy)
    if (distanceToObject <= 10) {
      radio.sendString("Too Close")
    }
  }
  radio.onReceivedString(function (receivedString) {
    basic.clearScreen()
    basic.showString(receivedString)
    basic.showIcon(IconNames.Happy)
  })
}
