from solarcell.solarcell_model import DiodeExperiment
import click
import csv
import matplotlib.pyplot as plt

@click.group()
def cmd_group():
    pass

# @cmd_group.command(help= "gives list of all available ports for connected arduino device")
# def list():
#     """function that returns back the available ports to the arduino device from the model

# @cmd_group.command()
def plot():
    """shows a plot of the solarcell with the voltage (v) against current (a)
    """
    measurements = DiodeExperiment(port = "ASRL5::INSTR")
    U_solarcell_list_mean, I_solarcell_list_mean, error_I_solarcell_list, error_U_solarcell_list = measurements.scan(start = 485, stop = 530, number = 5)
    plt.errorbar(U_solarcell_list_mean,I_solarcell_list_mean, xerr =error_U_solarcell_list, yerr = error_I_solarcell_list, fmt = '.' )
    plt.title("Solarcell graph voltage (V) against current (I)")
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (I)")
    plt.show()

plot()