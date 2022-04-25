from .User import User
from .adress import Adress

class Manager(User):
    """
    Class used to represent a Manager, this class inherits the super class methods and atributes
    """
    def __init__(self, id_user: int, adress: Adress, name: str = 'Name', last_name: str = "LastName", email: str = 'Email', password: str = 'Password', typeu: str = 'manager'):
        """ User constructor abstract.
        :param id_user: id of the Manager.
        :type id: int
        :param name: name of the Manager.
        :type name: str
        :param last_name: last name of the Manager.
        :type last_name: str
        :param email: email adress of the Manager
        :type email: str
        :param password: password of the Manager to access the system
        :type password: str
        :param adress: physical adress of the Manager
        :type adress: Adress
        :returns: Manager object
        :rtype: object
        """
        super().__init__(id_user, adress, name, email, password)
        self._last_name = last_name
        self._typeu = typeu
        
    
    @property
    def id_user(self):
        """ Returns id of the Manager.
          :returns: id of the Manager.
          :rtype: int
        """
        super().id_user(self)
    
    @id_user.setter
    def id_user(self, id_user: int):
        """ The id of the Manager.
        :param id_user: id of Manager.
        :type: int
        """
        super(Manager, Manager).value.__set__(self, id_user)
    
    @property
    def name(self):
        """ Returns the name of the Manager.
          :returns: name of the Manager.
          :rtype: str
        """
        super().name(self)
    
    @name.setter
    def name(self, name: str):
        """ The name of the Manager.
        :param name: name of the Manager.
        :type: str
        """
        super(Manager, Manager).value.__set__(self, name)
    
    @property
    def last_name(self) -> str:
        """ Returns the last name of the Manager.
          :returns: last name of the Manager.
          :rtype: str
        """
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name: str):
        """ The last name of the Manager.
        :param last_name: last name of the Manager.
        :type: str
        """
        self._last_name = last_name
    
    @property
    def last_name(self) -> str:
        """ Returns the last name of the Manager.
          :returns: last name of the Manager.
          :rtype: str
        """
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name: str):
        """ The last name of the Manager.
        :param last_name: last name of the Manager.
        :type: str
        """
        self._last_name = last_name
    
    @property
    def email(self):
        """ Returns the email of the Manager.
          :returns: email of the Manager.
          :rtype: str
        """
        super().email(self)
    
    @email.setter
    def email(self, email: str):
        """ The email of the Manager
        :param email: email of the Manager.
        :type: str
        """
        super(Manager, Manager).value.__set__(self, email)
    
    @property
    def password(self):
        """ Returns the password of the Manager.
          :returns: password of the Manager.
          :rtype: str
        """
        super().password(self)

    @password.setter
    def password(self, password: str):
        """ The password of the Manager.
        :param password: password of the Manager.
        :type: str
        """
        super(Manager, Manager).value.__set__(self, password)
    
    @property
    def adress(self):
        """ Returns the adress of the Manager.
          :returns: adresss of the Manager.
          :rtype: Adress
        """
        super().adress(self)
    
    @adress.setter
    def adress(self, adress: Adress):
        """ The adress of the Manager.
        :param adress: adress of the Manager.
        :type: Adress
        """
        super(Manager, Manager).value.__set__(self, adress)
    
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

