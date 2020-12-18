import selenium
from selenium import webdriver
import time
import datetime
from datetime import date
from selenium.webdriver.chrome.options import Options
opt = Options()
opt.add_experimental_option("prefs", { "profile.default_content_setting_values.media_stream_mic":2, 
    "profile.default_content_setting_values.media_stream_camera":2})
    
emailid="Your Teams Email ID"
password="Your Teams Password"
filepath= r" FILE PATH OF CHROME DRIVER"
day1=["CHANNEL NAME","CHANNEL NAME"] #monday routine
day2=["CHANNEL NAME","CHANNEL NAME"] #tuesday routine
day3=["CHANNEL NAME","CHANNEL NAME"] #wednesday routine
day4=["CHANNEL NAME","CHANNEL NAME"] #thrusday routine
day5=["CHANNEL NAME","CHANNEL NAME"] #friday routine
day6=["CHANNEL NAME","CHANNEL NAME"] #saturday routine
startclass=["00:00","00:00","00:00","00:00",] #starting time of classes in 24-hours format
endclass=["00:00","00:00","00:00","00:00",] #ending time of classes in 24-hours format
noc=4

op=filepath[:2].lower() + "//" + filepath[3:].replace('\\','/')+"/chromedriver"
driver = webdriver.Chrome(options=opt,executable_path=op) 
print("WELCOME TO PRASOON BOT")
driver.get("http://teams.microsoft.com")
time.sleep(2)
email=driver.find_element_by_id("i0116")
email.send_keys(emailid)
print("PRASOON BOT: eMAIL ID entered")
time.sleep(2)
enter=driver.find_element_by_id("idSIButton9")
time.sleep(2)
enter.click()
time.sleep(2)
passwd=driver.find_element_by_id("i0118")
passwd.send_keys(password)
print("PRASOON BOT: PASSWORD entered")
passbtn=driver.find_element_by_id("idSIButton9")
passbtn.click()
time.sleep(2)
confirmbtn=driver.find_element_by_id("idSIButton9")
confirmbtn.click()
print("PRASOON BOT: Logged In to your Account. Loading TEAMS web app...")
time.sleep(2)
usebtn=driver.find_element_by_link_text("Use the web app instead")
usebtn.click()
print("PRASOON BOT: TEAMS web app loaded")
time.sleep(5)
try:
    teambtn=driver.find_elements_by_css_selector('div.team-card')
    teambtn[0].click()
except:
    j=0
    while j<=1:
        teambtn=driver.find_elements_by_css_selector('div.team-card')
        if teambtn==None:
            time.sleep(2)
            continue
        elif teambtn !=None:
            teambtn[0].click()
            print("PRASOON BOT successfully entered inside your team.")
            break
