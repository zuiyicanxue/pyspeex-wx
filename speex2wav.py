from ctypes import cdll

cur = cdll.LoadLibrary('./declib/libpyspeex.so')
cur.decode(b'./example/a.speex',b'./example/a.wav')
