import uniconf

config = uniconf.Config()
config.struct()

num = 123
config.set("data", "number", num)
config.struct()

print(config.get("data", "number"))
print(config("data", "number"))
print((type(config("data", "number"))))

num_list = [1, 2, 3, 4, 5]
config.set("data", "num_list", num_list)
print(config("data", "num_list"))
print((type(config("data", "num_list"))))

config.struct()
