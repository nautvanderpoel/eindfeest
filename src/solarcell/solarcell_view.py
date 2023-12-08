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
    print('PLOTTING')
    measurements = DiodeExperiment(port = "ASRL9::INSTR")
    U_solarcell_list, I_solarcell_list = measurements.scan(start = 0, stop = 5)

    plt.plot(I_solarcell_list,U_solarcell_list)
    plt.show()

plot()