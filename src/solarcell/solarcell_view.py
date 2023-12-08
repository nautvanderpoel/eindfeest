from solarcell_model import DiodeExperiment, find_ports
import click
import csv
import matplotlib.pyplot as plt

@click.group()
def cmd_group():
    pass

@cmd_group.command(help= "gives list of all available ports for connected arduino device")
def list():
    """function that returns back the available ports to the arduino device from the model

    Returns:
        list: available ports
    """
    return print(find_ports())