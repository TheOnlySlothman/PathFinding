from pathlib import Path


class Images:
    def __init__(self):
        self.options = ["tiny", "braid200", "normal", "small", "combo400"]
        self.default = "braid200"

    def __getitem__(self, item):
        if item == "tiny":
            return Path('./Images/tiny.png')
        elif item == "braid200":
            return Path("./Images/braid200.png")
        elif item == "normal":
            return Path("./Images/normal.png")
        elif item == "small":
            return Path("./Images/small.png")
        elif item == "combo400":
            return Path("./Images/combo400.png")
