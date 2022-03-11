from pyfirmata import ArduinoMega, util
from pyfirmata.util import Iterator
import time

port = 'COM6'
board = ArduinoMega(port)

it = util.Iterator(board)
it.start()



while True:
    board.analog[0].enable_reporting()
    print(board.analog[0].read())
    time.sleep(0.5)




