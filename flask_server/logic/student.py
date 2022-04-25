from .User import User
from .adress import Adress
from .professor import Professor


class Student(User):
    """
    Class used to represent a Student, this class inherits the super class methods and atributes
    """
    def __init__(self, id_user: int, adress: Adress, courseNumber: str, studentCode: str, assignedProfessor: Professor, projects: list = [] ,name: str = 'Name', last_name: str = "LastName", email: str = 'Email', password: str = 'Password', typeu: str = 'student'):
        """ User constructor abstract.
        :param id_user: id of the Student.
        :type id: int
        :param name: name of the Student.
        :type name: str
        :param last_name: last name of the Student.
        :type last_name: str
        :param email: email adress of the Student
        :type email: str
        :param password: password of the Student to access the system
        :type password: str
        :param adress: physical adress of the Student
        :type adress: Adress
        :param courseNumber: course number in wich the Student is assigned
        :type courseNumber: str
        :param studentCode: code of the Student.
        :type: str
        :returns: Student object
        :rtype: object
        """
        super().__init__(id_user, adress, name, email, password)
        self._last_name = last_name
        self._courseNumber = courseNumber
        self._assignedProfessor = assignedProfessor
        self._studentCode = studentCode
        self._projects = projects
        self._typeu = typeu
        
    
    @property
    def id_user(self):
        """ Returns id of the Student.
          :returns: id of the Student.
          :rtype: int
        """
        super().id_user(self)
    
    @id_user.setter
    def id_user(self, id_user: int):
        """ The id of the Student.
        :param id_user: id of Student.
        :type: int
        """
        super (Student, Student).value.__set__(self, id_user)
    
    @property
    def name(self):
        """ Returns the name of the Student.
          :returns: name of the Student.
          :rtype: str
        """
        super().name(self)
    
    @name.setter
    def name(self, name: str):
        """ The name of the Student.
        :param name: name of the Student.
        :type: str
        """
        super (Student, Student).value.__set__(self, name)
    
    @property
    def last_name(self) -> str:
        """ Returns the last name of the Student.
          :returns: last name of the Student.
          :rtype: str
        """
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name: str):
        """ The last name of the Student.
        :param last_name: last name of the Student.
        :type: str
        """
        self._last_name = last_name
    
    @property
    def studentCode(self) -> str:
        """ Returns the code of the Student.
          :returns: code of the Student.
          :rtype: str
        """
        return self._studentCode
    
    @studentCode.setter
    def studentCode(self, studentCode: str):
        """ The code of the Student.
        :param studentCode: code of the Student.
        :type: str
        """
        self._studentCode = studentCode
    
    @property
    def projects(self) -> list:
        """ Returns the code of the Student.
          :returns: code of the Student.
          :rtype: list
        """
        return self._projects
    
    @projects.setter
    def projects(self, projects: list):
        """ The code of the Student.
        :param studentCode: code of the Student.
        :type: str
        """
        self._projects = projects
    
    @property
    def assignedProfessor(self) -> Professor:
        """ Returns the assigned professor of the Student.
          :returns: assigned professor of the Student.
          :rtype: Professor
        """
        return self._assignedProfessor
    
    @assignedProfessor.setter
    def assignedProfessor(self, assignedProfessor: Professor):
        """ The assigned professorof the Student.
        :param assignedProfessor: assigned professor of the Student.
        :type: Professor
        """
        self._assignedProfessor = assignedProfessor
    
    @property
    def courseNumber(self) -> str:
        """ Returns the courseNumber of the Student.
          :returns: course number of the Student.
          :rtype: str
        """
        return self._courseNumber
    
    @courseNumber.setter
    def courseNumber(self, courseNumber: str):
        """ The course number of the Student.
        :param courseNumber: course number in which the Student is assigned.
        :type: str
        """
        self._courseNumber = courseNumber
    
    
    @property
    def email(self):
        """ Returns the email of the Student.
          :returns: email of the Student.
          :rtype: str
        """
        super().email(self)
    
    @email.setter
    def email(self, email: str):
        """ The email of the Student
        :param email: email of the Student.
        :type: str
        """
        super (Student, Student).value.__set__(self, email)
    
    @property
    def password(self):
        """ Returns the password of the Student.
          :returns: password of the Student.
          :rtype: str
        """
        super().password(self)

    @password.setter
    def password(self, password: str):
        """ The password of the Student.
        :param password: password of the Student.
        :type: str
        """
        super (Student, Student).value.__set__(self, password)
    
    @property
    def adress(self):
        """ Returns the adress of the Student.
          :returns: adresss of the Student.
          :rtype: Adress
        """
        super().adress(self)
    
    @adress.setter
    def adress(self, adress: Adress):
        """ The adress of the Student.
        :param adress: adress of the Student.
        :type: Adress
        """
        super (Student, Student).value.__set__(self, adress)

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
    
    def makeNewProposal(self, p):
        """
        adds a new project to the
        projects attribute of student
        """
        self._projects.append(p)

    def __str__(self):
        """ Returns str of the student.
          :returns: string student
          :rtype: str
        """
        return '{0}, {1.last_name}, {1.courseNumber}, {1.studentCode}, {1.assignedProfessor}, {1.projects!s}'.format(super().__str__(), self)
