import vk
from getpass import getpass
from tkinter import Tk, Label, Entry, Button, Text

APP_ID = -1  # Replace with your VK app_id


class VKFriendsGUI:
    def __init__(self, master):
        self.master = master
        master.title("VK Friends Online Checker")

        self.label_login = Label(master, text="Enter your VK login:")
        self.label_login.pack()

        self.entry_login = Entry(master)
        self.entry_login.pack()

        self.label_password = Label(master, text="Enter your VK password:")
        self.label_password.pack()

        self.entry_password = Entry(master, show="*")
        self.entry_password.pack()

        self.result_text = Text(master, height=10, width=40)
        self.result_text.pack()

        self.check_online_button = Button(master, text="Check Online Friends", command=self.check_online_friends)
        self.check_online_button.pack()

    def check_online_friends(self):
        login = self.entry_login.get()
        password = self.entry_password.get()
        friends_online = get_online_friends(login, password)
        self.output_friends_to_console(friends_online)

    def output_friends_to_console(self, friends_online):
        self.result_text.delete(1.0, 'end')
        if friends_online:
            self.result_text.insert('end', "Online Friends:\n")
            for friend in friends_online:
                self.result_text.insert('end', f"{friend['first_name']} {friend['last_name']}\n")
        else:
            self.result_text.insert('end', "No online friends.")


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    try:
        friends_online = api.friends.getOnline()
        return friends_online
    except vk.exceptions.VkAuthError:
        print("Authentication failed. Please check your login and password.")
        return None


if __name__ == '__main__':
    root = Tk()
    app = VKFriendsGUI(root)
    root.mainloop()
