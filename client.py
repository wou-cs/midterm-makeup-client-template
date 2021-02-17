import requests


def get_first_id():
    """
    Return the ID of the *first* programmer in the plural list of programmers at api/programmers
    :return: An integer representing the "id" field of the first programmer
    """
    return 0


def get_last_id():
    """
    Return the ID of the *last* programmer in the plural list of programmers at api/programmers
    :return: An integer representing the "id" field of the first programmer
    """
    return 0


def get_programmer_attribute_for_id(pid, field_name):
    """
    Return the field_name *value* referenced by the specified programmer id (pid)
    :param pid: Unique identifier for the programmer to lookup
    :param field_name: The field in the dictionary to return
    :return: The value of the specified field name, or None if the field or programmer do not exist
    """
    return None


def get_programmer_birth_year(first_name):
    """
    Return the birth year of the *first* programmer having the provided first name.
    :param first_name: The first name to search by. The search is case insensitive, i.g. ada == ADA
    :return: An integer corresponding to the birth year of the found programmer, or None if not found
    """
    return None
