from solarcell_model import DiodeExperiment, find_ports
import click
import csv
import matplotlib.pyplot as plt

@click.group()
def cmd_group():
    pass

# @cmd_group.command(help= "gives list of all available ports for connected arduino device")
# def list():
#     """function that returns back the available ports to the arduino device from the model

#     Returns:
#         list: available ports
#     """
    # return print(find_ports())


@cmd_group.command()
def plot():
    measurements = DiodeExperiment
    U_solarcell_list, I_solarcell_list = measurements.scan(0,1023)

    plt.plot(I_solarcell_list,U_solarcell_list)
    plt.show()
