class emp:
    name = "vishesh"
    language = "python "
    salary = 1200000

    def __init__(self):
        print("I am creating an object")

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("good morning")


vish = emp()
vish.name = "vishesh"
print(vish.name,vish.salary)

rohan = emp()
