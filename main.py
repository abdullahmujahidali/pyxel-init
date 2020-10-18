import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Abdullah Mujahid")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(55, 41, "Abdullah, Pyxel!", pyxel.frame_count % 16)
        pyxel.blt(61, 66, 0, 0, 0, 38, 16)

App()