from graphics import *;
class Person:
  autoflush=False
  def __init__ (self,x,y,headRadius,bodyLength,legLength,armLength,face=0):
    self.circle = Circle(Point(x,y),headRadius)
    self.body = Line(Point(x,y+headRadius),Point(x,y+headRadius+bodyLength))
    self.leg1 = Line(Point(x,y+headRadius+bodyLength),Point(x-(legLength*0.7),y+headRadius+bodyLength+(legLength*0.7)))
    self.leg2 = Line(Point(x,y+headRadius+bodyLength),Point(x+(legLength*0.7),y+headRadius+bodyLength+(legLength*0.7)))
    self.arm1 = Line(Point(x,y+headRadius+(bodyLength/3)),Point(x-(armLength*0.7),y+headRadius+(bodyLength/3)+(armLength*0.7)))
    self.arm2 = Line(Point(x,y+headRadius+(bodyLength/3)),Point(x+(armLength*0.7),y+headRadius+(bodyLength/3)+(armLength*0.7)))
    self.face=1
    if (armLength>legLength&armLength>headRadius*2):
      widthDeterminer = armLength*0.7
    elif (legLength>armLength&legLength>headRadius*2):
      widthDeterminer = legLength*0.7
    else:
      widthDeterminer = headRadius*2
    self.width = widthDeterminer
    if ((armLength*0.7)-(bodyLength*(2/3))>legLength*0.7):
      lengthDeterminer = (armLength*0.7)-(bodyLength*(2/3))
    else:
      lengthDeterminer = legLength*0.7
    self.length = (headRadius*2)+bodyLength+lengthDeterminer
    if (face==":|"):
      self.eye1 = Point(x-(headRadius/2),y-(headRadius/2))
      self.eye2 = Point(x+(headRadius/2),y-(headRadius/2))
      self.mouth = Line(Point(x-(headRadius/2),y+(headRadius/2)),Point(x+(headRadius/2),y+(headRadius/2)))
    else:
      self.face=0
  def draw(self,window):
    self.circle.draw(window)
    self.body.draw(window)
    self.leg1.draw(window)
    self.leg2.draw(window)
    self.arm1.draw(window)
    self.arm2.draw(window)
    if (self.face!=0):
      self.eye1.draw(window)
      self.eye2.draw(window)
      self.mouth.draw(window)
  def undraw(self):
    self.circle.undraw()
    self.body.undraw()
    self.leg1.undraw()
    self.leg2.undraw()
    self.arm1.undraw()
    self.arm2.undraw()
    if (self.face!=0):
      self.eye1.undraw()
      self.eye2.undraw()
      self.mouth.undraw()
  def getLength(self):
    print(self.length)
  def getWidth(self):
    print(self.width)
  #def move(self,dx,dy):
  #def setFace()
    
win = GraphWin("person",500,500)
person1 = Person(50,100,10,20,10,10)
person2 = Person(100,200,10,20,10,10)
person1.draw(win)
person1.getLength()
