# Create class architecture

class Product:
    def __init__(self, price):
        self.price = price


class AdminUser:
    user_id = 1

    def __init__(self, user_name):
        self.user_name = user_name
        self.balance = None
        self.user_id = AdminUser.user_id
        AdminUser.user_id += 1

    def can_buy(self, product):
        if self.balance is not None and product.price < self.balance:
            return "CAN buy"
        else:
            return "can't buy"

    def __str__(self):
        return f"#{self.get_id_value()} {self.get_name_value()}"

    def get_id_value(self):
        return self.user_id

    def get_name_value(self):
        return self.user_name


class CustomerUser(AdminUser):
    def __init__(self, user_name, user_balance):
        super().__init__(user_name)
        self.balance = user_balance


class ModeratorUser(AdminUser):
    def __init__(self, user_name: str, user_arguments: set):
        super().__init__(user_name)
        self.topics = user_arguments


def main():
    tim = AdminUser("tim")
    sheila = AdminUser("sheila")
    karen = CustomerUser("karen", 100) # first arg is name, second is balance
    julio = CustomerUser("julio", 25)
    vince = ModeratorUser("vince", {"flowers", "general"})
    kim = ModeratorUser("kim", {"general", "FAQ"})

    product1 = Product(40)  # first arg is price

    users = [tim, sheila, karen, julio, vince, kim]

    for user in users:
        print(str(user) + " - " + user.can_buy(product1))

    assert str(sheila) == "#2 sheila" # format is #{id} {name}
    assert str(kim) == "#6 kim"


if __name__ == "__main__":
    main()
