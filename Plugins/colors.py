

class Palette:
    

    def __init__(self) -> None:
        # try: __import__("colorama").init()
        # except ModuleNotFoundError:
        #     print("Warning colorama is not installed")

        self.colors = [
    '\x1b[1;97m',
    '\x1b[1;91m',
    '\x1b[1;92m',
    '\x1b[1;93m',
    '\x1b[1;94m',
    '\x1b[1;95m',
    '\x1b[1;96m',
    '\x1b[0m',
    '\x1b[1;30m',
    '\x1b[41m\x1b[1;97m',
    '\x1b[m',
    '\x1b[93m',
    '\x1b[32m',
    '\x1b[95m',
    '\x1b[33m',
    '\x1b[1;96m',
    '\x1b[0;34m',
    '\x1b[1;97m',
    '\x1b[30m',
    '\x1b[31m',
    '\x1b[32m',
    '\x1b[33m',
    '\x1b[34m',
    '\x1b[35m',
    '\x1b[36m',
    '\x1b[37m',
    '\x1b[91m',
    '\x1b[92m',
    '\x1b[93m',
    '\x1b[95m',
    '\x1b[38;5;204m',
    '\x1b[38;5;220m',
    '\x1b[38;5;193m',
    '\x1b[38;5;216m',
    '\x1b[38;5;190m',
    '\x1b[38;5;231m',
    '\x1b[38;5;208m',
    '\x1b[38;5;106m',
    ]
        

    @property
    def error(self):
        return self.colors[9]
    

    @property
    def sky_blue(self):
        return self.colors[6]
    

    @property
    def red(self):
        return self.colors[1]
    

    @property
    def magenta(self):
        return self.colors[13]
    
    @property
    def sexy_blue(self):
        return self.colors[4]

    @property
    def grassy_green(self):
        return self.colors[12]

    @property
    def sunny_yellow(self):
        return self.colors[11]

    @property
    def fucked_up_blue(self):
        return self.colors[24]

    @property
    def better_grassy_green(self):
        return self.colors[27]
    
    @property
    def mustard(self):
        return self.colors[21]
    
    @property
    def grey(self):
        return self.colors[8]
    
    @property
    def better_purpule(self):
        return self.colors[23]

    @property
    def fuck(self):
        return "\033[0m"

    def print_all(self):
        for i in range(len(self.colors)):
            print(f"{self.colors[i]} Hello world {i}\033[0m")


my_palette = Palette()