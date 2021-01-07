import os
import time

LowAmbTemp = False
HighAmbTemp = False

while True:
    # We could do subprocess.check_output() here but it would get messy, so I will just read a text file.
    ambientTemp = os.system("ipmitool sdr type temperature |grep Ambient |grep degrees |grep -Po '\d{2}' | tail -1 > AmbTemp.txt")
    with open("AmbTemp.txt", "r") as file:
        ambientTempFile = file.read().replace('\n', '')
    if os.stat("AmbTemp.txt").st_size == 0:
        print("File Empty, assuming single digit")
        LowAmbTemp = True
    else:
        ambientTempFile = int(ambientTempFile)
        if ambientTempFile <= 13:
            print("Ambient Temp is Low")
            LowAmbTemp = True
        elif ambientTempFile >= 25:
            print("Ambient Temp is High")
            HighAmbTemp = True
        else:
            print("Ambient Temp is Nominal")

    if HighAmbTemp == True:
        with open("/sys/class/hwmon/hwmon0/temp2_input", "r") as file:
            CPUtemp = file.read().replace('\n', '')
        CPUtemp = int(CPUtemp)
        if CPUtemp <= 45000:
            os.system("ipmitool raw 0x30 0x30 0x02 0xff 0x19")
        elif 45000 <= CPUtemp <= 55000:
            os.system("ipmitool raw 0x30 0x30 0x02 0xff 0x23")
        elif 55000 <= CPUtemp <= 67000:
            os.system("ipmitool raw 0x30 0x30 0x02 0xff 0x27")
        elif 67000 <= CPUtemp:
            os.system("ipmitool raw 0x30 0x30 0x02 0xff 0x64")

    elif LowAmbTemp == True:
        with open("/sys/class/hwmon/hwmon0/temp2_input", "r") as file:
            CPUtemp = file.read().replace('\n', '')
        CPUtemp = int(CPUtemp)
        if CPUtemp <= 45000:
            os.system("ipmitool raw 0x30 0x30 0x02 0xff 0x10")
        elif 45000 <= CPUtemp <= 55000:
            os.system("ipmitool raw 0x30 0x30 0x02 0xff 0x18")
        elif 55000 <= CPUtemp <= 67000:
            os.system("ipmitool raw 0x30 0x30 0x02 0xff 0x27")
        elif 67000 <= CPUtemp:
            os.system("ipmitool raw 0x30 0x30 0x02 0xff 0x64")

    else:
        with open("/sys/class/hwmon/hwmon0/temp2_input", "r") as file:
            CPUtemp = file.read().replace('\n', '')
        CPUtemp = int(CPUtemp)
        if CPUtemp <= 45000:
            os.system("ipmitool raw 0x30 0x30 0x02 0xff 0x15")
        elif 45000 <= CPUtemp <= 55000:
            os.system("ipmitool raw 0x30 0x30 0x02 0xff 0x18")
        elif 55000 <= CPUtemp <= 67000:
            os.system("ipmitool raw 0x30 0x30 0x02 0xff 0x27")
        elif 67000 <= CPUtemp:
            os.system("ipmitool raw 0x30 0x30 0x02 0xff 0x64")

    time.sleep(1)
