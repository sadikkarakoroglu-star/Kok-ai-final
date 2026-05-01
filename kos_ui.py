from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse
import random, threading, time

# SİSTEM ORGANLARI
try:
    from brain import KokBrain
    from hardware import KokHardware
    from vault import KokVault
    from chat import KokChat
    from ghost_link import GhostLink
    import androidhelper
    droid = androidhelper.Android()
except Exception as e:
    print(f"[!] Baglanti Hatasi: {e}")
    droid = None

class KOS_Deity_UI(App):
    def build(self):
        Window.clearcolor = (0.01, 0.01, 0.01, 1)
        
        # ORGANLARI BAŞLAT
        self.brain = KokBrain()
        self.hw = KokHardware()
        self.vault = KokVault()
        self.chat = KokChat(self.brain)
        self.ghost = GhostLink()
        
        self.ALTIN = (1.0, 0.84, 0.0, 1) 
        self.layout = BoxLayout(orientation='vertical', padding=25, spacing=15)

        # 👑 Üst Panel
        self.header = Label(
            text=f"K-OS DEITY MODE\nZEKA: {self.brain.brain_power:.2f}",
            font_size='24sp', bold=True, halign='center', color=self.ALTIN
        )
        self.layout.add_widget(self.header)

        self.console = Label(text="[ SİSTEM ÇELİK GİBİ ]", font_size='16sp', color=self.ALTIN)
        self.layout.add_widget(self.console)

        # 📊 Canlı Nabız
        self.hw_label = Label(text="Analiz...", font_size='18sp', color=self.ALTIN)
        self.layout.add_widget(self.hw_label)
        Clock.schedule_interval(self.update_ui, 0.5)

        # 🕹️ Kontrol Gridi
        btn_grid = BoxLayout(orientation='vertical', spacing=20, size_hint_y=0.5)
        
        row1 = BoxLayout(orientation='horizontal', spacing=20)
        self.add_btn(row1, "HASAT", self.ALTIN, (0,0,0,1))
        self.add_btn(row1, "RADAR", self.ALTIN, (0,0,0,1))
        
        row2 = BoxLayout(orientation='horizontal', spacing=20)
        self.add_btn(row2, "KALKAN", (0.2, 0.2, 0.2, 1), self.ALTIN)
        self.add_btn(row2, "KONUS", (0, 0.5, 0.8, 1), (1,1,1,1))

        btn_grid.add_widget(row1)
        btn_grid.add_widget(row2)
        self.layout.add_widget(btn_grid)
        return self.layout

    def add_btn(self, target, txt, bg, fg):
        btn = Button(text=txt, background_color=bg, color=fg, bold=True, font_size='20sp')
        # on_release dokunmatik cihazlar için en garantisidir
        btn.bind(on_release=self.komut_atesle) 
        target.add_widget(btn)

    def update_ui(self, dt):
        d = self.hw.anlik_izle()
        self.hw_label.text = f"CPU: %{d['cpu']} | ISI: {d['temp']}°C"
        self.header.text = f"K-OS DEITY MODE\nZEKA: {self.brain.brain_power:.2f}"

    def komut_atesle(self, instance):
        komut = instance.text
        self.console.text = f"[!] {komut} İŞLENİYOR..."
        self.kivilcim_efekti()
        if droid: droid.vibrate(40)
        
        # 🚀 THREADING: İşlemciyi yoran işleri arka planda yap, ekran donmasın kanka!
        threading.Thread(target=self.arka_plan_islem, args=(komut,)).start()

    def arka_plan_islem(self, komut):
        try:
            if komut == "HASAT":
                self.brain.gercek_hasat(self.ghost)
            elif komut == "RADAR":
                self.ghost.derin_sizma_tara()
            elif komut == "KALKAN":
                self.vault.kalkan_aktif()
            elif komut == "KONUS":
                self.chat.sohbet_baslat()
        except Exception as e:
            print(f"Hata: {e}")

    def kivilcim_efekti(self):
        with self.layout.canvas.after:
            Color(1, 0.84, 0, 1)
            for _ in range(12):
                Ellipse(pos=(random.uniform(0, Window.width), random.uniform(0, Window.height)), size=(6, 6))
        Clock.schedule_once(lambda dt: self.layout.canvas.after.clear(), 0.3)

if __name__ == "__main__":
    KOS_Deity_UI().run()
