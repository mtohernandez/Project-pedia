import datetime

currentTime =  datetime.datetime.now()

class Date(object):
    """
    Class used to represent the subbmision date of a project
    """

    def __init__(self, day: int = currentTime.day, month: int = currentTime.month, year: int = currentTime.year):
        """ 
        Date constructor object.
        :param day: day the project was submitted.
        :type day: int
        :param month: month the project was submitted.
        :type street: str
        :param year: year the project was submitted.
        :type year: int
        :returns: Date object
        :rtype: object
        """
        self._day = day
        self._month = month
        self._year = year
        

    @property
    def day(self) -> int:
        """ Returns day of subbmision.
          :returns: day of subbmision.
          :rtype: int
        """
        return self._day

    @day.setter
    def day(self, day: int):
        """ The day of submission of the project.
        :param day: day of submission of the project.
        :type: int
        """

        self._day = day
    
    @property
    def month(self) -> int:
        """ Returns month the project was submitted.
          :returns: month the prject was submitted.
          :rtype: int
        """
        return self._month

    @month.setter
    def month(self, month: int):
        """ The month the project was submitted.
        :param month: month the project was submitted.
        :type: int
        """
        self._month = month
    
    @property
    def year(self) -> int:
        """ Returns year the project was submitted.
          :returns: year the prject was submitted.
          :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year: int):
        """ The year the project was submitted.
        :param year: year the project was submitted.
        :type: int
        """
        self._year = year
    

    def __str__(self):
        """ Returns str of Date.
          :returns: sting Date
          :rtype: str
        """
        return '{0}/{1}/{2}'.format(self.day, self.month, self.year)

