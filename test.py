from uniconf import uniconf
import datetime

date_format = '%Y-%m-%d %H:%M:%S.%f'
if __name__ == '__main__':
    print("main.py")

    config = uniconf.Config()
    # config.set("info_4", "number", "125721", "int")
    a_bool = True
    config.struct()

