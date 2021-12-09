from tkinter import *
from tkinter.messagebox import showinfo
import random

# Define Variables
BARS = 50
STATE_SORTED = 1
STATE_RANDOMIZED = 2
STATE_SORTING_B = 3
STATE_SORTING_I = 4
STATE_SORTING_M = 5
STATE_SORTING_Q = 6


def is_sorting(cur_state: int) -> bool:
    # Returns if the variable "cur_state" represents a state that is used while sorting algorithm is running
    return cur_state >= STATE_SORTING_B


class Bar(Label):
    def __init__(self, master, bars, height, loc):
        self.H = height
        self.main_master = master
        self.bars = bars
        H = str(height)
        if len(H) == 1: H = "0" + H
        super().__init__(master, bg="#222222", fg="white", text="      " + "\n" * height, font="Times 10", relief=FLAT)

        self.grid(row=0, column=loc, sticky=S, padx=1, pady=4)
        self._loc = loc

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return str(self.H)

    def __eq__(self, other):
        return self.H == other.H

    def __ne__(self, other):
        return self.H != other.H

    def __lt__(self, other):
        return other.H > self.H

    def __gt__(self, other):
        return other.H < self.H

    def __le__(self, other):
        return other.H >= self.H

    def __ge__(self, other):
        return other.H <= self.H

    @property
    def loc(self): return self._loc

    @loc.setter
    def loc(self, val):
        chld = self.master.winfo_children()
        bar1 = chld[val]
        bar2 = chld[self._loc]
        bar1.grid_configure(column=self._loc)
        bar2.grid_configure(column=val)
        self._loc = val

    def mark_sorting(self):
        self.config(bg="#005050")

    def mark_sorted(self):
        self.config(bg="#005000")

    def mark_normal(self):
        self.config(bg="#222222")

    def mark_before(self):
        self.config(bg="#220000")

    def mark_after(self):
        self.config(bg="#000022")


