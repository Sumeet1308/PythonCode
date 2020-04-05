class Computer:
    def __init__(self,ram,CPU='AMD'):   # This is constructor which allocates memory for an object
        self.ram=ram
        self.CPU=CPU
    def update(self):
        self.CPU='I7'
    def config(self):
        print ("The configuration is ",self.ram," RAM and ",self.CPU," CPU")

c1=Computer("9GB")
c2=Computer("8GB","AMD")
c1.CPU="I3"
c1.config()
c2.config()

c1.update()

