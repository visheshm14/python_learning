class emp:
    name = "vishesh"
    language = "python "
    salary = 1200000

    def getinfo(self):
        print(f"The language is{self.language}. The salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("good morning")


vish = emp()
vish.language = "java"
print(vish.name,vish.language)    
vish.getinfo()
vish.greet()
