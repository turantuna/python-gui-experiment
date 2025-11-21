import random
import string
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class PasswordGenerator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.add_widget(Label(text='Enter password length:'))
        self.length_input = TextInput(multiline=False, input_filter='int')
        self.add_widget(self.length_input)

        generate_btn = Button(text='Generate Password')
        generate_btn.bind(on_press=self.generate_password)
        self.add_widget(generate_btn)

        self.password_label = Label(text='Your password will appear here')
        self.add_widget(self.password_label)

    def generate_password(self, instance):
        try:
            length = int(self.length_input.text)
            if length <= 0:
                self.password_label.text = 'Enter a positive number.'
                return

            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_label.text = password
        except:
            self.password_label.text = 'Invalid input. Please enter a number.'


class PasswordApp(App):
    def build(self):
        return PasswordGenerator()


if __name__ == '__main__':
    PasswordApp().run()