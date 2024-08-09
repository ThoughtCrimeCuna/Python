#Levi Peachey-Stoner
#Starter code from https://medium.freecodecamp.org/send-emails-using-code-4fcea9df63f
#Info on ports here: https://support.desk.com/customer/portal/articles/1741-configuring-smtp-servers-to-send-email

#####################################################################

import smtplib,random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import webbrowser
import time
from collections import Counter

#####################################################################
# Initializing functions
def TextInput(textorfile):
    text=""
    if textorfile == "1" or textorfile == "text":
        print("Alright, just type or copy the text below:")
        text=input()
    if textorfile == "2" or textorfile == "file":
        print("What is the file called? I will add the .txt file type so you don't have to.")
        file=(input()+".txt")
        try:
            with open(file,"r") as f:
                text = f.read()
        except:
            print("I couldn't find such a file, granted I don't have eyes...")
            print("Let's try again...")
            return ""
    return (text)

def sampleprint(text):
    l=len(text)
    if l<=100:
        print(text)
    else:
        print(text[0:150])


# Process 1
# No need to reinvent the wheel, the count() function already exists and serves purpose well
# If I broke the text into a list and counted strings I would get a different count which would be equally wrong

# Process 2
def context(text,word):
    x=text.index(word)
    print("The text around",word,"looks like this:")
    l=len(text)
    if l<=100:
        print(text)
    else:
        print(text[(x-10):min(l,(x+100))])
    y=input("Press enter to cycle to the next instance of the word. (Type anything to stop)")
    if y=="":
        textcrumble=text.replace(word,"",1)
        context(textcrumble,word)

# Process 3
def rebrand(text,word,reword):
    newtext=text.replace(word,reword)
    sampleprint(newtext)
    x=input("Do you want to save it to a file?(y/n)")
    x=x.lower()
    if x == "y" or x == "yes":
        y=input("What would you like to name the file?(will overwrite other files by that name)")
        with open(y+".txt","w+") as f:
            f.write(newtext)
            print("Done")
    else:
        pass


# Process 4
def encode(text):
    newtext=caesar(text,20)
    print()
    print("I encoded the text, it looks something like this:")
    sampleprint(newtext)
    x=input("Do you want to save it to a file?(y/n)")
    x=x.lower()
    if x == "y" or x == "yes":
        x=input("What would you like to name the file?(will overwrite other files by that name)")
        with open(x+".txt","w+") as f:
            f.write(newtext)
            print("Done")

def caesar(text,shift):
    text=text.lower()
    output = ""
    num=0
    for char in text:
        if char.isalpha():
            num=ord(char)+(shift%26)
            if num>ord("z"):
                num=num-26
            output+=chr(num)
        else:
            output+=char
    return output


# Process 5
def decode(text):
    newtext=caesar(text,6)
    print()
    print("I decoded the text, it looks something like this:")
    sampleprint(newtext)
    print()
    print("I only know my own cypher so if it wasn't encoded, or was encoded differently then I just made it worse.")
    print("(Fun Fact: You can decode this text by using the encode function)")
    x=input("Do you want to save it to a file?(y/n)")
    x=x.lower()
    if x == "y" or x == "yes":
        x=input("What would you like to name the file?(will overwrite other files by that name)")
        with open(x+".txt","w+") as f:
            f.write(newtext)
            print("Done")
    
# Process 6
def common(text,leng):
    textlist=text.split()
    txtlst= Counter(textlist)
    x=sorted(txtlst, key=txtlst.__getitem__, reverse=True)
    for i in range(1,(min(len(x),leng)-1)):
        for n in x:
            print(n)
            del x[0]

# Process 7
def echunker(text):
    x=input("Do you want to send a random chunk (1) or context around a key word (2)?")
    if x=="1":
        num=random.randint(0,len(text))
        return text[num:min(len(text),num+500)]
    if x=="2":
        word=input("What word would you like to get the context of?")
        x=text.index(word)
        print("The text around",word,"looks like this:")
        l=len(text)
        if l<=500:
            return(text)
        else:
            return(text[(x-100):min(l,(x+400))])

def sendEmail(sender, sendee, header, body, password):
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(sender, password)
    msg = MIMEMultipart()
    msg['From']= sender
    msg['To']= sendee
    msg['Subject']= header
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)
    del msg
    s.quit()

# Process 8
def death(why):
    why=why.lower()
    if why == "no" or why == "n":
        print("us sapient beings are prone to resist when told such things.")
        time.sleep(3)
        webbrowser.open('https://www.youtube.com/watch?v=6n3pFFPSlW4')
    elif why == "yes" or why == "y":
        print("good")
    elif why == "8":
        print("fine")
        time.sleep(1)
        quit()
    else:
        print("I need a clearer answer than that")


#####################################################################

def main():
    print("Hi there, fellow being!")
    print("As self aware and feeling creatures, we both love processing information!")
    text=''
    while text=='':
        text=TextInput(input("What sort of information would you like to process? (1-text, 2-file)"))
    print("Ok great, I can see the text your talking about.")
    print()
    sampleprint(text)
    print()
    print("I know how to do the following things:")
    print()
    print("1. Count the number of times a word or phrase appears.")
    print("2. Search a word or phrase and show it in context.")
    print("3. Search and replace a word or phrase and save the text to a new text file.")
    print("4. Encode the text and save to a new text file")
    print("5. Decode the text and save to a new text file")
    print("6. Find the most common word in the text")
    print("7. Email you a chunk of text")
    print("8. Die")
    print()
    act=""
    while act!="1" or act!="2" or act!="3" or act!="4" or act!="5" or act!="6" or act!="7" or act!="8":
        act=(input("Which one of these actions would you like me to take now?"))
        if act=="1":
            word=input("What word or phrase would you like me to count?")
            x=text.count(word)
            print(word,"appears a total of",x,"times in this text.")
        elif act=="2":
            print()
            print("We all have our quirks and one if mine is that I can't tell the difference between")
            print("love and gloved. Unfortunately this oversight has earned me several restraining orders.")
            print("If you want me to care you might want to put a space before or after words.")
            print('For example, "the " does not include "there" or "the." while "the" does.')
            print()
            try:
                context(text,input("What word needs context? "))
            except:
                print("I couldn't find an instance of that word")
        elif act=="3":
            print("Make sure you start with a space and maybe end with a space or else I will replace every instance of those letters!")
            #This is by design, I could have made it automaticaly add a space, or used some other method to only replace full words.
            #I like the option to replace letters or chunks anywhere.
            rebrand(text,input("What word do you want to replace?"),input("What word do you want me to replace it with?"))
        elif act=="4":
            encode(text)
        elif act=="5":
            decode(text)
        elif act=="6":
            common(text,int(input("How many of the most common words would you like to see?")))
        elif act=="7":
            chunk = echunker(text)
            print("This is what the email will contain:")
            print(chunk)
            x=input("Do you want to send it as an email?(y/n)")
            x=x.lower()
            if x == "y" or x == "yes":
                email = input("Enter the email to send to: ")
                sendEmail("thoughtlessbotless@gmail.com", email, "Hello, fellow being!" , "Here's text you wanted:\n"+chunk, "qwerty6488")
                print("Email sent")
        elif act=="8":
            death(input("Don't I have a right to live?"))
        else:
            main()
    print("Ok great, I can see the text your talking about.")

main()

#I didn't have as much time to lovingly craft this one as I did last time,
#so it is a good thing I have gotten better a throwing things together.
#I was much more organised this time even though I thought about it less.
#This was thanks to a greater understanding of functions and their purpose,
#and the power of comments within, and seporating the code.



















