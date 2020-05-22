from wags import __version__
from wags.applications import Wags 


def test_version():
    assert __version__ == '0.1.0'


def test_applications():
    app = Wags()
    assert True

