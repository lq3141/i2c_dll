import ctypes
import time
dll=ctypes.cdll.LoadLibrary("../x64/Release/i2c_dll.dll")
print(dll)
dll.printtest()
#dll.set_arr()

dll.i2c_init()
### 
##  + In py3, user encode to convert string to bytestring
##  
##  + https://stackoverflow.com/questions/50515790/sending-strings-between-c-libraries-and-python
##   
print("")

##b0.sysif.sys_acc_password.value = 0x72
##b0.sysif.lane_acc_password.value = 0x52
##b0.sysif.mcu_ctrl_password.value = 0x87
a=dll.i2c_write(0x60, 0x00, 0x10,0x72)
a=dll.i2c_write(0x60, 0x00, 0x11,0x52)
a=dll.i2c_write(0x60, 0x00, 0x12,0x87)
print("--- plain test ---")
##time.sleep(10)
#b=dll.i2c_read(0x60, 0x00, 0x14)
#print("    plain read 0x14: 0x{0:x}".format(b))
a=dll.i2c_write(0x60, 0x00, 0x14,0xAA)
#a=dll.i2c_write(0x60, 0x00, 0x15,0xAB)
#a=dll.i2c_write(0x60, 0x00, 0x16,0xAC)
#a=dll.i2c_write(0x60, 0x00, 0x17,0xAD)
a=dll.i2c_read(0x60, 0x00, 0x14)
print("    plain read: 0x{0:x}".format(a))
#a=dll.i2c_read(0x60, 0x0C, 0x10)
#print("    plain read: 0x{0:x}".format(a))
#a=dll.i2c_write(0x60, 0x0C, 0x10,0xBB)
#a=dll.i2c_read(0x60, 0x0C, 0x10)
#print("    plain read: 0x{0:x}".format(a))
#a=dll.i2c_read(0x60, 0x00, 0x16)
#print("    plain read: {0:x}".format(a))
#a=dll.i2c_read(0x60, 0x00, 0x17)
#print("    plain read: {0:x}".format(a))


##
##if True:
##    print("")
##    print("--- md test ---")
##    print("IMPORTANT NOTE: must make sure using SAB0_E7/SAB0_E8 board")
##    a=dll.md_i2c_write("SAB0_E7".encode('utf-8'),0x60, 0x00, 0x14,0xF0)
##    a=dll.md_i2c_read("SAB0_E7".encode('utf-8'), 0x60, 0x00, 0x14)
##    print("    E7 read: {0:x}".format(a));
##    a=dll.md_i2c_write("SAB0_E8".encode('utf-8'),0x60, 0x00, 0x14,0x55)
##    a=dll.md_i2c_read("SAB0_E8".encode('utf-8'), 0x60, 0x00, 0x14)
##    print("    E8 read: {0:x}".format(a));
#
