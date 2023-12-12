// variable
let distanceToObject: number = 0

// setup
radio.setGroup(76)
basic.showIcon(IconNames.Happy)

// distanceToObject setup
input.onButtonPressed(Button.A, function () {
  basic.clearScreen()
  distanceToObject = sonar.ping(
    DigitalPin.P1,
    DigitalPin.P2,
    PingUnit.Centimeters
  )
  // if distanceToObject is <= 10 show hello world if more than 10 then show hello universe
  if (distanceToObject <= 10) {
    radio.sendString('hello world')
  } else {
    radio.sendString('hello universe')

    basic.showIcon(IconNames.Happy)
  }
})

// radio.onReceivedString lets this microbit recieve strings from other microbits
radio.onReceivedString(function (receivedString) {
  basic.clearScreen()
  basic.showString(receivedString)
  basic.showIcon(IconNames.Happy)
})
