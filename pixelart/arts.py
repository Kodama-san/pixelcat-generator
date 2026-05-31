import turtle, random, os, glob
myPen = turtle.Turtle()
myPen.speed(0)
myPen.hideturtle()
turtle.tracer(0, 0)

def makeArt():
  myPen.hideturtle()

  def box(intDim):
    myPen.begin_fill()
    for i in range(3):
        myPen.forward(intDim)
        myPen.left(90)
    myPen.forward(intDim)
    myPen.end_fill()
    myPen.setheading(0)
    
  boxSize = 20
#Position myPen in top left area of the screen
  myPen.penup()
  myPen.goto(-170, 150)
  myPen.setheading(0)

  fur=['#d77d31', '#7f7679', '#4D220E', '#000000', '#ffa500']
  pinky=['#ffc0cb', '#fa9284', '#ffa089', '#ff6e4a', '#fd5e53']
  cloth=['#00b300', '#2c75ff', '#dd4492', '#fde910', '#ff2400', '#9400d3']
  atr1=['#cf99ff', '#c9c5c7', '#dbd7d2', '#afdafc', '#dcd0ff', '#ffff99', '#fad201']
  atr2=['#ffd700', '#7b001c', '#00004d', '#002800', '#310062']
  eyes=['#a8d9ff', '#008000', '#ffbf00', '#cc99ff', '#17002e']
  eyesadd=['#8b4513', '#665e61', '#c9c0bb', '#817066', '#834d18']
  nose=['#f73b23', '#fc6c85', '#c21030', '#33040d', '#f78fa7']
  stars='#ffff00'
  mouth='#ff033e'
  hat='#ffb600'

  palette=[random.choice(fur), random.choice(pinky), random.choice(cloth), random.choice(atr1), random.choice(atr2), random.choice(eyes), random.choice(eyesadd), random.choice(nose), stars, mouth, hat]

  file_list = glob.glob("pixels/*.txt")  # Получаем список элементов папки
  file = random.choice(file_list)
  art = []
  with open(file) as f:
    for line in f:
      art.append([int(x) for x in line.split()])

  for i in range(0, len(art)): #для строки из списка строк от 0 до 15:
    for j in range(0, len(art[i])):#для пикселя в строке от 0 до 15:
      x = art[i][j]
      if x != 0:
        myPen.color(palette[x - 1])
        box(boxSize)
      myPen.goto(-170+(j*boxSize), 150-i*boxSize)

  myPen.getscreen().update()

def cleaning():
  myPen.reset()
  myPen.hideturtle()
