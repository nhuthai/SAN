"""
SAN.cli
~~~
Command line to call operations
:copyright: 2017 by Nhut Hai Huynh.
:license: MIT, see LICENSE for more details.
"""

import click
from .AC import *
from .T2V import *

@click.group()
def SAN():
    pass

@SAN.command()
@click.argument('input_text', type=str)
def reading(input_text):
    """Read input text with standard voice.
    Parse text first, then try to find the most matching terms as well as sounds
    Finally, merge sounds, release audio and play audio

    \b
    :param input_text: text which users want to listen.
    """
    read(input_text)

@SAN.command()
@click.option('-m','--learning_mode',type=click.Choice(['unsupervised', 'supervised']),
              default='unsupervised',show_default=True,
              help='Learning mode: supervised (deep learning) or unsupervised \
              (entropy or Bayes network)')
def learning_to_read(learning_mode):
    """Trains to group the most popular terms:
    1. Supervised - Deep Learning or Decision Trees: inputs are the given texts
    and corresponding speeches. Labels for input are pre-defined cluster. Output
    is MODEL predicts terms which usually occur together. Training is based on
    continuity of speech files and probabilities of term clustering.
    2. Unsupervised - Entropy or Bayesian network: inputs are tons of documents
    without speech. Outputs are TERMS which usually occur together. Training is
    based on the time of occurring of terms.

    \b
    :param learning_mode: unsupervised or supervised
    """
    click.echo('Learn to read!')

@SAN.command()
@click.argument('input_text', type=str)
@click.argument('id_user', type=int)
def parody(input_text,id_user):
    """Change voice to be similar to individual voice.

    \b
    :param input_text: text which users want to listen.
    :param id_user: individual voice which we try to parody if applicable.
    """
    click.echo('Parody!')

@SAN.command()
@click.argument('id_user', type=int)
def learning_to_parody(id_user):
    """Trains the voice in the given speech list.
    Analyze speech files and retrieve the knowledge about this voice.
    Finally, store the parameters of this voice to parody in the future.

    \b
    :param id_user: individual voice which we try to parody if applicable.
    """
    click.echo('Learn to parody!')

if __name__ == '__main__':
    SAN()
