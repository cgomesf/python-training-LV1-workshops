# Create class architecture

tim = AdminUser("tim")
sheila = AdminUser("sheila")
karen = CustomerUser("karen", 100)
julio = CustomerUser("julio", 25)
vince = ModeratorUser("vince", {"flowers", "general"})
kim = ModeratorUser("vince", {"general", "FAQ"})

product1 = Product(40)

users = [tim, sheila, karen, julio, vince, kim]

for user in users:
    print(str(user) + " - " + user.can_buy(product1))

assert str(sheila) == "#2 sheila"
assert str(kim) == "#6 kim"
