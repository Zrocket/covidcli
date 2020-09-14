import click
import COVID19Py
import plotext

@click.command()
def hello():
    click.echo('Hello!')
    covid = COVID19Py.COVID19()
