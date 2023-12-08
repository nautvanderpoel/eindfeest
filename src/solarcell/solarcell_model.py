from solarcell.solarcell_view import ArduinoVISADevice
import numpy as np 

class DiodeExperiment:
    """This class extracts data from the device.
    """
    def __init__(self,port):
        """Here are all the used lists defined.
        """
        # mean values of voltages and currents
        
        self.U_solarcell_list = []
        self.U_resistor_list = []

        self.I_solarcell_list = []

        self.error_U_solarcell_list = []
        self.error_I_solarcell_list = []

        self.device = ArduinoVISADevice(port = port)
    
    def scan_(self,start,stop):
        for i in range(start,stop):
            
            self.set_output_value(i)
            self.ch2 = self.device.get_input_value_voltage(2)
            self.ch1 = self.device.get_input_value_voltage(1)

            self.U_solar_cell_list.append(3*self.ch2)
            self.U_resistor_list.append(self.ch1)

             # calculates the current using ohm's law    
        for l in range(len(self.U_resistor_list)):
            self.I_solarcell_list = self.U_resistor_list[l]/220
            self.I_solarcell.append(self.I_LED)
            
        
        return self.U_solarcell_list, self.I_solarcell_list

    def convert_voltage_adc(self, voltage):
        """Converts voltage to adc.

        Args:
            voltage (float): voltage

        Returns:
            adc (int): adc
        """
        self.adc = math.floor((1023/3.3)*voltage)
        return self.adc 

    def close_device(self):
        """Closes device from controller

        Returns:
            function: close function function from controller
        """
        return self.device.close_device1()

