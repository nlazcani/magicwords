from .abracadabra import Abracadabra

def load_ipython_extension(ipython):
    ipython.register_magics(Abracadabra)