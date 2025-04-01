class user:
    def __init__(self, name,  email, password, isOn=False):
        self.name=name
        self.isOn=isOn
        self.email=email
        self.password=password
user1=user("suryansh", "Suryansh.15171@stu.upes.ac.in", "iajd2u4hf", True)
print(user1.name)
print(user1.isOn)
print(user1.email)
print(user1.password)