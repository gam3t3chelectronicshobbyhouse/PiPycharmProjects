## simple I2C Test on a 4x20 lcd - remove lines 3 and 4 if using a 2x16

import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("Hello World!", 1)
mylcd.lcd_display_string("Hello World!", 2)
mylcd.lcd_display_string("Hello World!", 3)
mylcd.lcd_display_string("Hello World!", 4)