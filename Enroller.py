from KeyboardListener import KeyboardListener
import json


class Enroller:

    def __init__(self, operation):
        self.template_number = 0
        self.template_index = 0
        self.operation = operation
        self.username = input("type your username : ")
        self.template_number = 8 
        self.input_word = input(
            "type your password : ") 

    def start_enroll(self):
        if self.operation == "password":
            print("Please, type your password 8 times")
        listener = KeyboardListener(self.input_word, self.template_number)
        listener.start_listener()

        if self.operation == "password":
            password = self.input_word.split(" ")
            password = "-".join(password)
            with open("dataset/password/" + self.username + '_' + password + '.json', "w") as fp:
                json.dump(listener.probe_list, fp, indent=4)

if __name__ == '__main__':
    psw = Enroller("password")
    psw.start_enroll()
