from solarcell.solarcell_model import DiodeExperiment
import click
import csv
import matplotlib.pyplot as plt
import numpy as np 

@click.group()
def cmd_group():
    pass


def plot():
    """Generates two plots, U-I-graph of the solarcell, P-R-graph (Variable resistance, and power of the solarcell).
    """
    measurements = DiodeExperiment(port = "ASRL5::INSTR")
    U_solarcell_list_mean, I_solarcell_list_mean, error_I_solarcell_list, error_U_solarcell_list, R_var_list_mean, error_R_var_list, P_solarcell_list_mean, error_P_solarcell_list = measurements.scan(start = 1.51, stop = 1.71, number = 3)
    plt.errorbar(U_solarcell_list_mean,I_solarcell_list_mean, xerr =error_U_solarcell_list, yerr = error_I_solarcell_list, fmt = '.' )
    plt.title("Solarcell graph voltage (V) against current (I)")
    plt.xlabel("Voltage (V)")
    plt.ylabel("Current (I)")
    plt.show()
    plt.errorbar(R_var_list_mean,P_solarcell_list_mean, xerr = error_R_var_list,yerr =error_P_solarcell_list, fmt = '.' )
    plt.xlabel("Variable resistancte (Ohm)")
    plt.ylabel("Power solarcell (W)")
    plt.show()

plot()