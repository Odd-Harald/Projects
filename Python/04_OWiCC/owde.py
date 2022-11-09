# [O]dd Harald Sandtveit [W]indows [D]irectory [E]xplorer
version_number=1.0    #-----------------------------------------------------------<<<--<-<-<-<-

#format i_state: 
# 0 - current_DIR,                   ONLY one to have \\ at the end
# 1 - Dirs          stored as names
# 2 - Files         stored as names
# 3 - Other         stored as names

# 4 - s_Dirs        stored as full paths
# 5 - s_Files       stored as full paths
# 6 - s_Other       stored as full paths

# 7 - options(0=continue, 1=quit, 2=quit and return)

#__________________________________________________________________________________________________________________#
#                                                       FUNCTIONS                                                  #
#__________________________________________________________________________________________________________________#

import os

def help_statement(version_number):
    print(f'Welcome to the [O]dd Harald Sandtveit [W]indows [D]irectory [E]xplorer (OWDE) version {version_number}.')
    print('')
    print('The directory explorer allows the user to navigate the directory-tree, ')
    print('as well as returning files when called from a separate program.')
    print('OWDE is intended to be used on Windows inside the CMD.')
    print('')
    print('Here are the built-in functions one should know about:')
    print('')
    print("'help' or 'h'           Show this message.")
    print("'exit' or 'e'           Exit the explorer without returning anything to an external program.")
    print("'return' or 'r'         Return Directories, Files and Others to external program")
    print("Inputting a path        Return exactly this Directory/File/Other immediately.")
    print('')
    print("Inputting a number      Enter this directory")
    print("'u' or 'up'             Navigate up one directory")
    print('')
    print("'qN'                    Select/deselect Directory number N")
    print("'aN'                    Select/deselect File number N")
    print("'zN'                    Select/deselect Other number N")
    print('')
    print("'cdN' or 'changedriveN' Enter drive N; N is a capital letter.")
    print('')
    print('Press <Enter> to exit help statement.')


def dir_info(path):
    a=[path,[],[],[]]
    b=os.scandir(path)
    for c in b:
        if c.is_dir()==True:
            a[1].append(c.name)
        elif c.is_file()==True:
            a[2].append(c.name)
        else:
            a[3].append(c.name)
    a[1]=sorted(a[1])
    a[2]=sorted(a[2])
    a[3]=sorted(a[3])
    return a

def dir_printer(info,version_number,c_selected): # The printer works well to 999, but will print weirdly after that.
    print(f'OWDE v{version_number}   -   type "h" for help')
    print()
    print(info[0])
    print()
    print('DIRECTORIES')
    for a,b in enumerate(info[1]):
        x1=' '
        for y2 in c_selected[0]:
            if y2==info[0]+b:
                x1='-'
        
        if len(str(a+1))==1:
            print(x1*5+str(a+1)+' '+b)
        elif len(str(a+1))==2:
            print(x1*4+str(a+1)+' '+b)
        else:
            print(x1*3+str(a+1)+' '+b)
    print('FILES')
    for c,d in enumerate(info[2]):
        x1=' '
        for y2 in c_selected[1]:
            if y2==info[0]+d:
                x1='-'
        
        if len(str(c+1))==1:
            print(x1*5+str(c+1)+' '+d)
        elif len(str(c+1))==2:
            print(x1*4+str(c+1)+' '+d)
        else:
            print(x1*3+str(c+1)+' '+d)
    print('OTHER')
    for e,f in enumerate(info[3]):
        x1=' '
        for y2 in c_selected[2]:
            if y2==info[0]+f:
                x1='-'
        if len(str(e+1))==1:
            print(x1*5+str(e+1)+' '+f)
        elif len(str(e+1))==2:
            print(x1*4+str(e+1)+' '+f)
        else:
            print(x1*3+str(e+1)+' '+f)

