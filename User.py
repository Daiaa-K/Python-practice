class Privileges:
    def __init__(self,level):
        self.level = level
        if self.level.lower() == "admin":
            self.privileges_granted = ["can post","can update","can delete","can ban user"]
        elif self.level.lower() == "user":
            self.privileges_granted =["can post","can update"]
class User:
    def __init__(self, f_name, l_name, id, branch):
        self.f_name = f_name
        self.l_name = l_name
        self.id = id
        self.branch = branch
        self.login_attempts = 0
        self.privileges = Privileges("user")

    def describe_user(self):
        print(f"Full name: {self.f_name.title()} {self.l_name.title()}\nid: {self.id}\nbranch: {self.branch}")

    def greet_user(self):
        print(f"Hello, {self.f_name.title()} {self.l_name.title()} welcome to our company")

    def increment_attempts(self):
        self.login_attempts += 1

    def reset_attempts(self):
        self.login_attempts = 0

    def show_privileges(self):
        print("Privileges available for current user:")
        for privilege in self.privileges.privileges_granted:
            print(f"\t{privilege}")


class manager(User):
    def __init__(self, f_name, l_name, id, branch):
        super().__init__(f_name,l_name,id,branch)
        self.privileges = Privileges("admin")

        def show_privileges(self):
            print("Privileges available for current user:")
            for privilege in self.privileges.privileges_granted:
                print(f"\t{privilege}")


if __name__ == '__main__':
    hany = User("hany", "ahmed", 42, "main")
    hany.describe_user()
    hany.greet_user()

    for i in range(1, 5):
        hany.increment_attempts()
    print(hany.login_attempts)
    hany.reset_attempts()
    print(hany.login_attempts)
    hany.show_privileges()

    daiaa = manager("daiaa","sayed",3,"main")
    daiaa.show_privileges()