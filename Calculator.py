from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window

Window.size = (400, 600)

class CalculatorApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.output_label = Label(size_hint_y=0.3, font_size=48, text='')
        button_grid = GridLayout(cols=4, size_hint_y=1.5, spacing=5)
        
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', '=', '+'
        ]
        
        for symbol in buttons:
            btn = Button(text=symbol, font_size=32)
            if symbol == '=':
                btn.bind(on_press=self.evaluate_result)
            else:
                btn.bind(on_press=self.on_button_press)
            button_grid.add_widget(btn)
        
        clear_btn = Button(text='Clear', size_hint_y=0.2, font_size=32)
        clear_btn.bind(on_press=self.clear_output)
        
        self.output_label.bind(height=self.resize_font)
        
        root.add_widget(self.output_label)
        root.add_widget(button_grid)
        root.add_widget(clear_btn)
        
        return root

    def on_button_press(self, instance):
        self.output_label.text += instance.text

    def evaluate_result(self, instance):
        try:
            if self.output_label.text.strip():
                self.output_label.text = str(eval(self.output_label.text))
        except SyntaxError:
            self.output_label.text = 'Syntax Error!'
        except Exception as e:
            self.output_label.text = f'Error: {e}'

    def clear_output(self, instance):
        self.output_label.text = ""

    def resize_font(self, instance, value):
        instance.font_size = 0.5 * instance.height

if __name__ == '__main__':
    CalculatorApp().run()
