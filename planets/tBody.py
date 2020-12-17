from math import sin, cos

class TBody:
  _planet_liveTime = 0
  _planet_ = None
  _planet_xx = 0
  _planet_yy = 0
  _planet_x = 0
  _planet_y = 0
  _planet_center = None
  _planet_orbitRadius = 0.002
  _planet_rotationalSpeed = 0
  _planet_size = 0
  _planet_bodyColor = 'orange'
  _fild_ = None
  _fild_size_x = 700
  _fild_size_y = 500

  def __init__(self, fild, planetCenter, planetSize, planetOrbitRadius, planetRotationalSpeed, planetBodyColor):
    self._fild_ = fild
    self._planet_size = planetSize * 2
    self._planet_center = planetCenter
    self._planet_orbitRadius = planetOrbitRadius * 2
    self._planet_xx = planetOrbitRadius * 2
    self._planet_rotationalSpeed = planetRotationalSpeed
    self._planet_bodyColor = planetBodyColor
    self.planetLocationFromSenter()
    self._planet_satellites = []
    self._planet_orbits = []

  def planetLocationFromSenter(self):
    self._planet_x = self._fild_size_x/2 - self._planet_size/2
    self._planet_y = self._fild_size_y/2 - self._planet_size/2
    self._planet_x = self._planet_x + self._planet_orbitRadius/2

  def drawRadius(self, radius):
    self._planet_orbits.append(self._fild_.create_oval(
      (self._fild_size_x/2 + self._planet_orbitRadius/2 - radius/2) - 1,
      (self._fild_size_y/2 - radius/2) - 1,
      (self._fild_size_x/2 + self._planet_orbitRadius/2 + radius/2) + 1,
      (self._fild_size_y/2 + radius/2) + 1,
      fill='white'
    ))
    self._planet_orbits.append(self._fild_.create_oval(
      self._fild_size_x/2 + self._planet_orbitRadius/2 - radius/2 + 1,
      self._fild_size_y/2 - radius/2 + 1,
      self._fild_size_x/2 + self._planet_orbitRadius/2 + radius/2 - 1,
      self._fild_size_y/2 + radius/2 - 1,
      fill='black'
    ))

  def drawPlanet(self):
    self._planet_ = self._fild_.create_oval(
      self._planet_x + (self._planet_center._planet_orbitRadius/2 if self._planet_center is not None else 0),
      self._planet_y,
      self._planet_x + self._planet_size + (self._planet_center._planet_orbitRadius/2 if self._planet_center is not None else 0),
      self._planet_y + self._planet_size,
      fill=self._planet_bodyColor
    )

  def addSatellites(self, satellites):
    self._planet_satellites.append(satellites)

  def draw(self):
    listRadius = []
    for satellites in self._planet_satellites:
      listRadius.append(satellites._planet_orbitRadius)
    
    listRadius.sort(reverse=True)

    for radius in listRadius:
      self.drawRadius(radius)

    self.drawPlanet()

    for satellites in self._planet_satellites:
      satellites.draw()

  def step(self):
    self._planet_liveTime += 0.1
    w = (self._planet_rotationalSpeed * 2) / self._planet_orbitRadius
    f = w * self._planet_liveTime
    
    self._fild_.move(
      self._planet_,
      ((self._planet_orbitRadius * cos(f)) - self._planet_xx)/2,
      ((self._planet_orbitRadius * sin(f)) - self._planet_yy)/2
    )

    for orbit in self._planet_orbits:
      self._fild_.move(
        orbit,
        ((self._planet_orbitRadius * cos(f)) - self._planet_xx)/2,
        ((self._planet_orbitRadius * sin(f)) - self._planet_yy)/2
      )

    for satellites in self._planet_satellites:
      self._fild_.move(
        satellites._planet_,
        ((self._planet_orbitRadius * cos(f)) - self._planet_xx)/2,
        ((self._planet_orbitRadius * sin(f)) - self._planet_yy)/2
      )

    self._planet_xx = self._planet_orbitRadius * cos(f)
    self._planet_yy = self._planet_orbitRadius * sin(f)