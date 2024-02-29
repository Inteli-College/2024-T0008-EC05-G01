import sys
import glob
import serial
from serial.tools import list_ports

def serial_ports():
    """
        Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """

    #? Windows
    if sys.platform.startswith('win'): ports = [port.device for port in list_ports.comports()]

    #? Linux
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # Exclude terminal device (/dev/tty)
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'): ports = glob.glob('/dev/tty.*')
    else: raise EnvironmentError('Unsupported platform')

    if not sys.platform.startswith('win'):
        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
    else: result = ports
    
    print(result)
    return result