time.sleep(3)
def classjoin(x,i,y):
    print("PRASOON BOT: Searching the subject channel")
    z=x[i]
    channelbtn=driver.find_element_by_xpath("//a[@title=\'"+z+"\']")
    channelbtn.click()
    print("Channel Found")
    time.sleep(10)
    print("PRASOON BOT: Looking for the join button")
    c=0
    while c<=1:
        print("PRASOON BOT is trying to join the meeting")
        time.sleep(2)
        joinbtn=driver.find_element_by_css_selector('button.ts-calling-join-button')
        if joinbtn==None:
            time.sleep(2)
            continue
        elif joinbtn != None:
            joinbtn.click()
            break
            
    print("PRASOON BOT is joining the meeting")
    d=0
    while d<=1:
        print("PRASOON BOT is trying its best to join the meeting")
        time.sleep(2)
        conbtn=driver.find_element_by_css_selector('button.ts-btn-fluent-secondary-alternate')
        if conbtn==None:
            time.sleep(2)
            continue
        elif conbtn != None:
            conbtn.click()
            time.sleep(2)
            break    
    joinbtn2=driver.find_element_by_css_selector('button.join-btn')
    joinbtn2.click()
    time.sleep(5)
    print("PRASOON BOT has joined the meeting")
    time.sleep(5)
    try:
        time.sleep(2)
        driver.find_element_by_id('callingButtons-showMoreBtn').click()
    except:
        u=0
        while u<=1:
            print("PRASOON BOT: trying to press show more btn")
            showbtn=driver.find_element_by_id('callingButtons-showMoreBtn')
            if showbtn !=None:
                driver.find_element_by_id('callingButtons-showMoreBtn').click()
                break 
            elif showbtn == None:
                driver.find_element_by_css_selector('div.ts-calling-screen').click()
                continue
    try:
        driver.find_element_by_id('incoming-video-button').click()
        print("PRASOON BOT: turned video off")
    except:
        o=0
        while o<=1:
            print('PRASOON BOT: trying its best to turn off the video')
            inbtn=driver.find_element_by_id('incoming-video-button')
            if inbtn !=None:
                driver.find_element_by_id('incoming-video-button').click()
                break
            elif inbtn==None:
                time.sleep(10)
                driver.find_element_by_css_selector('div.ts-calling-screen').click()
                driver.find_element_by_id('callingButtons-showMoreBtn').click()
                continue
                
    print("PRASOON BOT has turned incoming video off")
    endtime=y[i]
    m=0
    while m<=1:
        if time.strftime('%H:%M')==endtime:
              print("PRASOON BOT is leaving the meeting")
              try:
                  driver.find_element_by_css_selector('div.ts-calling-screen').click()
                  driver.find_element_by_id('hangup-button').click()
                  print("PRASOON BOT is left the meeting")
              except:
                  y=0
                  while y<=1:
                      print("PRASOON BOT is trying to leave the meeting")
                      exitbtn=driver.find_element_by_id('hangup-button')
                      if exitbtn==None:
                          driver.find_element_by_css_selector('div.ts-calling-screen').click()
                          continue
                      elif exitbtn !=None:
                          driver.find_element_by_id('hangup-button').click()
                          driver.find_element_by_id('hangup-button').click()
                          break
                                  
              print("PRASOON BOT left the class")
              break
        else:
            continue
              
               
     
if date.today().weekday()==0:
     print("PRASOON BOT is checking MONDAY Timetable")
     i=0
     while i<=1:
          print("Looking for class...")
          for x in range(0,noc):
              if time.strftime('%H:%M')==startclass[x]:
                  print("PRASOON BOT : Its time for the class")
                  classjoin(day1,x,endclass)
                  continue

if date.today().weekday()==1:
     print("PRASOON BOT is checking TUESDAY Timetable")
     i=0
     while i<=1:
          print("Looking for class...")
          for x in range(0,noc):
              if time.strftime('%H:%M')==startclass[x]:
                  print("PRASOON BOT : Its time for the class")
                  classjoin(day2,x,endclass)
                  continue

if date.today().weekday()==2:
     print("PRASOON BOT is checking WEDNESDAY Timetable")
     i=0
     while i<=1:
          print("Looking for class...")
          for x in range(0,noc):
              if time.strftime('%H:%M')==startclass[x]:
                  print("PRASOON BOT : Its time for the class")
                  classjoin(day3,x,endclass)
                  continue


if date.today().weekday()==3:
     print("PRASOON BOT is checking THRUSDAY Timetable")
     i=0
     while i<=1:
          print("Looking for class...")
          for x in range(0,noc):
              if time.strftime('%H:%M')==startclass[x]:
                  print("PRASOON BOT : Its time for the class")
                  classjoin(day4,x,endclass)
                  continue
     

if date.today().weekday()==4:
     print("PRASOON BOT is checking FRIDAY Timetable")
     i=0
     while i<=1:
          print("Looking for class...")
          for x in range(0,noc):
              if time.strftime('%H:%M')==startclass[x]:
                  print("PRASOON BOT : Its time for the class")
                  classjoin(day5,x,endclass)
                  continue
          


if date.today().weekday()==5:
     print("PRASOON BOT is checking SATURDAY Timetable")
     i=0
     while i<=1:
          print("Looking for class...")
          for x in range(0,noc):
              if time.strftime('%H:%M')==startclass[x]:
                  print("PRASOON BOT : Its time for the class")
                  classjoin(day6,x,endclass)
                  continue





     
    
    
























