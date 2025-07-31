from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):
    def build(self):
        self.operators = ['+', '-', '*', '/', '%']
        self.last_was_operator = None
        self.last_button = None

        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        self.solution = TextInput(
            multiline=False,
            readonly=True,
            halign="right",
            font_size=40
        )
        main_layout.add_widget(self.solution)

        buttons = [
            ["AC", "⌫", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="]
        ]

        for row in buttons:
            h_layout = BoxLayout(spacing=10)
            for label in row:
                button = Button(
                    text=label,
                    font_size=32,
                    on_press=self.on_button_press
                )
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "AC":
            self.solution.text = ""
        elif button_text == "⌫":
            self.solution.text = current[:-1]
        elif button_text == "=":
            try:
                self.solution.text = str(eval(current))
            except:
                self.solution.text = "Error"
        else:
            if current == "Error":
                self.solution.text = ""
            self.solution.text += button_text


if __name__ == "__main__":
    CalculatorApp().run()
