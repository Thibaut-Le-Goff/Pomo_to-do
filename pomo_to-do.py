"""
__        __         _      ___
\ \      / /__  _ __| | __ |_ _|_ __
 \ \ /\ / / _ \| '__| |/ /  | || '_ \
  \ V  V / (_) | |  |   <   | || | | |
   \_/\_/ \___/|_|  |_|\_\ |___|_| |_|
 ____
|  _ \ _ __ ___   __ _ _ __ ___  ___ ___
| |_) | '__/ _ \ / _` | '__/ _ \/ __/ __|
|  __/| | | (_) | (_| | | |  __/\__ \__ \
|_|   |_|  \___/ \__, |_|  \___||___/___/
                 |___/
/!\ Caution /!\

This is an unfinished project created by a beginner, I am open to any kind of advice to improve my code, thanks.

Goal of the code:
Create a to-do list platform with the time management of the pomodoro technique.
"""

import os
duraw = 0.5 # seconds
freqw = 440  # Hz
durar = 0.5 # seconds
freqr = 311.127 # Hz
conti = 'y'
todo = []
done = []

while conti == 'y':
	task = input("What would you like to do? : ")
	minw = int(input("How many minutes do you want to spend on it? : "))
	conti = input("Would you like to do something else after? (y/n) : ")
	if conti == 'y':
		minr = int(input("How many minutes do you want to rest untill the next task? : "))
	else:
		minr = 0
	todo.append([task, minw, minr])

# I would like to use "for i in range(len(todo)):" but it print an error "list index out of range" and I can't explain why...
while todo != []:
	work = todo[0][1]
	while work != 0:
		os.system('play -nq -t alsa synth {} sine {} && clear && figlet {} && figlet Time left : {} min && sleep 60'.format(duraw, freqw, todo[0][0], work))
		work = work -1
		if work == 0:
			for i in range(3):
				os.system('play -nq -t alsa synth {} sine {}'.format(durar, freqr))
	rest = todo[0][2]
	while rest != 0:
		os.system('clear && figlet Time to rest ! Time left : {} min && sleep 60'.format(rest))
		rest = rest -1
		if rest == 0:
			for i in range(3):
				os.system('play -nq -t alsa synth {} sine {}'.format(duraw, freqw))
	done.append(todo[0])
	todo.pop(0)

"""
https://pypi.org/project/pyfiglet/0.7/
https://medium.com/py-bits/sound-generation-python-904e54f5398d
"""
