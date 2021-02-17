import requests


def get_programmer_count():
    """
    Return the number of programmers return from the plural programmers API
    :return: An integer indicating the number of programmers in the plural list.
    """
    return 0


def get_programmer_by_id(pid):
    """
    Return the single programmer referenced by the specified programmer id (pid)
    :param pid: Unique identifier for the programmer to lookup
    :return: A dictionary containing the matched programmer. Return an empty dictionary if not found
    """
    return {}


def get_last_name_from_first(first_name):
    """
    Return the last name of the *first* programmer having the provided first name.
    :param first_name: The first name to search by. The search is case insensitive, i.g. ada == ADA
    :return: A string containing the last name of the first programmer in the list of matches,
    or None if there are no matches.
    """
    return ""
