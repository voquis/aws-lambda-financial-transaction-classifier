"""
Classifier unit tests
"""

from financial_transaction_classifier import __version__
from financial_transaction_classifier import classifier


def test_version():
    """
    Test package version
    """
    assert __version__ == '0.1.0'


def test_classifier():
    """
    Test classify function
    """
    assert classifier.classify('a') == 'a'
