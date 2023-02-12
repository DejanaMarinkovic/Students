class Student:
    def __init__(self, name , adress, phone, course, index_number):
        self.name = name
        self.adress = adress
        self.phone = phone
        self.course = course
        self.index_number = index_number

    def getInfo(self):
        return f"Name and surname: {self.name} \nAdress: {self.adress} \nPhone number: {self.phone} \nChosen course: {self.course} \nIndex number: {self.index_number}"

student1 = Student("Natasha Rostova", "Polyany, Leningrad Oblast, Russia, 188824", "+7 454 686 25 49", "Python", "001/2023")
student2 = Student("Ali Habib ", "Jabal al-Druze, Syria", "+963 2458 14 74", "PHP", "002/2023")
student3= Student("Anna Marcinowska", "Hańcza, Poland", "+48 71 854 22 49", "Python", "003/2023")
student4= Student("James Brown", "Randolph, NE 68771, USA", "+34 965 98 64 64", "JavaScript", "004/2023")

print(student4.getInfo())

