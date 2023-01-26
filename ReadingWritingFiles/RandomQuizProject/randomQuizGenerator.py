#! usr/bin/python
"""
A program to create random quizzes with random answer keys
with the questions jumbled to make cheating difficult
"""

import random, os, sys


capitals =  {
  'Alabama': 'Montgomery',
 'Alaska': 'Juneau',
 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock',
 'California': 'Sacramento',
 'Colorado': 'Denver',
'Connecticut': 'Hartford',
 'Delaware': 'Dover',
 'Florida': 'Tallahassee',
'Georgia': 'Atlanta',
 'Hawaii': 'Honolulu',
 'Idaho': 'Boise',
 'Illinois':'Springfield',
 'Indiana': 'Indianapolis',
 'Iowa': 'Des Moines',
 'Kansas':'Topeka',
 'Kentucky': 'Frankfort',
 'Louisiana': 'Baton Rouge',
 'Maine':'Augusta',
 'Maryland': 'Annapolis',
 'Massachusetts': 'Boston',
 'Michigan':'Lansing',
 'Minnesota': 'Saint Paul',
 'Mississippi': 'Jackson',
 'Missouri':'Jefferson City',
 'Montana': 'Helena',
 'Nebraska': 'Lincoln',
 'Nevada':'Carson City',
 'New Hampshire': 'Concord',
 'New Jersey': 'Trenton',
 'New Mexico': 'Santa Fe',
 'New York': 'Albany',
 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck',
 'Ohio': 'Columbus',
 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem',
 'Pennsylvania': 'Harrisburg',
 'Rhode Island': 'Providence',
'South Carolina': 'Columbia',
 'South Dakota': 'Pierre',
 'Tennessee':'Nashville',
 'Texas': 'Austin',
 'Utah': 'Salt Lake City',
 'Vermont':'Montpelier',
 'Virginia': 'Richmond',
 'Washington': 'Olympia',
 'West Virginia': 'Charleston',
 'Wisconsin': 'Madison',
 'Wyoming': 'Cheyenne'
 }

# create n number of quizzes
n : int = int(input("Enter number of quizfiles to generate: "))


print(os.getcwd())
basePath = os.path.join(
  os.getcwd(),
  "ReadingWritingFiles/RandomQuizProject/QuizFiles")
if not os.path.exists(basePath):
  os.mkdir(basePath)
for qNo in range(n):
  # create quiz and answer key file
  filePath = os.path.join(basePath,("Quiz%s" % (qNo+1)))
  if not os.path.exists(filePath):
    os.mkdir(filePath)
  quizFile = open(os.path.join(filePath,('quiz%s' % (qNo+1))), 'w')
  answerKey = open(os.path.join(filePath,('ansKey%s' % (qNo+1))), 'w')

  # write out the quiz header
  quizFile.write("Name:\nRoll Number:\nData:\n\n")
  quizFile.write(" "*20 + 'State Capitals Quiz , Number %s' % (qNo+1))
  quizFile.write("\n\n")
  # shuffle through order of states
  states = list(capitals.keys())
  random.shuffle(states)

  # loop through all 50 states, make question for each 
  for questionNo in range(50):
    correctAnswer = capitals[states[questionNo]]
    wrongAnswers = list(capitals.values())
    wrongAnswers.remove(correctAnswer)
    # del wrongAnswers[wrongAnswers.index(correctAnswer)]
    wrongAnswers = random.sample(wrongAnswers,3)
    answerValues = wrongAnswers + [correctAnswer]
    random.shuffle(answerValues)
    quizFile.write("%s. What is the capital of %s?\n" % (questionNo+1, states[questionNo]))
    for i in range(4):
      quizFile.write("   %s. %s\n" % (i+1, answerValues[i]))
    quizFile.write("\n")

    answerKey.write("%s : %s\n"%(questionNo+1,"ABCD"[answerValues.index(correctAnswer)]))
  quizFile.close()
  answerKey.close()    
# sys.exit()