class Board(Tk):
    def __init__(self):
        super().__init__()
        self.state = STATE_RANDOMIZED
        self.delay_var = IntVar()
        but_frame = Frame(self, bg="#111111")
        but_frame.pack(side=TOP, fill=X)
        Button(but_frame, text="    Bubble     ", command=self.bubble_sort, bg="#111111", fg="white", relief=FLAT).pack(side=LEFT, fill=X)
        Button(but_frame, text="   Insertion   ", command=self.insertion_sort, bg="#111111", fg="white", relief=FLAT).pack(side=LEFT, fill=X)
        Button(but_frame, text="     Merge     ", command=self.merge_sort, bg="#111111", fg="white", relief=FLAT).pack(side=LEFT, fill=X)
        Button(but_frame, text="     Quick     ", command=self.qs, bg="#111111", fg="white", relief=FLAT).pack(side=LEFT, fill=X)
        Button(but_frame, text="   Randomize   ", command=self.randomize, bg="#111111", fg="white", relief=FLAT).pack(side=LEFT, fill=X)
        Button(but_frame, text="   Stop   ", command=self.stop_sorting, bg="#111111", fg="white", relief=FLAT).pack(side=LEFT, fill=X)
        Label(but_frame, text="            Delay (sec): ", bg="#111111", fg="white", relief=FLAT).pack(side=LEFT, fill=BOTH)
        Entry(but_frame, textvariable=self.delay_var, bg="#111111", fg="white", relief=RIDGE).pack(side=LEFT, fill=BOTH)
        self.frame = Frame(self, background="#111111")
        self.frame2 = Frame(self, background="#111111")
        self.frame.pack(fill=BOTH, expand=1)
        self.frame2.pack(fill=BOTH, expand=1)

        self.bars: list[Bar] = []
        ranged = list(range(1, BARS + 1))
        random.shuffle(ranged)
        heights = list(enumerate(ranged))
        for loc, height in heights:
            self.bars.append(Bar(self.frame, self.bars, height, loc))

    def stop_sorting(self):
        self.state = STATE_RANDOMIZED

    def randomize(self):
        if is_sorting(self.state):
            self.stop_sorting()
            self.update()
            self.after(1000)

        for item in self.frame.winfo_children(): item.destroy()
        ranged = list(range(1, BARS + 1))
        random.shuffle(ranged)
        heights = list(enumerate(ranged))
        self.bars = []
        for loc, height in heights: self.bars.append(Bar(self.frame, self.bars, height, loc))

    def swap_two(self, i1: int, i2: int, swp_lst: bool = True):
        self.bars[i1].grid_configure(column=i2)
        self.bars[i2].grid_configure(column=i1)
        if swp_lst: self.bars[i1], self.bars[i2] = self.bars[i2], self.bars[i1]

    def bubble_sort(self):
        if is_sorting(self.state): return
        elif self.state == STATE_SORTED:
            self.randomize()
            self.update()
            self.after(1000)

        self.state = STATE_SORTING_B
        working_ind = 0
        working_bar = self.bars[working_ind]
        sorted_upto = len(self.bars)
        working_bar.mark_sorting()
        while (sorted_upto > 0) and (self.state == STATE_SORTING_B):
            for comp_ind in range(sorted_upto):
                comp_bar = self.bars[comp_ind]
                if comp_bar.H < working_bar.H:
                    self.swap_two(working_ind, comp_ind)
                else:
                    working_bar.mark_normal()
                    working_bar = comp_bar
                    working_bar.mark_sorting()
                working_ind = comp_ind
                self.update()
                self.after(int(self.delay_var.get() * 1000))
            working_bar.mark_sorted()
            working_ind = 0
            working_bar = self.bars[working_ind]
            working_bar.mark_sorting()
            sorted_upto -= 1
        working_bar.mark_sorted()
        self.state = STATE_SORTED

    def insertion_sort(self):
        if is_sorting(self.state): return
        elif self.state == STATE_SORTED:
            self.randomize()
            self.update()
            self.after(1000)

        self.state = STATE_SORTING_I
        working_ind = 1
        working_bar = self.bars[working_ind]
        working_bar.mark_sorting()
        while (working_ind < len(self.bars)) and self.state == STATE_SORTING_I:
            for comp_ind in range(working_ind - 1, -1, -1):
                comp_bar = self.bars[comp_ind]
                if working_bar.H < comp_bar.H:
                    self.swap_two(working_ind, comp_ind)
                    working_ind = comp_ind
                else:
                    break
                self.update()
                self.after(int(self.delay_var.get() * 1000))

            working_bar.mark_sorted()
            working_ind += 1
            try:
                working_bar = self.bars[working_ind]
            except IndexError:
                break
            working_bar.mark_sorting()
        self.state = STATE_SORTED

    def merge(self, ar1, ar2):
        new = []
        try:
            while self.state == STATE_SORTING_M:
                if ar1[0] < ar2[0]:
                    new.append(ar1.pop(0))
                else:
                    new.append(ar2.pop(0))
        except IndexError:
            pass
        new.extend(ar1 + ar2)
        return new

    def merge_sort(self):
        if is_sorting(self.state): return
        elif self.state == STATE_SORTED:
            self.randomize()
            self.update()
            self.after(1000)

        self.state = STATE_SORTING_M
        i = 0
        arr = [[i] for i in self.bars]
        try:
            while self.state == STATE_SORTING_M:
                if len(arr[i]) == len(arr[i + 1]):
                    p1, p2 = arr.pop(0), arr.pop(0)
                    mrged = self.merge(p1, p2)
                    arr.insert(0, mrged)
                    i -= 1
                else:
                    i += 1
        except IndexError:
            pass

        self.bars = self.merge(arr.pop(0), arr.pop(0))
        for cnt, bar in enumerate(self.bars):
            bar.grid_configure(column=cnt)
        self.state = STATE_SORTED

    def quick_sort(self, start, end):
        before_pivot = []
        after_pivot = []
        pivot = random.choice(self.bars[start:end])
        pivot.mark_sorting()
        self.update()
        self.after(int(self.delay_var.get() * 1000))
        for itm in self.bars[start:end]:
            if itm < pivot:
                before_pivot.append(itm)
                itm.mark_before()
            if itm > pivot:
                after_pivot.append(itm)
                itm.mark_after()
        self.bars[start:end] = [*before_pivot, pivot, *after_pivot]
        p1 = start + len(before_pivot)
        pivot.grid_configure(column=p1)
        for ind, item in enumerate(before_pivot): item.grid_configure(column=ind + start)
        for ind, item in enumerate(after_pivot): item.grid_configure(column=ind + 1 + p1)
        pivot.mark_sorted()
        if before_pivot: self.quick_sort(start, p1)
        if after_pivot: self.quick_sort(p1 + 1, end)

    def qs(self):
        if is_sorting(self.state): return
        elif self.state == STATE_SORTED:
            self.randomize()
            self.update()
            self.after(1000)
        self.state = STATE_SORTING_Q
        self.bars = self.quick_sort(0, len(self.bars))
        self.state = STATE_SORTED


bord = Board()
bord.mainloop()
