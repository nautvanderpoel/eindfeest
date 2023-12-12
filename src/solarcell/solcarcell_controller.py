# try:
#     from nsp2visasim import sim_pyvisa as pyvisa
# except ModuleNotFoundError:
#     import pyvisa
import pyvisa

class ArduinoVISADevice:
    """class for the arduino controller to open ports and make measurements on channels
    """
    def __init__(self, port):
        """method to open the port of the arduino device

        Args:
            port (string): inputting the used port for the arduino device
        """
        rm = pyvisa.ResourceManager("@py")
        self.device = rm.open_resource(port, read_termination="\r\n", write_termination="\n")

    def get_identification(self):
        """method to give back the identifcationstring of the arduino device

        Returns:
            (string): gives back the identificationstring of the arduino device
        """
        return self.device.query("*IDN?")
    
    def set_output_value(self, value):
        """method to set the bit-value-amount on channel 0 on the device

        Args:
            value (integer): the bitvalue set by user
        """
        self.bits_CH0 = int(self.device.query(f"OUT:CH0 {value}"))
    
    def get_output_value(self):
        """method to give back the bitsvalue on channel 0 on the device

        Returns:
            (integer): the bitvalue on channel 0
        """
        return self.bits_CH0

    def get_input_value(self, channel):
        """method to measure the amount of bits on a certain channel

        Args:
            channel (integer): user choosing the channel with the corresponding channel-number

        Returns:
            channel_bit (integer): measurement of the bitsvalue on the channel chosen by user
        """
        channel_bit = int(self.device.query(f"MEAS:CH{channel}?"))
        return channel_bit

    def get_input_voltage(self, channel):
        """method to measure the amount of voltage on a certain channel by calculating with the bitsvalue

        Args:
            channel (integer): user choosing the channel with the corresponding channel-number

        Returns:
            voltage (float): gives back the voltage over the channel chosen by user
        """
        channel_bits = int(self.device.query(f"MEAS:CH{channel}?"))
        U_channel = (3.3 / 1023) * channel_bits
        return U_channel

    def close_device(self):
        """method that allows the device to close

        Returns:
            function: closes device
        """
        return self.device.close()

def list_devices():
    """method to find list of ports available to the arduino

    Returns:
        list: gives back available ports of the arduino
    """
    rm = pyvisa.ResourceManager("@py")
    ports = rm.list_resources()
    return ports