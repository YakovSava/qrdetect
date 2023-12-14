from argparse import ArgumentParser

arg = ArgumentParser()
arg.add_argument('-opt', 'optimize', default=None)
args = arg.parse_args()

if args.optimize is not None:
    from optimize import read, write, Connector
else:
    from plugs import read, write, Connector
from plugs import Cache, Decoder, Config,\
    AppCreate, AppScan, QRCodeGenerator
