import hashlib
import subprocess
import os
import platform

def calculate_hash(filename):
    sha256_hash = hashlib.sha256()
    with open(filename, 'rb') as f:
        for byte_block in iter(lambda: f.read(4096), b''):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def flatten(inlist):
    outlist = []
    if isinstance(inlist, (list, tuple)):
        for item in inlist:
            outlist+=flatten(item)
    else:
        outlist+=[inlist]
    return outlist

def open_prog(filepath):
    if platform.system() == 'Darwin':
        subprocess.call(('open', filepath))
    elif platform.system() == 'Windows':
        os.startfile(filepath)
    else:
        subprocess.call(('xdg-open', filepath))