from .User import User
from .adress import Adress

class Company(User):
    """
    Class used to represent a Company, this class inherits the super class methods and atributes
    """
    def __init__(self, id_user: int, nitNumber: int, adress: Adress, name: str = 'Name', email: str = 'Email', password: str = 'Password', typeu: str = 'company'):
        """ User constructor abstract.
        :param id_user: id of the Company.
        :type id: int
        :param name: name of the Company.
        :type name: str
        :param email: email adress of the Company
        :type email: str
        :param password: password of the Company to access the system
        :type password: str
        :param adress: physical adress of the Company
        :type adress: Adress
        :param nitNumber: nit number of the Company
        :type nitNumber: int
        :returns: Company object
        :rtype: object
        """
        super().__init__(id_user, adress, name, email, password)
        self._nitNumber = nitNumber
        self._typeu = typeu
    
    @property
    def id_user(self):
        """ Returns id of the Company.
          :returns: id of the Company.
          :rtype: int
        """
        super().id_user(self)
    
    @id_user.setter
    def id_user(self, id_user: int):
        """ The id of the Company.
        :param id_user: id of Company.
        :type: int
        """
        super(Company, Company).value.__set__(self, id_user)
    
    @property
    def name(self):
        """ Returns the name of the Company.
          :returns: name of the Company.
          :rtype: str
        """
        super().name(self)
    
    @name.setter
    def name(self, name: str):
        """ The name of the Company.
        :param name: name of the Company.
        :type: str
        """
        super(Company, Company).value.__set__(self, name)
    
    @property
    def email(self):
        """ Returns the email of the Company.
          :returns: email of the Company.
          :rtype: str
        """
        super().email(self)
    
    @email.setter
    def email(self, email: str):
        """ The email of the Company
        :param email: email of the Company.
        :type: str
        """
        super(Company, Company).value.__set__(self, email)
    
    @property
    def password(self):
        """ Returns the password of the Company.
          :returns: password of the Company.
          :rtype: str
        """
        super().password(self)

    @password.setter
    def password(self, password: str):
        """ The password of the Company.
        :param password: password of the Company.
        :type: str
        """
        super(Company, Company).value.__set__(self, password)
    
    @property
    def adress(self):
        """ Returns the adress of the Company.
          :returns: adresss of the Company.
          :rtype: Adress
        """
        super().adress(self)
    
    @adress.setter
    def adress(self, adress: Adress):
        """ The adress of the Company.
        :param adress: adress of the Company.
        :type: Adress
        """
        super(Company, Company).value.__set__(self, adress)
    
    @property
    def nitNumber(self) -> int:
        """ Returns nitNumber of the Company.
          :returns: nitNumber of the Company.
          :rtype: int
        """
        return self._nitNumber
    
    @nitNumber.setter
    def id_user(self, nitNumber: int):
        """ The nit number of the Company.
        :param nitNumber: nitNumber of Company.
        :type: int
        """
        self._nitNumber = nitNumber

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
        return '({0}, {1.nitNumber})'.format(super().__str__(), self)
