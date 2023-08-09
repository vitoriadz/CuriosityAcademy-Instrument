import serial
import random


class Instrument:
    """
    Simulated instrument class that reads and writes messages to a serial port.

    This class simulates an instrument that communicates through a serial port.
    It generates random values for status, type, voltage, temperature, and current.
    It can read messages from the serial port and respond accordingly.

    Attributes:
        status (int): A random status value.
        type (str): A random type value.
        voltage (int): A random voltage value.
        temperature (int): A random temperature value.
        current (int): A random current value.

    Args:
        ser (serial.Serial): An instance of the `serial.Serial` class representing the serial port.
    """
    def __init__(self, ser: serial.Serial):
        """
        Initialize the Instrument with random attribute values and a serial port.

        Args:
            ser (serial.Serial): An instance of the `serial.Serial` class representing the serial port.
        """
        self.status = random.randint(0, 0xFFFFFFFF)
        self.type = random.choice(["a", "b", "c", "abc"])
        self.voltage = random.randint(0, 220)
        self.temperature = random.randint(0, 85)
        self.current = random.randint(0, 2000)
        self.ser = ser

    def read_message(self):
        """
        Read a message from the serial port and respond accordingly.

        This method reads a message from the serial port and processes it based on
        the command. It can respond with the status, type, voltage, temperature, or
        current based on the command received.

        Raises:
            ValueError: If an unknown command is received.
        """
        message = self.ser.readline().decode()
        command = message[:3]

        if command == "STA":
            self.write_response(str(self.status))
        elif command == "TYP":
            self.write_response(self.type)
        elif command == "VOL":
            self.write_response(str(self.voltage))
        elif command == "TMP":
            self.write_response(str(self.temperature))
        elif command == "CUR":
            self.write_response(str(self.current))
        else:
            raise ValueError("Unknown command: " + command)

    def write_response(self, response):
        """
        Write a response to the serial port.

        This method writes a response to the serial port. The response is sent as bytes
        using the UTF-8 encoding.

        Args:
            response (str): The response to be sent.

        Example:
            >>> instrument = Instrument(ser)
            >>> instrument.write_response("Response message")
        """
        self.ser.write(bytearray(response + "\r\n", 'utf-8'))

