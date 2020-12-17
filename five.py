import time
from tkinter import *
from planets.sun import *
from planets.mercury import *
from planets.venus import *
from planets.earth import *
from planets.mars import *
from planets.moon import *
from planets.deimos import *
from planets.phobos import *

root = Tk()
root.resizable(width=False, height=False)

 
c = Canvas(root, width=700, height=500, bg='#000000')
c.focus_set()
c.pack()

def esc(event):
    root.destroy()
root.bind('<Escape>', esc)

sun = Sun(c, None, 20, 0.002, 0, 'orange')
mercury = Mercury(c, sun, 3, 58, 0.416, 'orange')
venus = Venus(c, sun, 5, 108, 0.416, 'red')
earth = Earth(c, sun, 6, 150, 0.1, 'blue')
moon = Moon(c, earth, 2, 15, 1.3, 'grey')
mars = Mars(c, sun, 4, 228, 0.053, 'red')
deimos = Deimos(c, mars, 1, 12, 30.4, 'blue')
phobos = Phobos(c, mars, 1, 7, 114.4, 'gray')

sun.addSatellites(mercury)
sun.addSatellites(venus)
sun.addSatellites(earth)
earth.addSatellites(moon)
sun.addSatellites(mars)
mars.addSatellites(phobos)
mars.addSatellites(deimos)

# sys.setrecursionlimit(25000)

sun.draw()
# earth.step()

def drawEarth():
  mercury.step()
  venus.step()
  earth.step()
  mars.step()
  moon.step()
  deimos.step()
  phobos.step()
  root.after(1, drawEarth)
 
 
def main():
    drawEarth()
    root.mainloop()
 
main()
# while True:
#   earth.step()
#   time.sleep(0.1)
 
root.mainloop()