#! usr/bin/python3

# Assert are like programmer's guideropes to what went wrong
# There are a few things which should always be true for a program
# to work. Assertion is basically a guarantee that something is exactly as you 
# believe, otherwise the program stops
isDoorOpen = 'close'
assert isDoorOpen == "open", "The doors need to be open"
# as above is false, throws an assertion error
# assertions disabled by hitting -0 while running