from solarcell.solarcell_model import DiodeExperiment
import click
import csv
import matplotlib.pyplot as plt
import numpy as np 

@click.group()
def cmd_group():
    pass

# @cmd_group.command(help= "gives list of all available ports for connected arduino device")
# def list():
#     """function that returns back the available ports to the arduino device from the model

# @cmd_group.command()
def plot():
    measurements = DiodeExperiment(port = "ASRL5::INSTR")
    U_solarcell_list_mean, I_solarcell_list_mean, error_I_solarcell_list, error_U_solarcell_list, R_var_list_mean, error_R_var_list, P_solarcell_list_mean, error_P_solarcell_list,fill_factor = measurements.scan(start = 1.56, stop = 1.71, number = 5)
    plt.errorbar(U_solarcell_list_mean,I_solarcell_list_mean, xerr =error_U_solarcell_list, yerr = error_I_solarcell_list, fmt = '.' )
    plt.title("Solarcell graph voltage (V) against current (I)")
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (I)")
    plt.show()
    plt.errorbar(R_var_list_mean,P_solarcell_list_mean, xerr = error_R_var_list,yerr =error_P_solarcell_list, fmt = '.' )
    plt.xlabel("Variable resistancte (Ohm)")
    plt.ylabel("Power solarcell (W)")
    plt.show()
    print(f"{fill_factor=}")
plot()