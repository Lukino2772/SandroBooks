import click
from flask.cli import with_appcontext

from src.ext import db

@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("initializing db")
    db.drop_all()
    db.create_all()
    click.echo("done")