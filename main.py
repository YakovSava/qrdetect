from plugs import Config, MoySklad, AppCreate

config_getter = Config(config_filename='conf.ini')
mosk = MoySklad()


creater = AppCreate(func=_send)


def run():
    pass


if __name__ == "__main__":
    run()
