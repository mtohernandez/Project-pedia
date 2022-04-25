from .User import User
from .adress import Adress

class Person(User):
    """
    Class used to represent a Person, this class inherits the super class methods and atributes
    """
    def __init__(self, id_user: int, adress: Adress, name: str = 'Name', last_name: str = "LastName", email: str = 'Email', password: str = 'Password', typeu: str = 'person'):
        """ User constructor abstract.
        :param id_user: id of the person.
        :type id: int
        :param name: name of the person.
        :type name: str
        :param last_name: last name of the person.
        :type last_name: str
        :param email: email adress of the person
        :type email: str
        :param password: password of the person to access the system
        :type password: str
        :param adress: physical adress of the person
        :type adress: Adress
        :returns: Person object
        :rtype: object
        """
        super().__init__(id_user, adress, name, email, password)
        self._last_name = last_name
        self._typeu = typeu
        
    
    @property
    def id_user(self):
        """ Returns id of the person.
          :returns: id of the person.
          :rtype: int
        """
        super().id_user(self)
    
    @id_user.setter
    def id_user(self, id_user: int):
        """ The id of the person.
        :param id_user: id of person.
        :type: int
        """
        super(Person, Person).value.__set__(self, id_user)
    
    @property
    def name(self):
        """ Returns the name of the person.
          :returns: name of the person.
          :rtype: str
        """
        super().name(self)
    
    @name.setter
    def name(self, name: str):
        """ The name of the person.
        :param name: name of the person.
        :type: str
        """
        super(Person, Person).value.__set__(self, name)
    
    @property
    def last_name(self) -> str:
        """ Returns the last name of the person.
          :returns: last name of the person.
          :rtype: str
        """
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name: str):
        """ The last name of the person.
        :param last_name: last name of the person.
        :type: str
        """
        self._last_name = last_name
    
    @property
    def last_name(self) -> str:
        """ Returns the last name of the person.
          :returns: last name of the person.
          :rtype: str
        """
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name: str):
        """ The last name of the person.
        :param last_name: last name of the person.
        :type: str
        """
        self._last_name = last_name
    
    @property
    def email(self):
        """ Returns the email of the person.
          :returns: email of the person.
          :rtype: str
        """
        super().email(self)
    
    @email.setter
    def email(self, email: str):
        """ The email of the person
        :param email: email of the person.
        :type: str
        """
        super(Person, Person).value.__set__(self, email)
    
    @property
    def password(self):
        """ Returns the password of the person.
          :returns: password of the person.
          :rtype: str
        """
        super().password(self)

    @password.setter
    def password(self, password: str):
        """ The password of the person.
        :param password: password of the person.
        :type: str
        """
        super(Person, Person).value.__set__(self, password)
    
    @property
    def adress(self):
        """ Returns the adress of the person.
          :returns: adresss of the person.
          :rtype: Adress
        """
        super().adress(self)
    
    @adress.setter
    def adress(self, adress: Adress):
        """ The adress of the person.
        :param adress: adress of the person.
        :type: Adress
        """
        super(Person, Person).value.__set__(self, adress)
    
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
        return '({0}, {1.last_name})'.format(super().__str__(), self)



