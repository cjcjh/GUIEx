import math
from cs1graphics import *

def interpolate_colors(t, color1, color2):  # t값 = 0~1 =  color1(0)에서 color(1) 사이 위치
  """Interpolate between color1 (for t == 0.0) and color2 (for t == 1.0)."""
  r1, g1, b1 = color1     # t = 0.5 -> 두색 50:50으로 나눈 색
  r2, g2, b2 = color2     # t = 0 -> colo1색이 더 많이 t = 1 -> color2색이 더 많이
  return (int((1-t) * r1 + t * r2), # red값
          int((1-t) * g1 + t * g2), # green값
          int((1-t) * b1 + t * b2)) # blue값

def color_value(color):   # animate_sunrise 함수 컬러 지정
  """Convert a color name to an (r,g,b) tuple."""
  return Color(color).getColorValue()

def animate_sunrise(sun, morning_sun, noon_sun, morning_sky, noon_sky):
  morning_color = color_value(morning_sun)
  noon_color = color_value(noon_sun)
  dark_sky = color_value(morning_sky)
  bright_sky = color_value(noon_sky)
  w = canvas.getWidth()
  h = canvas.getHeight()
  r = sun.getRadius()
  x0 = w / 2.0
  y0 = h + r
  xradius = w / 2.0 - r
  yradius = h
  for angle in range(181):
    rad = (angle/180.0) * math.pi
    t = math.sin(rad)      # rad = angle = 90도 일때 t = 1 ,  180도 일때 t = 0
    col = interpolate_colors(t, morning_color, noon_color)
    sun.setFillColor(col)
    sun.setBorderColor(col)
    col = interpolate_colors(t, dark_sky, bright_sky)
    canvas.setBackgroundColor(col)
    x = x0 - xradius * math.cos(rad)
    y = y0 - yradius * math.sin(rad)
    sun.moveTo(x, y)

canvas = Canvas(600, 200)

sun = Circle(30)
canvas.add(sun)

animate_sunrise(sun, "dark orange", "yellow", "dark blue", "deepskyblue")

canvas.close()