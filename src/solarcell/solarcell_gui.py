import sys
import pyqtgraph as pg
import numpy as np
import csv
from solarcell.designer import Ui_MainWindow
from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from solarcell.solarcell_model import DiodeExperiment, find_ports

# PyQtGraph global options
pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")

class UserInterface(QtWidgets.QMainWindow):
    """ class to create a graphical user interface showing a graph of an arduino device with the voltage and current over the LED, with the help of designer
    """
    def __init__(self):
        """ init method that shows the graphical user interface with a combobox for choosing port, buttons to start and save measurement and spinboxes for voltagevalues and measurement repeats
        """
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.ports_combo.addItems(find_ports())
        self.ui.start_button.clicked.connect(self.plot)
        self.ui.save_button.clicked.connect(self.save_data)

        self.show()

    @Slot()
    def plot(self):
        """method that makes use of the model, in which a plot is made of the current and voltage with errors over LED when the user chooses a start- and endvoltage and amount of repeats in the spinbox
        """
        try:
            self.ui.plot_widget.clear()

            self.measurements = DiodeExperiment(port= self.ui.ports_combo.currentText())

            #self.LED_U_list, self.LED_I_list = self.measurements.scan_voltage(start = self.ui.voltage_start.value(), end = self.ui.voltage_end.value())
            self.U_solarcell_list_mean, self.I_solarcell_list_mean, self.error_U_solarcell_list, self.error_I_solarcell_list = self.measurements.repeat_voltage(start = self.ui.voltage_start.value(), stop = self.ui.voltage_end.value(), number = self.ui.repeats.value())

            self.ui.plot_widget.plot(self.U_solarcell_list_mean, self.I_solarcell_list_mean, symbol="o", symbolSize=5, pen=None)
            error_bars = pg.ErrorBarItem(x=self.U_solarcell_list_mean, y=self.I_solarcell_list_mean, width=2 * np.array(self.error_U_solarcell_list), height=2 * np.array(self.error_I_solarcell_list))
            self.ui.plot_widget.setLabel("left", "Current I in amps")
            self.ui.plot_widget.setLabel("bottom", "Voltage U in volts")
            self.ui.plot_widget.addItem(error_bars)
            self.ui.portlabel.setText("")

        except:
            self.ui.portlabel.setText("ERROR: corresponding port does not make a measurement, choose another port.")

        self.device_close()
    
    @Slot()
    def save_data(self):
        """method that creates a csv with a filename chosen by user, when the save data button is clicked
        """
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(filter="CSV files (*.csv)")
        with open(f'{filename}', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Voltage LED in volts', 'Current LED in amps', 'Error on voltage LED', 'Error on current LED'])
            for e, f, g, h in zip(self.LED_U_list, self.LED_I_list, self.error_U, self.error_I):
                writer.writerow([e, f, g, h])

    @Slot()
    def device_close(self):
        """method that closes the device

        Returns:
            function: the close device function called from model which is also called from controller
        """
        return self.measurements.closing_device()

def main():
    """function that shows the user interface
    """
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()  