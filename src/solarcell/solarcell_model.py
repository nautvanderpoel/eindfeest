from solarcell.solcarcell_controller import ArduinoVISADevice
import numpy as np 
import math

class DiodeExperiment:
    """This class extracts data from the device.
    """
    def __init__(self,port):
        """Here are all the used lists defined.
        """
        
        self.U_solarcell_list = []
        self.U_resistor_list = []

        self.U_solarcell_list_mean = []
        self.I_solarcell_list_mean = []

        self.I_solarcell_list = []

        self.error_U_solarcell_list = []
        self.error_I_solarcell_list = []

        self.device = ArduinoVISADevice(port = port)
    
    def scan(self,start,stop, number):
        # for n in range(number):
            for i in range(start,stop):
                
                for w in range(number):
                    self.device.set_output_value(i)
                    self.ch2 = self.device.get_input_voltage(channel = 2)
                    self.ch1 = self.device.get_input_voltage(channel = 1)

                    self.U_solarcell_list.append(3*self.ch1) #dit naar ch1?
                    self.U_resistor_list.append(self.ch2) #dit naar ch2?

                    # calculates the current using ohm's law    
                    for l in range(len(self.U_resistor_list)):
                        self.I_solarcell = self.U_resistor_list[l]/4.7
                        self.I_solarcell_list.append(self.I_solarcell)



                    self.U_solarcell_list_mean.append(np.mean(self.U_solarcell_list))
                    self.I_solarcell_list_mean.append(np.mean(self.I_solarcell_list))

                    # calculates the deviation of the central values
                    self.error_U_solarcell_list.append(np.std(self.U_solarcell_list)/(len(self.U_solarcell_list)**0.5))
                    self.error_I_solarcell_list.append(np.std(self.I_solarcell_list)/(len(self.I_solarcell_list)**0.5))

            
                    self.U_solarcell_list.clear()
                    self.U_resistor_list.clear()
                    self.I_solarcell_list.clear()
                


            return self.U_solarcell_list_mean, self.I_solarcell_list_mean, self.error_I_solarcell_list, self.error_U_solarcell_list

    def convert_voltage_adc(self, voltage):
        """Converts voltage to adc.

        Args:
            voltage (float): voltage

        Returns:
            adc (int): adc
        """
        self.adc = np.floor((1023/3.3)*voltage)
        return self.adc 

    def close_device(self):
        """Closes device from controller

        Returns:
            function: close function function from controller
        """
        return self.device.close_device()