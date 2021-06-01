class Base:
    def __init__(self):
        print("Baseee")

class Child(Base):
    def __init__(self):
        super().__init__()
        print("Child")

gag = Child()
print(isinstance(gag, Base))
        