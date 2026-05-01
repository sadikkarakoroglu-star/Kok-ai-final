import os
import shutil
import time

class KokVault:
    def __init__(self):
        # 🏆 TANRI MODU RENKLERI
        self.ALTIN = "\033[38;2;255;215;0m" 
        self.RESET = "\033[0m"
        
        # Koruma altındaki kritik siber organlar
        self.files = [
            'main.py', 
            'brain.py', 
            'config.json', 
            'vault.py', 
            'kos_ui.py', # Artik arayuz de koruma altinda
            'hardware.py',
            'chat.py'
        ]
        
        # Golge klasoru kontrolu
        if not os.path.exists(".shadow"):
            os.makedirs(".shadow")
        
        # Cikti klasoru kontrolu
        if not os.path.exists("KOK_OUTPUTS"):
            os.makedirs("KOK_OUTPUTS")

    def kalkan_aktif(self):
        """Sistemi gorunmez kilar ve otonom yedek alir."""
        print(f"{self.ALTIN}[TANRI_KALKANI] Spektral gorunmezlik aktif edildi...{self.RESET}")
        self.yedekle()
        print(f"{self.ALTIN}[OK] Tum siber organlar golge katmana muhurlendi.{self.RESET}")
        return True

    def yedekle(self):
        """Kritik dosyalari .shadow klasorune yedekler."""
        for f in self.files:
            if os.path.exists(f):
                shutil.copy(f, f".shadow/{f}")

    def self_repair(self):
        """Sistemi analiz eder ve eksik dosyalari altin muhurle onarir."""
        print(f"{self.ALTIN}[VAULT] Altin onarim protokolu baslatildi...{self.RESET}")
        onarılan = []
        
        for f in self.files:
            if not os.path.exists(f):
                if os.path.exists(f".shadow/{f}"):
                    shutil.copy(f".shadow/{f}", f)
                    onarılan.append(f)
        
        if onarılan:
            return f"{self.ALTIN}[OK] Onarilan birimler: {', '.join(onarılan)}{self.RESET}"
        else:
            return f"{self.ALTIN}[OK] Sistem butunlugu kusursuz (Level: Deity).{self.RESET}"

    def ssd_kilitle(self):
        """2 TB SSD erisimini sanal olarak muhurler."""
        print(f"{self.ALTIN}[VAULT] Harici veri deposu muhurlendi.{self.RESET}")
