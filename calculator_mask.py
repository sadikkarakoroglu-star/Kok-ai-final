from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.clock import Clock

# Siber Tanrı arayüzünü içeri alıyoruz kanka
try:
    from kos_ui import KOS_Deity_UI 
except ImportError:
    KOS_Deity_UI = None

class KOS_Maske(App):
    def build(self):
        self.title = "Hesap Makinesi"
        # Standart uygulama görünümü için renkler
        Window.clearcolor = (0.98, 0.98, 0.98, 1)
        
        layout = BoxLayout(orientation='vertical', padding=5, spacing=5)
        
        # 📟 Hesap Makinesi Ekranı
        self.display = TextInput(
            text="", 
            font_size=60, 
            readonly=True, 
            halign='right', 
            multiline=False,
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1),
            size_hint_y=0.25
        )
        layout.add_widget(self.display)
        
        # ⌨️ Buton Izgarası
        grid = GridLayout(cols=4, spacing=2)
        
        btns = [
            'C', '(', ')', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=', '%'
        ]
        
        for b in btns:
            text_clr = (1, 0.5, 0, 1) if b in '/*-+=' else (0, 0, 0, 1)
            btn = Button(
                text=b, 
                font_size=30,
                color=text_clr,
                background_normal='', 
                background_color=(1, 1, 1, 1) if b not in '/*-+=' else (0.95, 0.95, 0.95, 1)
            )
            btn.bind(on_press=self.tus_basildi)
            grid.add_widget(btn)
            
        layout.add_widget(grid)
        return layout

    def tus_basildi(self, instance):
        text = instance.text
        
        if text == 'C':
            self.display.text = ""
        elif text == '=':
            # 🌀 GİZLİ GEÇİT: Master Key
            if self.display.text == "1327":
                self.stop() # Maskeyi kapat
                if KOS_Deity_UI:
                    KOS_Deity_UI().run() # SİBER TANRI UYANDI!
            else:
                try:
                    # Gerçek hesaplama motoru
                    self.display.text = str(eval(self.display.text))
                except:
                    self.display.text = "0"
        else:
            self.display.text += text

if __name__ == "__main__":
    KOS_Maske().run()
