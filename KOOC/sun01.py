import math
from cs1graphics import *

def animate_sunrise(sun):
  w = canvas.getWidth()   # canvas 가로
  h = canvas.getHeight()  # canvas 세로
  r = sun.getRadius()     # 각도
  x0 = w / 2.0            # sun 가로 중심 위치
  y0 = h + r              # sun 세로 중심 위치
  xradius = w / 2.0 - r   # x 측 반지름(중심점 - r)
  yradius = h             # y 측 반지름
  for angle in range(181):    # 타원 방정식 참고 0 ~ 180도
    rad = (angle/180.0) * math.pi # python 삼각함수는 radian 단위를 씀
    x = x0 - xradius * math.cos(rad)
    y = y0 - yradius * math.sin(rad)
    sun.moveTo(x, y)

canvas = Canvas(600, 200)
canvas.setBackgroundColor("dark blue")

sun = Circle(30)
sun.setFillColor("yellow")
canvas.add(sun)

animate_sunrise(sun)