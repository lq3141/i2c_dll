import ctypes
dll=ctypes.windll.LoadLibrary("./i2c_dll.dll")
#dll.printtest()
#dll.set_arr()
#dll.printtest()

dll.i2c_init()
a=dll.i2c_read(0x61, 0x8F, 0xFF)

print("read: {0:x}".format(a));

a=dll.i2c_write(0x61, 0x8F, 0xFF,0xFF)
a=dll.i2c_read(0x61, 0x8F, 0xFF)
print("read: {0:x}".format(a));
a=dll.i2c_write(0x61, 0x8F, 0xFF,0x12)
a=dll.i2c_read(0x61, 0x8F, 0xFF)
print("read: {0:x}".format(a));
