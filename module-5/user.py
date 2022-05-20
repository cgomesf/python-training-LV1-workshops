# Create class architecture

class user:
    total_user = 0
    def __init__(self, name):
        self.name = name
        user.total_user += 1
        self.balance = 0
        self.user_id = user.total_user
    def __str__(self):
        return f"#{self.user_id} {self.name}"

    def can_buy(self, product):
        if self.balance:
            if self.balance > product.get_priced():
                return product.__str__()
            else:
                return "NO"
        else:
            return "NO"

class CustomerUser(user):
    def __init__(self, name, wallet):
        super().__init__(name)
        self.balance = wallet


class ModeratorUser(user):
    def __init__(self, name,tab_info):
        super().__init__(name)
        self.tab = tab_info


class AdminUser(user):
    def __init__(self, name):
        super().__init__(name)

class Product:
    def __init__(self, price):
        self.price = price

    def get_priced(self):
        return self.price

def main():
    tim = AdminUser("tim")
    sheila = AdminUser("sheila")
    karen = CustomerUser("karen", 100)
    julio = CustomerUser("julio", 25)
    vince = ModeratorUser("vince", {"flowers", "general"})
    kim = ModeratorUser("kim", {"general", "FAQ"})

    product1 = Product(40)

    users = [tim, sheila, karen, julio, vince, kim]

    for user in users:
        print(str(user) + " - " + user.can_buy(product1))

    assert str(sheila) == "#2 sheila"
    assert str(kim) == "#6 kim"

if __name__ == "__main__":
    main()