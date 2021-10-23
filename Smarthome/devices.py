import os

funkcodes =  {"AON" : 5506385,
              "AOff" : 5506388,
              "BON" : 5509457,
              "BOff" : 5509460 }
              
"""
A on : 5506385
A Off: 5506388
B on : 5509457
B off: 5509460
"""

def SwitchDev(command):
    if command in funkcodes:
        code = funkcodes[command]
        print(code)
        cmd = "sudo /home/pi/433Utils/RPi_utils/codesend " + str(code)
        print(cmd)
        os.system(cmd)
    else:
        print("DEVICES; Switchdev: No command found")
