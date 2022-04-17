import re


class Utils:
    '''Contains the static utility functions for the application'''
    @staticmethod
    def email_is_valid(email: str) -> bool:
        '''
        Checks whether the given email address is valid or not
        :param email: Email to be verified

        :return: bool, True if the user is valid else False
        '''
        email_address_matcher = re.compile('^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$')
        return True if email_address_matcher.match(email) else False
