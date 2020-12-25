def demo():
    print("{}{}".format("th", "Thailand"))
    print("{:5}|{:15}|".format("th", "Thailand"))  # align left
    print("{:>5}|{:>15}|".format("th", "Thailand"))  # align right
    print("{:*>5}|{:->15}|".format("th", "Thailand"))  # align right
    print("{:^5}|{:^15}|".format("th", "Thailand"))  # align center


def demo_dict():
    menu = {"name": "mocha", "price": 165, "size": "m"}
    print(menu["name"])
    print("menu name = {} price = {}".format(menu["name"], menu["price"]))
    print("menu name = {name}({size}) price = {price}".format(**menu))


def multi_table(n):
    for i in range(1, 13):
        print("{} x {:2} = {:3}".format(n, i, n*i))


def ascii_table():
    for i in range(65, 128):
        print("{0:3} {0:#b} {0:04o} {0:#x} {0:#X} {0:c}".format(i))


# demo()
# demo_dict()
# multi_table(12)
ascii_table()
