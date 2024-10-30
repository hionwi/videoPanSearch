import ctypes

my_lib = ctypes.CDLL('./my_lib.dll')
my_lib.genera_keys.argtypes = [
    ctypes.POINTER(ctypes.c_ubyte),
    ctypes.POINTER(ctypes.c_ubyte),
    ctypes.POINTER(ctypes.c_ubyte),
]

my_lib.sign.argtypes = [
    ctypes.POINTER(ctypes.c_ubyte),
    ctypes.POINTER(ctypes.c_ubyte),
    ctypes.POINTER(ctypes.c_ubyte),
    ctypes.POINTER(ctypes.c_ubyte),
    ctypes.POINTER(ctypes.c_ubyte),
]

my_lib.verify.argtypes = [
    ctypes.POINTER(ctypes.c_ubyte),
    ctypes.POINTER(ctypes.c_ubyte),
    ctypes.POINTER(ctypes.c_ubyte),
    ctypes.POINTER(ctypes.c_ubyte),

]

my_lib.init()


def clean():
    my_lib.clean()


def generate_keys(id):
    pk = (ctypes.c_ubyte * 65)()
    sk = (ctypes.c_ubyte * 32)()
    id_b = (ctypes.c_ubyte * len(id))(*id)  # Convert to ctypes array
    my_lib.genera_keys(id_b, pk, sk)
    return pk, sk


def sign(id, pk, sk, message):
    pk_b = (ctypes.c_ubyte * 65)(*pk)
    sk_b = (ctypes.c_ubyte * 32)(*sk)
    id_b = (ctypes.c_ubyte * len(id))(*id)  # Convert to ctypes array
    message_b = (ctypes.c_ubyte * len(message))(*message)  # Convert to ctypes array
    sig = (ctypes.c_ubyte * 64)()
    my_lib.sign(id_b, message_b, pk_b, sk_b, sig)
    return sig


def very(id, pk, message, sig):
    id_b = (ctypes.c_ubyte * len(id))(*id)  # Convert to ctypes array
    pk_b = (ctypes.c_ubyte * 65)(*pk)

    sig_b = (ctypes.c_ubyte * 64)(*sig)
    message_b = (ctypes.c_ubyte * len(message))(*message)  # Convert to ctypes array
    return my_lib.verify(id_b, message_b, pk_b, sig_b)
