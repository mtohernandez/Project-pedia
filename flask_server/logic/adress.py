class Adress(object):
    """
    Class used to represent the adress of a user
    """

    def __init__(self, zip_code: int, street: str = 'Street', city: str = 'City', country: str = 'Country', department: str = 'Department'):
        """ Adress constructor object.

        :param zip_code: postal zip code of the person.
        :type zip_code: int
        :param street: name of the street.
        :type street: str
        :param city: name of the city.
        :type city: str
        :param country: name of the country
        :type country: str
        :param department: name of the department
        :type department: str
        :returns: Adress object
        :rtype: object
        """
        self._zip_code = zip_code
        self._street = street
        self._city = city
        self._country = country
        self._department = department
        

    @property
    def zip_code(self) -> int:
        """ Returns zip_code of the person.
          :returns: zip_code of person.
          :rtype: int
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code: int):
        """ The zip code of the person.
        :param zip_code: zip_code of the person.
        :type: int
        """
        self._zip_code = zip_code
    
    @property
    def street(self) -> str:
        """ Returns name of the street.
          :returns: street of adress.
          :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street: str):
        """ The street of the adress.
        :param street: street of adress.
        :type: str
        """
        self._street = street
    
    @property
    def city(self) -> str:
        """ Returns city of the adress.
          :returns: name of the city of adress.
          :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city: str):
        """ The city of the adress.
        :param city: name of the city of adress.
        :type: str
        """
        self._city = city
    
    @property
    def country(self) -> str:
        """ Returns country of the adress.
          :returns: country of adress.
          :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country: str):
        """ The country of the adress.
        :param country: country of the adress.
        :type: str
        """
        self._country = country

    @property
    def department(self) -> str:
        """ Returns department of the adress.
          :returns: department of adress.
          :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department: str):
        """ The department of the adress.
        :param department: department of the adress.
        :type: str
        """
        self._department = department

    def __str__(self):
        """ Returns str of adress.
          :returns: sting adress
          :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4})'.format(self.zip_code, self.street, self.city, self.country, self.department)

