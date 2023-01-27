# logging is one of the most important python techniques
# to use logging, use the following two lines at the beginning
import logging
logging.basicConfig(
  level=logging.DEBUG,
  format=" %(asctime)s - %(levelname)s - %(message)s")
# when python logs an event, it creates LogRecord object
# basicConfig decides what details of LogRecord you want displayed
# eg: factorial logging
logging.debug("Start of factorial component") 
def factorial(n):
  logging.debug("Start of factorial function")
  total = 1
  for i in range(1,n+1):
    total*= i
    logging.debug(f"I is {i} , total is {total}")
  logging.debug("End of factorial")
  return total
print(factorial(5))
logging.debug("End of factorial component") 
# logging can be disabled by adding
# logging.disable(logging.CRITICAL) at the top of code
# don't have to involve unnecessary print statements
# or need to comment them out
# logging messages are for programmer

# Logging levels
"""
logging.debug()
logging.info()
logging.warning()
logging.error()
logging.critical()
"""
# the parameter to logging.basicConfig sets the
# lowest level, so if u set warning, u won't get info or debug
# can also log to filename
# logging.basicConfig(filename="myLog.txt", level=logging.DEBUG, format="%(message)s")