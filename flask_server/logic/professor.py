from .User import User
from .adress import Adress

class Professor(User):
    """
    Class used to represent a Professor, this class inherits the super class methods and atributes
    """
    def __init__(self, id_user: int, adress: Adress, courseNumber: str, name: str = 'Name', last_name: str = "LastName", email: str = 'Email', password: str = 'Password', typeu: str = 'professor'):
        """ User constructor abstract.
        :param id_user: id of the Professor.
        :type id: int
        :param name: name of the Professor.
        :type name: str
        :param last_name: last name of the Professor.
        :type last_name: str
        :param email: email adress of the Professor
        :type email: str
        :param password: password of the Professor to access the system
        :type password: str
        :param adress: physical adress of the Professor
        :type adress: Adress
        :param courseNumber: course number in wich the professor is assigned
        :type courseNumber: str
        :returns: Professor object
        :rtype: object
        """
        super().__init__(id_user, adress, name, email, password)
        self._last_name = last_name
        self._courseNumber = courseNumber
        self._typeu = typeu
        
    
    @property
    def id_user(self):
        """ Returns id of the Professor.
          :returns: id of the Professor.
          :rtype: int
        """
        super().id_user(self)
    
    @id_user.setter
    def id_user(self, id_user: int):
        """ The id of the Professor.
        :param id_user: id of Professor.
        :type: int
        """
        super (Professor, Professor).value.__set__(self, id_user)
    
    @property
    def name(self):
        """ Returns the name of the Professor.
          :returns: name of the Professor.
          :rtype: str
        """
        super().name(self)
    
    @name.setter
    def name(self, name: str):
        """ The name of the Professor.
        :param name: name of the Professor.
        :type: str
        """
        super (Professor, Professor).value.__set__(self, name)
    
    @property
    def last_name(self) -> str:
        """ Returns the last name of the Professor.
          :returns: last name of the Professor.
          :rtype: str
        """
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name: str):
        """ The last name of the Professor.
        :param last_name: last name of the Professor.
        :type: str
        """
        self._last_name = last_name
    
    @property
    def courseNumber(self) -> str:
        """ Returns the courseNumber of the Professor.
          :returns: course number of the Professor.
          :rtype: str
        """
        return self._courseNumber
    
    @courseNumber.setter
    def courseNumber(self, courseNumber: str):
        """ The course number of the Professor.
        :param courseNumber: course number in which the professor is assigned.
        :type: str
        """
        self._courseNumber = courseNumber
    
    @property
    def email(self):
        """ Returns the email of the Professor.
          :returns: email of the Professor.
          :rtype: str
        """
        super().email(self)
    
    @email.setter
    def email(self, email: str):
        """ The email of the Professor
        :param email: email of the Professor.
        :type: str
        """
        super (Professor, Professor).value.__set__(self, email)

    @property
    def password(self):
        """ Returns the password of the Professor.
          :returns: password of the Professor.
          :rtype: str
        """
        super().password(self)

    @password.setter
    def password(self, password: str):
        """ The password of the Professor.
        :param password: password of the Professor.
        :type: str
        """
        super (Professor, Professor).value.__set__(self, password)
    
    @property
    def adress(self):
        """ Returns the adress of the Professor.
          :returns: adresss of the Professor.
          :rtype: Adress
        """
        super().adress(self)
    
    @adress.setter
    def adress(self, adress: Adress):
        """ The adress of the Professor.
        :param adress: adress of the Professor.
        :type: Adress
        """
        super (Professor, Professor).value.__set__(self, adress)

    @property
    def typeu(self):
        """ Returns the adress of the Student.
          :returns: adresss of the Student.
          :rtype: Adress
        """
        return self._typeu
    
    @typeu.setter
    def typeu(self, typeu: str):
        """ The adress of the Student.
        :param adress: adress of the Student.
        :type: Adress
        """
        self._typeu = typeu

    def __str__(self):
        return '({0}, {1.last_name}, {1.courseNumber})'.format(super().__str__(), self)



