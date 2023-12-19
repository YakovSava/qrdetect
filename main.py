from argparse import ArgumentParser

arg = ArgumentParser()
arg.add_argument('-opt', 'optimize', default=None)
args = arg.parse_args()

if args.optimize is not None:
    from optimize import read, write
else:
    from plugs import read, write
from plugs import Decoder, Config,\
    AppCreate, AppScan, QRCodeGenerator, MoySklad

config_getter = Config(config_filename='conf.ini')
