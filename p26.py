class emp:
    company ="itc"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.slary} ")
    
class programmer(emp):
    company = "itc infotech."
    # def show(self):   
        # print(f"the nameis {self.name} and the slary is {self.salary}")

    def showlanguage(self):
        print(f"the name is {self.name} and he is good with {self.language} language")     

a = emp()
b = programmer()

print(a.company,b.company)