import time
class KokUpdater:
    def sistem_kontrol(self): return f"Senkron: {time.ctime()}"
    def guncelleme_tara(self): return "Kernel_V2_Optim"
    def otonom_yama_yap(self, brain, pkg): brain.learn_new_skill(pkg); return "[OK] Guncellendi."