from abc import abstractproperty, abstractmethod, ABC
from logic.adress import Adress

class User(ABC):
    """
    Class used to represent a User, this is an abstract class
    """
    @abstractmethod
    def __init__(self, id_user: int, adress: Adress, name: str = 'Name', email: str = 'Email', password: str = 'Password'):
        """ User constructor abstract.
        :param id: id of the user.
        :type id: int
        :param name: name of the user.
        :type name: str
        :param email: email adress of the user
        :type email: str
        :param password: password of the user to access the system
        :type password: str
        :param adress: physical adress of the user
        :type adress: Adress
        :returns: User object
        :rtype: object
        """
        self._id_user = id_user
        self._name = name
        self._email = email
        self._password = password
        self._adress = adress

    @abstractproperty
    def id_user(self) -> int:
        """ Returns id of the user.
          :returns: id of the user.
          :rtype: int
        """
        return self._id_user

    @abstractmethod
    @id_user.setter
    def id_user(self, id_user: int):
        """ The id of the user.
        :param id_user: id of user.
        :type: int
        """
        self._id_user = id_user

    @abstractproperty
    def name(self) -> str:
        """ Returns the name of the user.
          :returns: name of the user.
          :rtype: str
        """
        return self._name
    
    @abstractmethod
    @name.setter
    def name(self, name: str):
        """ The name of the user.
        :param name: name of th user.
        :type: str
        """
        self._name = name
    
    @abstractproperty
    def email(self) -> str:
        """ Returns the email of the user.
          :returns: email of the user.
          :rtype: str
        """
        return self._email
    
    @abstractmethod
    @email.setter
    def email(self, email: str):
        """ The email of the user.
        :param email: email of the user.
        :type: str
        """
        self._email = email
    
    @abstractproperty
    def password(self) -> str:
        """ Returns the password of the user.
          :returns: password of the user.
          :rtype: str
        """
        return self._password
    
    @abstractmethod
    @password.setter
    def password(self, password: str):
        """ The password of the user.
        :param password: password of the user.
        :type: str
        """
        self._password = password
    
    @abstractproperty
    def adress(self) -> Adress:
        """ Returns the adress of the user.
          :returns: adresss of the user.
          :rtype: Adress
        """
        return self._adress

    @abstractmethod
    @adress.setter
    def adress(self, adress: Adress):
        """ The adress of the user.
        :param adress: adress of the user.
        :type: Adress
        """
        self._adress = adress

    @abstractmethod
    def __str__(self):
        """ Returns str of the user.
          :returns: string user
          :rtype: str
        """
        return '{0._id_user!s}, {0._adress!s}, {0._name!s}'.format(self)
