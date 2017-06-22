from datetime import datetime
class spies:
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status = None


class Messages:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = spies('Abhinav', 'Mr.', 21, 4.7)

friend_one = spies('jerry', 'Mr.', 22, 7.1)
friend_two = spies('george', 'Ms.', 21, 9.9)
friend_three = spies('kramer', 'Dr.', 23, 10)


friends = [friend_one, friend_two, friend_three]