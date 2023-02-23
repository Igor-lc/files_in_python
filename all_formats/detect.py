# version 1
from sys import argv

with open(argv[1], "rb") as fi:
    f = fi.read(8)

    if "b'\\xff" in str(f):
        print('jpeg')
    if 'PNG'.encode() in f:
        print('png')
    if 'GIF'.encode() in f:
        print('gif')
    if "b'\\xff" not in str(f) and 'PNG'.encode() not in f and 'GIF'.encode() not in f:
        print(None)

# version 2
import sys
filename = sys.argv[1]

with open(filename, "rb") as image_file:
    data = image_file.read(50)

    if data[:6] in (b'GIF87a', b'GIF89a'):
        image_type = 'gif'
    elif data.startswith(b'\x89PNG\r\n\x1a\n'):
        image_type = 'png'
    elif data.startswith(b'\xff\xd8'):
        image_type = 'jpeg'
    else:
        image_type = None

    print(image_type)
