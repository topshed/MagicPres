#!/usr/bin/env python
import skywriter
import signal
import autopy
import sys

mouse_down = False
#work out how big the screen we're using is.
width, height = autopy.screen.get_size()

@skywriter.move()
def move(x, y, z):
  #print( x, y, z )
  global mouse_down
  if mouse_down: # Only run if we're in drawing mode
      x = (x) * width
      y = (y) * height
      # scale to screen size
      x = int(x)
      y = height - int(y)

      if( y > 799 ):
       y = 799

      autopy.mouse.move(x, y)
      #print( int(x), int(y) )

@skywriter.flick()
def flick(start,finish):
  print('Got a flick!', start, finish)
  if start == "east": # Back through Impress slides
    autopy.key.tap(autopy.key.K_LEFT)
  if start == "west": # Forward through Impress slides
    autopy.key.tap(autopy.key.K_RIGHT)
  if start == "north": # Start slideshow
    autopy.key.tap(autopy.key.K_F5)
  if start == "south": # Quit slideshow
    autopy.key.tap(autopy.key.K_ESCAPE)


@skywriter.double_tap()
def doubletap(position):
  print('Double tap!', position)
  sys.exit() # Emergency stop


@skywriter.tap()
def tap(position):
  global mouse_down
  print('Tap!', position)
  if mouse_down: # Toggle mouse up/dwon
      autopy.mouse.toggle(False)
      mouse_down = False
  else:
      autopy.mouse.toggle(True)
      mouse_down = True

#@skywriter.touch()
#def touch(position):
#  print('Touch!', position)

signal.pause()
