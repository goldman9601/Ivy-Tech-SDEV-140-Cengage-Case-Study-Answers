color1=str(input('Enter first primary color: '))
color2=str(input('Enter second primary color: '))

RED='red'
BLUE='blue'
YELLOW='yellow'


if color1 != BLUE and color1 != RED and color1 != YELLOW:
   print('Error')
elif color2 != BLUE and color2 != RED and color2 != YELLOW :
   print('Error')
elif color1 == BLUE and color2 == BLUE:
   print('Error')
elif color1 == YELLOW and color2 == YELLOW:
   print('Error')
elif color1 == RED and color2 == RED:
   print('Error')
elif (color1 == RED and color2 == BLUE) or (color1 == BLUE and color2 == RED):
   print('Purple')
elif (color1 == RED and color2 == YELLOW) or (color1 == YELLOW and color2 == RED):
   print('Orange')
else:
   print('Green')