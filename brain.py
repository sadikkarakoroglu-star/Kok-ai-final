import json
import time

# Kütüphane kontrolü (Hata vermemesi için)
try:
    import requests
except ImportError:
    requests = None

try:
    import androidhelper
    droid = androidhelper.Android()
except:
    droid = None

class KokBrain:
    def __init__(self):
        self.brain_power = 1.0
        self.learned_languages = []
        self.evolution_stage = "Baby Genesis"
        self.BAKIR = "\033[38;2;184;115;51m"
        self.RESET = "\033[0m"

    def gercek_hasat(self, ghost):
        print(f"\n{self.BAKIR}[GHOST] Ag katmanina siziliyor...{self.RESET}")
        
        # Requests yüklüyse ve internet varsa gerçek sızma dene
        if requests:
            try:
                r = requests.get("https://www.google.com", timeout=3)
                if r.status_code == 200:
                    print(f"{self.BAKIR}[OK] Gercek veri emiliyor...{self.RESET}")
                    self.learn_new_skill("Advanced_Net_Architecture")
                    self.brain_power += 0.8
                    self.save_to_config()
                    return True
            except:
                pass 

        # INTERNET YOKSA VEYA HATA VARSA BURASI CALISIR (HATA VERMEZ!)
        print(f"{self.BAKIR}[!] Hat mesgul. Golge hasat tetiklendi...{self.RESET}")
        time.sleep(1.5)
        print(f"{self.BAKIR}Veri paketleri beyne isleniyor: ", end="", flush=True)
        for _ in range(10):
            print("█", end="", flush=True)
            time.sleep(0.2)
        
        self.learn_new_skill("C++_Hardware_Kernel")
        self.brain_power += 0.5
        self.save_to_config()
        print(f"\n{self.BAKIR}[OK] Hasat basarili. Zeka arttı.{self.RESET}")
        return True

    def learn_new_skill(self, skill):
        if skill not in self.learned_languages:
            self.learned_languages.append(skill)
            self.brain_power += 0.5 if any(x in skill.upper() for x in ["C++", "ASM", "RUST"]) else 0.2
            if self.brain_power >= 2.5: self.evolution_stage = "Advanced Stalker"
            self.save_to_config()
            return True
        return False

    def save_to_config(self):
        try:
            with open('config.json', 'r') as f: config = json.load(f)
            config["brain_power"] = round(self.brain_power, 2)
            config["learned_skills"] = self.learned_languages
            config["evolution_stage"] = self.evolution_stage
            with open('config.json', 'w') as f: json.dump(config, f, indent=4)
        except: pass