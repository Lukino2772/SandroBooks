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

@click.command("populate_db")
@with_appcontext
def populate_db():
    from src.models.user import User
    username = "admin"
    password = "admin123"

    existing = User.query.filter_by(username=username).first()
    if existing:
        click.echo("admin exists")
        return

    u = User(username=username)
    u.password = password
    db.session.add(u)
    db.session.commit()
    click.echo("created admin")
