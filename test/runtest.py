import ctypes
dll=ctypes.cdll.LoadLibrary("../x64/Release/i2c_dll.dll")
print(dll)
#dll.printtest()
#dll.set_arr()

dll.i2c_init()
## 
#  + In py3, user encode to convert string to bytestring
#  
#  + https://stackoverflow.com/questions/50515790/sending-strings-between-c-libraries-and-python
#   

print("")
print("--- plain test ---")
a=dll.i2c_write(0x60, 0x00, 0x15,0xAB)
a=dll.i2c_read(0x60, 0x00, 0x15)
print("    plain read: {0:x}".format(a))

if True:
    print("")
    print("--- md test ---")
    print("IMPORTANT NOTE: must make sure using SAB0_E7/SAB0_E8 board")
    a=dll.md_i2c_write("SAB0_E7".encode('utf-8'),0x60, 0x00, 0x14,0xF0)
    a=dll.md_i2c_read("SAB0_E7".encode('utf-8'), 0x60, 0x00, 0x14)
    print("    E7 read: {0:x}".format(a));
    a=dll.md_i2c_write("SAB0_E8".encode('utf-8'),0x60, 0x00, 0x14,0x55)
    a=dll.md_i2c_read("SAB0_E8".encode('utf-8'), 0x60, 0x00, 0x14)
    print("    E8 read: {0:x}".format(a));

