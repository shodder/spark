
import click

from spark import Session
from spark.model import User
from spark.model import Address


@click.group()
def cli():
    pass


@cli.command()
def plugmein():

    click.echo('Welcome')
    session = Session()

    a = Address(
        house_num=10,
        street='Baker Street',
        city='London')

    u = User(
        first_name='Sherlock',
        family_name='Holmes',
        age=77,
        address=a)

    session.add(u)
    session.flush()
    session.commit()

    u = User.query.first()
    click.echo(u.address.street)

    from spark.hello_plugins import HelloModel
    from spark.goodbye_plugins import GoodbyeModel
    u.say_hello()
    u.address.say_hello()

    u.say_goodbye()
    u.address.say_goodbye()


