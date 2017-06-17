# Skeleton of a CLI

import click
import pyskel
import multiprocessing


@click.group(name='pyskel', chain=True)
@click.argument('count', type=int, metavar='N')
@click.pass_context
def cli(ctx, count):
    """Echo a value `N` number of times"""
    p1 = count
    p2 = tuple(range(5))
    ctx.obj = pyskel.Simulation((p1, p2))


@cli.command()
@click.option('--p1-val', type=float)
@click.pass_obj
def run(sim, p1_val):
    pyskel.mod_run((sim, p1_val))


@cli.command()
@click.option('--p1-range', type=(int, int, int),
              help="tuple passed is called with range(first, second, step)")
@click.pass_obj
def run_several_par1(sim, p1_range):
    first, last, step = p1_range
    p1_vals = list(range(first, last, step))

    pool = multiprocessing.Pool(3)
    res = pool.map(pyskel.mod_run, ((sim, p) for p in p1_vals))
    print(res)
