import time, random
from kivy.metrics import dp
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivymd.uix.datatables import MDDataTable
import random


def create_motivation_quotes():
    motivation_quotes = [
        "Code your dreams into reality.",
        "The only way to do great work is to love what you do.",
        "Embrace the struggle; it leads to success.",
        "Stay curious and keep coding.",
        "Success is a series of small wins.",
        "Failure is the opportunity to begin again, only more intelligently. ",
        "Every line of code is a step toward mastery.",
        "Dream big, program bigger.",
        "The best way to predict the future is to create it.",
        "Coding is the art of turning ideas into innovation.",
        "Stay committed; the code will follow.",
        "In the world of code, persistence is your superpower.",
        "Success is built on the foundation of failures.",
        "Write code today for a better tomorrow.",
        "Your code can change the world.",
        "Embrace the challenge, for in the world of code, your persistence will be the key to unlocking greatness.",
    ]

    return random.choices(motivation_quotes)


KV = """
MDScreen:
    id:main
    MDLabel:
        id: label_1
        markup:True
        halign:"center"
        size_hint:.9,.5
        pos_hint:{"top":1.2}

    MDLabel:
        id:label_2
        markup:True
        halign:"center"
        size_hint:.9,.5
        pos_hint:{"top":.4}
"""


class MainApp(MDApp):
    # self.word_index = 0
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def on_start(self):
        self.message = random.choice(
            [
                "Greetings Noah, I trust you're doing well. It's @, and according to my understanding, today is the day you're supposed to begin learning @.",
                "Hey Noah, I hope all is well with you. As per my information, today being @, it's time for you to start learning @.",
                "Hi Noah, I wish you're having a good day. Today is @, and based on what I know, you should start learning @ today.",
                "Hello Noah, I hope everything is going fine. As of today, which is @, it's expected that you begin your @ learning journey.",
                "Hey Noah, I hope you're in good spirits. It's @ today, and from what I know, you have to kickstart your @ learning.",
                "Greetings Noah, I trust you're doing well. Today is @, and by my calculations, it's the day earmarked for you to learn @.",
                "Hi Noah, I hope you're having a great day. As per my knowledge, today being @, you are scheduled to learn @.",
                "Hey Noah, I wish you well. Today is @, and based on what I know, it's time for you to dive into @ learning.",
                "Hello Noah, I hope everything is going smoothly. As of today, which happens to be @, it's expected that you start learning @.",
                "Greetings Noah, I hope you're feeling good. Today is @, and according to my understanding, today is your designated day to learn @.",
                "Hi Noah, I hope all is well. As per my information, today is @, and it's the day you've set aside to begin learning @.",
                "Hey Noah, I wish you a wonderful day. It's @ today, and based on what I know, you're supposed to commence your @ learning today.",
            ]
        )
        C1, C2, C3 = self.message.split("@")
        day = time.strftime("%A")
        Table = {
            "Monday": "Python (Advanced Topics)",
            "Tuesday": "Python (Flask, DBs,APIs)",
            "Wednesday": "JavaScript,HTML,CSS (web dev)",
            "Thursday": "C",
            "Friday": "DSA (Python)",
            "Saturday": "Projects...",
            "Sunday": "Machine Learning (Python)",
        }
        self.message = f"[color=#00FFFF]{C1}{day}\n{C2}{Table[day]}\n{C3}[/color]"
        self.word_index = 0
        self.root.ids.label_1.text = f"Noah remember today is {day} SO [color=#00FF00]{create_motivation_quotes()[0]}[/color]"

        self.table = MDDataTable(
            size_hint=(1, 0.5),
            pos_hint={"top": 0.75},
            use_pagination=True,
            rows_num=9,
            background_color="#000000",
            background_color_cell="#0F0F0F",
            background_color_selected_cell="#FF686B72",
            # background_color_header="#5D8AA8",
            column_data=[
                ("DAY", dp(20)),
                ("ACTIVITY", dp(70)),
            ],
            row_data=[(k, v) for k, v in Table.items()],
        )

        self.root.add_widget(self.table)
        Clock.schedule_interval(self.update_word, 0.05)  # Schedule the update function

    def on_leave(self):
        Clock.unschedule(
            self.update_word
        )  # Unschedule the update function when leaving the screen

    def update_word(self, dt):
        if self.word_index < len(self.message):
            self.root.ids.label_2.text += self.message[
                self.word_index
            ]  # Append the next letter
            self.word_index += 1
        else:
            Clock.unschedule(
                self.update_word
            )  # Stop updating when all letters are displayed


MainApp().run()
