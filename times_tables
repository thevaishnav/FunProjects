"""
A simple Python project to anticipate the Beauty of Mathematics.
The following project generates times tables visually.
See Mathologer video on Times Tables: https://youtu.be/qhbuKbxJsk8
GUI Parameters:
    Radii: Radius of the Circle
    Radii Increment: By how much the radius should change when keyboard shortcut is used.
    Total Dots: How many dots should be placed on circle.
    Dots Increment: By how much the total number of dots should change when keyboard shortcut is used
    Times: Times table of which number.
    Times Increment: By how much the times number should change when keyboard shortcut is used
    Color: Color of the circle.

Controls:
    Mouse Wheel: Controls Radius of Circle
    Up / Down Arrow: Changes number of Dots
    Left / Right Arrow: Changes Times number
    Double Click on the canvas, changes position of the Circle
    Right Click and Drag, to drag the canvas location.
"""

from math import sin, cos, pi, tan
from tkinter import *
from tkinter.colorchooser import askcolor

clamp = lambda n, minn, maxn: max(min(maxn, n), minn)
def avg(*args):
    sum = 0
    for num in [*args]:
        sum += num

    return sum/len([*args])


class GUI():
    def definemain(self):
        self.redii = 250
        self.inredii = 250
        self.points = 500
        self.times = 3
        self.color = "red"
        self.redlap = 10
        self.timelap = 1
        self.pointlap = 5
        self.canw = 1700
        self.canh = 700
        self.xpos, self.ypos = 850, 350
        self.defx = "r*sin(t)"
        self.defy = "r*cos(t)"

    def run(self):
        self.root = Tk()
        self.root.state("zoomed")
        self.can_frame = Frame(self.root, bg="black")
        self.frame1 = Frame(self.root, bg="#202020")
        self.frame3 = Frame(self.root, bg="#202020")

        self.frame1.pack(side=TOP, expand=0, fill=X)
        self.frame3.pack(side=TOP, expand=0, fill=X)
        self.can_frame.pack(side=TOP, fill=BOTH, expand=1)

        self.definemain()
        self.create_canvas()
        self.create_entries_labels()

        self.root.bind("<Any-Key>", self.increament)
        self.root.bind("<Double-Button-1>", self.reposition)
        self.root.bind("<MouseWheel>", self.change_redii)
        self.update_all()
        self.root.mainloop()

    def create_entries_labels(self):
        sep = 0
        self.redii_var, self.redii_inc = StringVar(), StringVar()
        self.dot_var, self.dot_inc = StringVar(), StringVar()
        self.time_var, self.time_inc = StringVar(), StringVar()

        Label(self.frame1, bg="#202020", fg="#CCCCCC", text="Radii:   ").grid(row=0, column=0)
        Entry(self.frame1, bg="#202020", fg="#CCCCCC", relief=GROOVE, textvariable=self.redii_var).grid(row=0, column=1)
        Label(self.frame1, bg="#202020", fg="#CCCCCC", text="          Radii Increment:   ").grid(row=0, column=2)
        Entry(self.frame1, bg="#202020", fg="#CCCCCC", relief=GROOVE, textvariable=self.redii_inc).grid(row=0, column=3)
        Label(self.frame1, bg="#202020", fg="#CCCCCC", text="          Total Dots: ").grid(row=0, column=4)
        Entry(self.frame1, bg="#202020", fg="#CCCCCC", relief=GROOVE, textvariable=self.dot_var).grid(row=0, column=5)
        Label(self.frame1, bg="#202020", fg="#CCCCCC", text="          Dots Increment: ").grid(row=0, column=6)
        Entry(self.frame1, bg="#202020", fg="#CCCCCC", relief=GROOVE, textvariable=self.dot_inc).grid(row=0, column=7)

        Label(self.frame1, bg="#202020", fg="#CCCCCC", text="Times: ").grid(row=1, column=0)
        Entry(self.frame1, bg="#202020", fg="#CCCCCC", relief=GROOVE, textvariable=self.time_var).grid(row=1, column=1)
        Label(self.frame1, bg="#202020", fg="#CCCCCC", text="          Times Increment:  ").grid(row=1, column=2)
        Entry(self.frame1, bg="#202020", fg="#CCCCCC", relief=GROOVE, textvariable=self.time_inc).grid(row=1, column=3)
        Label(self.frame1, bg="#202020", fg="#CCCCCC", text="          Color:  ").grid(row=1, column=4)
        self.color_butt = Button(self.frame1, bg="red", text="", command=self.change_color, relief=FLAT, width=23, font="Arial 6")
        self.color_butt.grid(row=1, column=5)
        inst1 = "         Double Click anywhere to reset diagram position."
        inst2 = "         Use up/down arrow buttons to change number of dots."
        inst3 = "         Use left and right arrows to change times."
        inst4 = "         Use Mouse wheel to change circle radius."
        inst5 = "         Left click and drag to Scroll"
        Label(self.frame1, bg="#202020", fg="#909090", text=inst1).grid(row=0, column=8, sticky=W)
        Label(self.frame1, bg="#202020", fg="#909090", text=inst5).grid(row=0, column=9, sticky=W)
        Label(self.frame1, bg="#202020", fg="#909090", text=inst3).grid(row=1, column=8, sticky=W)
        Label(self.frame1, bg="#202020", fg="#909090", text=inst4).grid(row=1, column=9, sticky=W)
        Label(self.frame1, bg="#202020", fg="#909090", text=inst2).grid(row=1, column=6, columnspan=2)


        # Button(self.frame2, text=f"Recenter", command=self.reset).pack(side=LEFT, fill=BOTH, expand=0)
        # Label(self.frame2, bg="white", text=" " * sep).pack(side=LEFT, fill=BOTH, expand=0, anchor=E)

        self.redii_var.set(self.redii)
        self.dot_var.set(self.points)
        self.time_var.set(self.times)
        self.redii_inc.set(self.redlap)
        self.dot_inc.set(self.pointlap)
        self.time_inc.set(self.timelap)

        self.redii_var.trace_add("write", self.update_all)
        self.dot_var.trace_add("write", self.update_all)
        self.time_var.trace_add("write", self.update_all)
        self.redii_inc.trace_add("write", self.update_all)
        self.dot_inc.trace_add("write", self.update_all)
        self.time_inc.trace_add("write", self.update_all)
        self.redii_var.trace_add("write", self.update_all)

    def create_canvas(self):
        self.can = Canvas(self.can_frame, width=400, height=400, bg="black", scrollregion=(0, 0, 1700, 700), relief=FLAT)
        self.hsb = Scrollbar(self.can_frame, orient="horizontal")
        self.vsb = Scrollbar(self.can_frame, orient="vertical")

        self.hsb.config(command=self.can.xview)
        self.vsb.config(command=self.can.yview)
        self.can.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)
        self.can.bind("<B1-Motion>", self.scroll_move)
        self.can.bind("<ButtonPress-1>", self.scroll_start)

        self.hsb.pack(side=BOTTOM, fill=X)
        self.vsb.pack(side=RIGHT, fill=Y)
        self.can.pack(side=RIGHT, fill=BOTH, expand=1)

    def scroll_move(self, event):
        self.can.scan_dragto(event.x, event.y, gain=1)

    def scroll_start(self, event):
        self.can.scan_mark(event.x, event.y)

    def draw(self):
        self.can.delete("all")
        for x in range(self.points):
            inx = self.redii * cos((2 * x * pi) / self.points) + self.xpos
            iny = self.redii * sin((2 * x * pi) / self.points) + self.ypos

            x += 1
            fix = self.redii * cos((2 * x * pi) / self.points) + self.xpos
            fiy = self.redii * sin((2 * x * pi) / self.points) + self.ypos
            self.can.create_line(inx, iny, fix, fiy, fill=self.color)

            x -= 1
            x = (x * self.times) % self.points
            fix = self.redii * cos((2 * x * pi) / self.points) + self.xpos
            fiy = self.redii * sin((2 * x * pi) / self.points) + self.ypos
            self.can.create_line(inx, iny, fix, fiy, fill=self.color)

    def increament(self, event=None):
        if event.keysym.lower() == "up":
            self.points += int(self.dot_inc.get())
            self.dot_var.set(self.points)
            self.draw()

        if event.keysym.lower() == "down":
            self.points -= int(self.dot_inc.get())
            if self.points <= 1:
                self.points = 2
            self.dot_var.set(self.points)
            self.draw()

        if event.keysym.lower() == "left":
            self.times -= float(self.time_inc.get())
            self.time_var.set(self.times)
            self.draw()

        if event.keysym.lower() == "right":
            self.times += float(self.time_inc.get())
            self.time_var.set(self.times)
            self.draw()

    def reposition(self, event=None):
        self.xpos, self.ypos = event.x, event.y
        self.draw()

    def change_color(self, event=None):
        self.color = askcolor()
        self.color = list(self.color)[1]
        self.color_butt.config(bg=self.color)
        self.draw()

    def update_all(self, v1=None, v2=None, v3=None):
        try:
            self.redii = clamp(float(self.redii_var.get()), 10, 500)
            ratio = self.redii / self.inredii
            self.canw = 1700 * ratio
            self.canh = 700 * ratio
            self.can.config(scrollregion=(0, 0, self.canw, self.canh))

            self.points = clamp(int(self.dot_var.get()), 10, 1000)
            self.times = clamp(float(self.time_var.get()), -100, 100)
            self.timelap = clamp(float(self.time_inc.get()), 0, 50)
            self.redlap = clamp(float(self.redii_inc.get()), 0, 50)
            self.pointlap = clamp(int(self.dot_inc.get()), 1, 50)
            self.draw()

        except ValueError: pass

    def change_redii(self, event):
        if event.delta < 0:
            self.redii -= self.redlap
            ratio = self.redii/self.inredii
            self.canw = 1700*ratio
            self.canh = 700*ratio
            self.can.config(scrollregion=(0, 0, self.canw, self.canh))

        if event.delta > 0:
            self.redii += self.redlap
            if self.redii <= 0:
                self.redii = 1
            ratio = self.redii / self.inredii
            self.canw = 1700*ratio
            self.canh = 700*ratio
            self.can.config(scrollregion=(0, 0, self.canw, self.canh))
        self.redii_var.set(self.redii)
        self.draw()

    def reset(self):
        self.xpos, self.ypos = self.canw/2, self.canh/2
        self.draw()


gui = GUI()
gui.run()
