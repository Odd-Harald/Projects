#_________________________________________________PRELIMINARIES__________________________________________________#

version_number='1.0'

import requests
import bs4
import csv
import owde
import os
import time
from datetime import datetime

# state ---->  [to be scraped, output folder, exit?]

def printlist(mylist): #For debugging
    for a in mylist:
        print(a)

#___________________________________________________FUNCTIONS____________________________________________________#

def help_statement():
    print('')
    print(f'Welcome to the [O]dd Harald Sandtveit [Wi]kipedia [C]ategories to [C]SV tool version {version_number}.')
    print('OWiCC allows the user to make available a much larger part of a wikipedia '
          'category-tree than would be possible on a single web page in a browser.')
    print('')
    print('Commands:')
    print('')
    print('<h>                    Show this help statement.')
    print('<e>                    Exit the program.')
    print('<s>                    Set output folder. Default is current working directory.')
    print('Any number             Decide how far down the scraper will reach.')
    print('')
    print('Entering a URL         Convert wikipedia category-tree at this URL to csv-file at specified output folder.')
    print('')
          
def interpreter(state):
    user_input=input()
    
    if user_input== 'h':
        help_statement()

    elif user_input== 'e':
        state[2]=1
        
    elif len(user_input)>0 and user_input.isdigit():
        state[3]=int(user_input)
    
    
    elif user_input== 's':
        
        try:
            state[1]=owde.owde(os.getcwd()+'\\')[0][0]
            print('Folder set to output.')
        
        except:
            print('OWDE could not be located. Please input new output folder manually:')
            while True:
                new_output_folder=input()
                if os.path.isdir(new_output_folder):
                    break
                print('Folder could not be located. Please try again.')
            print('Folder set to output.')
            state[1]=new_output_folder
            
    elif 'wikipedia.org' in user_input:
        state[0]=user_input
        
    return state
    
    
def url_to_list(state):
    initial_page=state[0].split('/')[-1][9:]
    
    levels=state[3]                      #We will construct a returned as strings
    pages_to_scrape=[initial_page]     # list stored as strings as top_category/sub_category/sub_sub_category...
    cat_scraped=[]
    elem_scraped=[]
    
    scraping=True
    while scraping==True:
        if len(pages_to_scrape)==0:
            break
        if len(pages_to_scrape[0].split('/'))>levels:
            #print('Check AAAAA') #------------------------------DEBUG
            pages_to_scrape.pop(0)
            continue
        
        print('will scrape '+'https://en.wikipedia.org/wiki/Category:'+pages_to_scrape[0].split('/')[-1])    #DEBUG____
        time.sleep(1)
        RO=requests.get('https://en.wikipedia.org/wiki/Category:'+pages_to_scrape[0].split('/')[-1])
        SO=bs4.BeautifulSoup(RO.text,'lxml')
        a=SO.select('div.mw-category a')
    
        for b in a:
            if 'a href="/wiki/Category:' in b.__str__():
                cat_scraped.append(pages_to_scrape[0]+'/'+b.__str__().split()[1][21:-1])
                pages_to_scrape.append(pages_to_scrape[0]+'/'+b.__str__().split()[1][21:-1])
            else:
                elem_scraped.append(pages_to_scrape[0]+'/'+b.__str__().split()[1][12:-1])
                
        pages_to_scrape.pop(0)
    
    print('Done scraping!')
    return [cat_scraped,elem_scraped]


def list_to_csv(content,state):
    #printlist(cat_scraped) #DEGUB
    #print('')              #DEGUB
    #printlist(elem_scraped)#DEGUB
    
    csv_FO=open(state[1]+'\\'+'OWiCC - '+'_'.join('_'.join(datetime.now().__str__().split('.')).split(':'))+'.csv', 'w', encoding='utf-8', newline='')
    WO=csv.writer(csv_FO, delimiter=',')
    
    for str_info in content[0]:    #categories
        list_to_write=['Category',len(str_info.split('/'))]
        list_to_write.extend(str_info.split('/'))
        WO.writerow(list_to_write)
        
    for str_info in content[1]:    #elements
        list_to_write=['Element',len(str_info.split('/'))]
        list_to_write.extend(str_info.split('/'))
        WO.writerow(list_to_write)
    
    csv_FO.close()
    # create writer object
    # write to file
    # close file.
    # end function
    

#_____________________________________________________LOGIC______________________________________________________#

def owicc():
    print(f'OWiCC v.{version_number}                    Enter <h> for help.')
    state=['',os.getcwd(),0,2]                  #[to be scraped, output folder, exit?, levels]
    owicc_on=True
    
    while owicc_on==True:
        state=interpreter(state)
        if state[2]==1:
            break
        if state[0]!='':
            list_to_csv(url_to_list(state),state)
        state[0]=''

#___________________________________________________EXECUTION____________________________________________________#

debug=False #    <--------------------------------------|

if __name__=='__main__' and debug==False:
    owicc()
    print('_______________________OWiCC has terminated_______________________')
elif debug==False:
    print('OWiCC v.{} has been loaded'.format(version_number))
    
#_____________________________________________________DEBUG______________________________________________________#
