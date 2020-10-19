"""
This is a program for chatbot
1. This bot helps u to know the news all over the country.
2. Bot starts with greeting & ask the user's name
3. Bot offers choice of things to do. User can select any of those.
4. Bot will help u by giving information and respond to the users input instantly.
"""
import random
from datetime import datetime

def greet_and_intro():
       msgs=[
           " \n Hey.. there ! welcome to our bot. It's me news chatbot :) may i know your name  ? \n "
       ]
       print(random.choice(msgs))

def get_timeofday_greeting():
    current_time = datetime.now()
    timeofday_greeting = "Good Morning"
    if current_time.hour > 12 and current_time.hour < 17:
        timeofday_greeting = "Good Afternoon"
    elif current_time.hour >=17 and current_time.hour < 22:
        timeofday_greeting = "Good Evening"
    elif current_time.hour >=22:
        timeofday_greeting = "Hi! it's high time"
    return timeofday_greeting

def welcome(name):
    messages = [
        "Nice to u meet u  :)  ",
        "lets start"
    ] 

    print (get_timeofday_greeting(), random.choice(messages))

def show_menu():
    print(" \n *HERE IS THE MAIN MENU *** \n  ")
    print("1.Get the news ")
    print("2.Current time ")
    print("3.End this chat ")
    print("..................")
    try:
        return int(input("Enter your choice [1-3]: "))
    except:
        print("Only enter choice from 1, 2, 3")
        return 0
def news_menu():
    print(" \n ** HERE IS YOUR NEWS MENU **\n ")
    print("1.Economy ")
    print("2.Reports ")
    print("3.Environment ")
    print("4.National ")
    print("5.Science & Technology ")
    print("6.flimyfocus ")
    print("7.Sports ")
    print("8.International ")
    print("9.End the search")

    try:
      return int(input("Enter your choice[1-9]"))
    except:
      print("Input Error:Only enter choice from 1-9.")
      return 0

def show_news() :
    news=news_menu()
    while(news!=9):
        if news==1:
            print("Welcome to todays Economy news \n ")
            print("---- \n ")
            Economy=[
                     
                   "Center borrowing for states sets to flatten yeild curve \n ",
                   "Forex reserves jump USD 75 billion since lockdown   \n "
                   
                   
            ]
            
            print(random.choice(Economy))
            print("---- \n ")
        elif news==2:
            print("Welcome to todays Reports news \n ")
            print("---- \n ")
            Reports=[
                     
                   "Monetary Fund’s (IMF’s) latest projection of \n Bangladesh’s real per capita gross domestic product",
                    "(GDP) surpassing India’s real per capita GDP\n",
                    "India fares poorly in hunger index   "
            ]
            
            print(random.choice(Reports))
            print("---- \n ")
        elif news==3:
            print("Welcome to todays Environment news \n ")
            print("---- \n ")
            Environment=[
                    "Global Warming might effect food security :National Geographic Magazine\n",
                    "6% drop in SO2 emission, but India still top polluter Oct 9, 2020.\n",
                    "India world's largest emitter of sulphur dioxide, emissions see drop in 2019: Report Oct 8, 2020.\n",
                    "COVID-19 trashed the recycling dream while oil and gas industry hope for more plastic Oct 7, 2020.\n" 
            ]
            
            print(random.choice(Environment))
            print("---- \n ")
        elif news==4:
            print("Welcome to todays National news \n ")
            print("---- \n ")
            National=[
                     
                   "A ‘Zero Rajdhani’ skirts Guwahati, cuts travel short\n",
                   "76% of rural Indians can’t afford nutrious diet"
                   
            ]
            
            print(random.choice(National))
            print("---- \n ")
        elif news==5:
            print("Welcome to todays Science & Technology news \n ")
            print("---- \n ")
            Science=[
                     
                   " Early childhood stress and mental illness :TIFR, Mumbai\n",
                   " New research sheds light on declining star formation  in Milky way\n"
                   
            ]
            
            print(random.choice(Science))
            print("---- \n ")
        elif news==6:
            print("Welcome to todays Flims news \n ")
            print("---- \n ")
            Flims=[
                     
                   "Akshay releases biggest dance track of the year Burj Khalifa\n",
                   "Shahid Kapoor announces Jersey schedule wrap\n",
                   "Varalaxmi Sarathkumar turns director with Kannamoochi\n"
            ]
            
            print(random.choice(Flims))
            print("---- \n ")
        elif news==7:
            print("Welcome to todays Sports news \n ")
            print("---- \n ")
            Economy=[
                     
                    "deVilliers’ genius drags RCB across the line\n",
                    "Man City shades Arsenal via Sterling’s strike\n"
            ]
            
            print(random.choice(Economy))
            print("---- \n ")
        elif news==8:
            print("Welcome to todays International news \n ")
            print("---- \n ")
            International=[
                   "Thailand declares emergency after umprecedent protest in bangkol\n",
                   "UK,EU set to discuss 'structure' of Brexit talks\n",
                   "Jacinda Ardern wins landslide re-election in New-Zealand vote"
            ]
            
            print(random.choice(International))
            print("---- \n ")
        else:
            print(" \n Sorry i don't understand please give input from (1-9) \n ")
        news=news_menu() 
def quotes():
    qut=[
        " \n DON'T LET YESTERDAY TAKE UP TOO MUCH OF TODAY. \n ",
        " \n SUCCESS COMES FROM ASPIRATION,DESPIRATION,PERSPIRATION AND INSPIRATION! \n ",
        " \n PERFECTION IS NOT ATTAINABLE,BUT IF WE CHASE PERFECTION WE CAN CATCH EXCELLENCE \n  "
    ]
    print (random.choice(qut))

def news():
    greet_and_intro()
    name = input("Enter ur name: ")
    welcome(name)
    choice = show_menu()
    while choice != 3:
        if choice == 1:
            show_news()
        elif choice == 2:
            print(str(datetime.now()))
        else:
            print("I dont understand that")
        choice = show_menu()
    print(" \n THANK TOU FOR VISITING OUR CHAT BOT! \n SEE YOU AGAIN \n ")
    quotes()
news()