def interpreter(c_state,c_selected,version_number):
    return_value = [c_state[0],c_state[1],c_state[2],c_state[3],c_selected[0],c_selected[1],c_selected[2],0] #i_state
    user_input=input()
                                                    #GENERAL
    if user_input=='':
        print('Error: Command not understood.')
        print('Press <Enter> to continue.')
        input()
        packed_return_value=[[return_value[0],return_value[1],return_value[2],return_value[3]],[return_value[4],return_value[5],return_value[6]],return_value[7]]
        return packed_return_value
    
    elif user_input=='h' or user_input=='help':
        os.system('cls')
        help_statement(version_number)
        input()
    
    elif user_input=='e' or user_input=='exit':
        return_value[7]=1
    
    elif user_input=='r' or user_input=='return':
        return_value[7]=2
                                                    #NAVIGATION
    elif user_input.isdigit():
        if len(return_value[1]) >= int(user_input):
            return_value[0]=return_value[0]+return_value[1][int(user_input)-1]+'\\'
        else:
            print('Error, directory not found.')
            print('Press <Enter> to continue.')
            input()
    
    elif user_input=='u' or user_input=='up':
        return_value[0]=one_dir_up(return_value[0])
    
    elif user_input[0:-1:]=='cd' or user_input[0:-1:]=='changedrive':
        if os.path.isdir(user_input[-1]+':\\') and os.path.islink(user_input[-1]+':\\')==False:
            return_value[0]=user_input[-1]+':\\'
        else:
            print('Error, drive not found.')
            print('Press <Enter> to continue.')
            input()
        
        
                                                    #SELECTION FOLDERS
    elif user_input[0]=='q' and user_input[1::].isdigit():
        folder_num=int(user_input[1::])
        if len(return_value[1]) >= folder_num:
            full_path_dir=return_value[0]+return_value[1][folder_num-1]
            if full_path_dir in return_value[4]:
                return_value[4].remove(full_path_dir)
            else:
                return_value[4].append(full_path_dir)
                
        else:
            print('Error, directory not found.')
            print('Press <Enter> to continue.')
            input()
            
                                                    #SELECTION FILES
    elif user_input[0]=='a' and user_input[1::].isdigit():
        file_num=int(user_input[1::])
        if len(return_value[2]) >= file_num:
            full_path_file=return_value[0]+return_value[2][file_num-1]
            if full_path_file in return_value[5]:
                return_value[5].remove(full_path_file)
            else:
                return_value[5].append(full_path_file)
                
        else:
            print('Error, file not found.')
            print('Press <Enter> to continue.')
            input()

                                                    #SELECTION OTHER
    elif user_input[0]=='a' and user_input[1::].isdigit():
        other_num=int(user_input[1::])
        if len(return_value[3]) >= other_num:
            full_path_other=return_value[0]+return_value[3][other_num-1]
            if full_path_other in return_value[6]:
                return_value[6].remove(full_path_file)
            else:
                return_value[6].append(full_path_file)
                
        else:
            print('Error, other not found.')
            print('Press <Enter> to continue.')
            input()
                                                    #DIRECTLY RETURN DIR/FIL/SL
    elif len(user_input)>=3:
        if user_input[2]=='\\':
            if os.path.isdir(user_input)==True and os.path.islink(user_input)==False:
                return_value = [c_state[0],c_state[1],c_state[2],c_state[3],[user_input],[],[],2]
            elif os.path.isdir(user_input)==True and os.path.islink(user_input)==True:
                return_value = [c_state[0],c_state[1],c_state[2],c_state[3],[],[],[user_input],2]
            elif os.path.isfile(user_input)==True:
                return_value = [c_state[0],c_state[1],c_state[2],c_state[3],[],[user_input],[],2]
            else:
                print('Error: Directory/File/Other could not be found.')
                print('Press <Enter> to continue.')
                input()
    
    else:
        print('Error: Command not understood.')
        print('Press <Enter> to continue.')
        input()
    
    packed_return_value=[[return_value[0],return_value[1],return_value[2],return_value[3]],[return_value[4],return_value[5],return_value[6]],return_value[7]]
    return packed_return_value

def one_dir_up(mypath):
    if len(mypath)>3:
        a=mypath.split('\\')
        a.pop()
        a.pop()
        return '\\'.join(a)+'\\'
    else:
        print('ERROR:')
        print('You are already in the root directory!')
        print('Press <Enter> to continue.')
        input()
        return mypath

#__________________________________________________________________________________________________________________#
#                                                         LOGIC                                                    #
#__________________________________________________________________________________________________________________#

def owde(startpath='NONE'):
    c_state=[os.getcwd(),[],[],[]]     #c_state is current state.
    if os.path.isdir(startpath)==True and os.path.islink(startpath)==False:
        c_state=[startpath,[],[],[]]
    c_selected=[[],[],[]]              #Selected folders, files and other.
    #c_state=['C:\\Home\\',[],[],[]]          #DEBUGGING-----------------------------
    owde_on=True
    
    
    while owde_on==True:
        try:
            c_state=dir_info(c_state[0])
        except:
            c_state=dir_info('C:\\')
            print('Error: Directory inaccessible.')
            print('Returning to C:\\.')
            print('Press <Enter> to continue.')
            input()
        os.system('cls')
        dir_printer(c_state,version_number,c_selected)
        
        i_state = interpreter(c_state,c_selected,version_number)
        c_state = i_state[0]
        c_selected =i_state[1]
        if i_state[2] == 1:
            owde_on=False
        if i_state[2] == 2:
            return c_selected
        
        #DEBUG:
        #print(i_state)
        #input()

    print('')
    print('________OWDE has been terminated________')
        
        
#__________________________________________________________________________________________________________________#
#                                                       EXECUTION                                                  #
#__________________________________________________________________________________________________________________#
if __name__=='__main__':
    owde()
else:
    print(f'OWDE v {version_number} has been loaded.')