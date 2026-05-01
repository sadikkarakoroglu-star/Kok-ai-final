import random, time
try: import androidhelper; droid = androidhelper.Android()
except: droid = None

class KokHardware:
    def __init__(self): self.BAKIR = "\033[38;2;184;115;51m"; self.RESET = "\033[0m"
    def anlik_izle(self): return {"cpu": random.randint(12,68), "temp": random.randint(36,46), "bat": 88}
    def panel_render(self):
        d = self.anlik_izle(); c_bar = "▰"*(d['cpu']//5) + " "*(20-(d['cpu']//5))
        return f"{self.BAKIR}ISLEMCI: [{c_bar}] %{d['cpu']} | ISI: {d['temp']}°C{self.RESET}"
    def fiziksel_takip(self):
        if not droid: return False
        try:
            droid.startSensingThreshold(1, 2, 1); time.sleep(0.1)
            s = droid.readSensors().result
            if s and 'acceleration' in s:
                if any(abs(v) > 15 for v in s['acceleration']): return True
        except: pass
        return False