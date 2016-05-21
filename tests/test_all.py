
import pytest

from spark import Session
from spark.model import User
from spark.model import Address


def test_all():

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

    a = Address.query.first()

    assert a is not None
