class emp:
    company ="itc"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.slary} ")
    
class coder:
    lang = "python"
    def printlang(self):
        print(f"here is your language: {self.lang}")

class programmer(emp, coder):
    company = "itc infotech."
    # def show(self):   
        # print(f"the nameis {self.name} and the slary is {self.salary}")

    def showlanguage(self):
        print(f"the name is {self.name} and he is good with {self.language} language")     

a = emp()
b = programmer()

print(a.company,b.company)
b.printlang()