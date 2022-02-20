import pyperclip, re


class MyRegexes:
    
    def __init__(self):
        self.mobilePhoneNumberRegex = re.compile(r'''(
                (091[0-9]|099[0-4]|093[02356-9]|090[0-5]|092[0-2]) # operator code
                (\d{7})                                            # seven digits after operator code
                )''', re.VERBOSE)
        self.emailRegex = re.compile(r'''(
                [a-zA-Z0-9._%+-]+                                  # username
                @                                                  # @ symbol
                [a-zA-Z0-9.-]+                                     # domain name
                (\.[a-zA-Z]{2,4})                                  # dot-something
                )''', re.VERBOSE)
        self.text = str(pyperclip.paste())                         # put clipboard's content to the text variable
        self.matches = [] 

    def find_mobile_phone_numbers(self):
        for groups in self.mobilePhoneNumberRegex.findall(self.text):
            mobilePhoneNumber = '-'.join([groups[1], groups[2]])
            self.matches.append(mobilePhoneNumber)
        if len(self.matches) > 0:
            pyperclip.copy('\n'.join(self.matches))
    
    def find_email_addresses(self):
        for groups in self.emailRegex.findall(self.text):
            emailaddress = groups[0]
            self.matches.append(emailaddress)
        if len(self.matches) > 0:
            pyperclip.copy('\n'.join(self.matches))


class Program:

    def __init__(self):    
        self.start = MyRegexes()
        self.choice = self.show_options_and_get_choice()
        if self.choice == '1':
            self.start.find_mobile_phone_numbers()
        elif self.choice == '2':
            self.start.find_email_addresses()     

    def show_options_and_get_choice(self):
        print('1-Phone Number\n2-Email')
        choice = input('Please enter your choice number: ')
        return choice


run = Program()



    