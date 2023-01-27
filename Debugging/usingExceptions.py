#! usr/bin/python3
# demo file for using the exception handling mechanism
def boxPrint(symbol:str, width:int,height:int):
  if len(symbol) != 1:
    raise Exception("Must be single character symbol")
  if width <= 2:
    raise Exception("Width must be greater than 2")
  if height <= 2:
    raise Exception("Height must be greater than 2")
  print(symbol*width)
  for i in range(height-2):
    print(symbol+" "*(width-2)+symbol )
  print(symbol*width)

for sym,w,h in (('a',4,5),('--',10,20),('|',1,30),('|',20,10)):
  try:
    boxPrint(sym,w,h)
  except Exception as err:
    #exception object err generated
    print("An exception occured: "+str(err)) 
    