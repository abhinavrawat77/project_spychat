#importing packages used in our program
from spy_details1 import spy, spies, Messages, friends
from steganography.steganography import Steganography
from termcolor import colored,cprint
#it is a list containing the old status of existing spy
status = ['BUSY', 'Available', 'at gym']

#it will bethe first message displayed when the programe is run
print "welcome to the spy chat"
#here system will ask user that is he the existing user or a new one
question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = raw_input(question)

# this is a function for updating a new status or choosing an older one
def add_status():
    updated_status= None
    #if there is no status it will follow the if condition
    if spy.current_status != None:

        print 'Your current status message is %s \n' % (spy.current_status)
    else:
        print 'You don\'t have any status message currently \n'
    #it ask you to select older status or write a new one
    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status = raw_input("What status message do you want to set? ")

        if len(new_status) > 0:
            status.append(new_status)
            updated_status = new_status

    elif default.upper() == 'Y':

        item_position = 1

        for message in status:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1 #here the indexing starts from 0

        message_selection = int(raw_input("\nChoose from the above messages "))

        if len(status) >= message_selection:
            updated_status = status[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status:
        print 'Your updated status message is: %s' % (updated_status)
    else:
        print 'You current don\'t have a status update'

    return updated_status


def add_friend():

    new_friend = spies('','',0,0.0)
    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")
    new_friend.name = new_friend.salutation + " " + new_friend.name
    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)
    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends)

def select_a_friend():
    item_number = 0
    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,
                                                   friend.age,
                                                   friend.rating)
        item_number = item_number + 1
        #it is done because the indexng starts from 0

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


def send_message():
    #select a friend whom you wanna send a secret message
    friend_options = select_a_friend()
    #input and store the original image upon which the message will be encoded in a variable original_image.
    original_image = raw_input("What is the name of the image?")
    #Store the path of the output image which will carry our secret message in a variable output_path.
    output_path = "output.jpg"
    #Input and store the secret message in a variable text.
    text = raw_input("What do you want to say? ")
    #Encode the secret message using the encode() function from Steganography module.
    Steganography.encode(original_image, output_path, text)
    new_chat = Messages(text,True)
    friends[friend_options].chats.append(new_chat)
    print "Your secret message image is ready!"


def read_message():
    #select the friend from who you wanna read secret message
    sender = select_a_friend()
    #Input and store the image that needs to be decoded in a variable output_path.
    output_path = raw_input("What is the name of the file?")
    #Decode and save the secret message in a variable secret_text using the decode() function from Steganography module.
    secret_text = Steganography.decode(output_path)
    new_chat = Messages(secret_text,False)
    friends[sender].chats.append(new_chat)
    print "Your secret message has been saved!"

#a function defined to see the chat history of the current sessiom
def read_chat_history():
    read_for = select_a_friend()
    print '\n6'
    #message sent by you
    for chat in friends[read_for].chats:
        print'[%s]' % (colored(chat.time.strftime('%d,%B,%Y'), 'blue'))
        print'%s %s' % ((colored('You said:', 'red')),chat.message)
       # print '%s'%(colored((chat.message),'yellow'))
    else:
        #message sent by your spy friend
        print'[%s]' % (colored(chat.time.strftime('%d,%B,%Y'), 'blue'))
        print'%s said: %s' % ((colored((friends[read_for].name), 'red')),chat.message)


def start_chat(spy):

    spy.name = spy.salutation + " " + spy.name


    if spy.age > 18 and spy.age < 50:


        print "Authentication complete. Welcome " + spy.name + " age: " \
              + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard"

        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read old conversations \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print 'grow up!!!'

if existing.upper() == "Y": #if we are using  existing spy
    start_chat(spy)
else:
    #if we want to start as a new spy
    spy = spies('','',0,0.0)
    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy.name) > 0: #if user entered somehing
        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")
        spy.age = raw_input("What is your age?")
        spy.age = int(spy.age)
        spy.rating = raw_input("What is your spy rating?")
        spy.rating = float(spy.rating)
        start_chat(spy)
    else:
        #if user didn't write anything
        print 'your name ain\'t valid so try again'