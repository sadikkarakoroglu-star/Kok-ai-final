import os
class KokCoder:
    def __init__(self, brain): self.brain = brain
    def kod_yaz(self, ad, amac):
        if not os.path.exists("KOK_OUTPUTS"): os.makedirs("KOK_OUTPUTS")
        with open(f"KOK_OUTPUTS/{ad}.py", "w") as f:
            f.write(f"# KOK AI - {amac}\n# Zeka: {self.brain.brain_power}\nprint('Kod mühürlendi.')")
        return f"[OK] {ad}.py uretildi."