import os

FWname = "NFCY_GNSS_AllInOne.bin"

APP_START_ADDR = 65536  # APP起始地址
BOOT_LOADER_START_ADDR = 0  # BootLoader其起始地址

TotleFlashSize = 512 * 1024  # 总flash大小

# 如果此文件夹中存在旧版固件文件，就删除它
if os.path.exists(FWname):
    os.remove(FWname)
    print("删除旧版固件文件...")
    print("-------------------------------------------------------")

# 创建合并后的文件
FirmwareFile = open(FWname, 'wb')

# 第一步，填充TotleFlashSize个0xFF到文件中
print("生成空文件")
for i in range(TotleFlashSize):
    FirmwareFile.write(0xFF.to_bytes(1, byteorder='big'))

# 第二步，填入APP固件
print("写入APP固件")
AppFile = open(file="../build/NFCY_GNSS/bin/AP_Periph.bin", mode="rb")
AppData = AppFile.read()
FirmwareFile.seek(APP_START_ADDR)
for i in range(len(AppData)):
    FirmwareFile.write(AppData[i].to_bytes(1, byteorder='big'))

# 第三步，填入BootLoader固件
print("写入BootLoader固件")
BootloaderFile = open(file="../build/NFCY_GNSS/bin/AP_Bootloader.bin", mode="rb")
BootLoaderData = BootloaderFile.read()
FirmwareFile.seek(BOOT_LOADER_START_ADDR)
for i in range(len(BootLoaderData)):
    FirmwareFile.write(BootLoaderData[i].to_bytes(1, byteorder='big'))

print("生成完成！")
FirmwareFile.close()
AppFile.close()
BootloaderFile.close()

input()