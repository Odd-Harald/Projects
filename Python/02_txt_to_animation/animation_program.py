# The entire DEFAULT window is 40x20 spaces.
version_number='1.0'

if input('Enter "y" if you want information about the program. Otherwise enter "n".')=='y':
	print('')
	print('Hi, and welcome to this demonstration of version '+version_number+' of my animation program. The program works by loading .txt files, each representing a single frame of animation, into memory. Each frame of animation also specifies how long it will last. The frames are then played sequentially. For more information about the program, check out the code in a text editor')
	print('')


import time
animation_folder=''
frames=[]

#-------------FUNCTIONS---------------#

def file_to_linelist(txt_name):
	with open(txt_name) as tempfile:
		filestring=tempfile.read()
	return filestring.split('\n')     # The line_list

def printframe(line_list):
	time_period=float(line_list[-1])  # Time period in seconds
	temp_line_list=line_list[:-1]
	if running_windows==True:
		os.system('cls')
	for line in temp_line_list:
		print(line)
	time.sleep(time_period)

#---------------LOGIC-----------------#

running_windows=False

animation_folder=input('What is the path to the animation folder?')
if animation_folder[0]=='/':               # Running MacOS or Linux
	animation_folder=animation_folder+'/'
elif animation_folder[2]=='\\':            # Running Windows
	animation_folder=animation_folder+'\\'
	running_windows=True
	import os


frame_number=0
loaded_to_memory=False
while loaded_to_memory==False:
	try:
		frames.append(file_to_linelist(animation_folder+str(frame_number)+'.txt'))
		frame_number+=1
	except:
		print('Done loading frames.')
		break

while True:
	print('Enter \'y\' to play/replay animation. Enter \'n\' to terminate program.')
	playanimation=input()
	if playanimation=='n':
		break
	elif playanimation=='y':
		current_frame=0
		while current_frame<len(frames):
			printframe(frames[current_frame])
			current_frame+=1
			
print('The program has terminated.')