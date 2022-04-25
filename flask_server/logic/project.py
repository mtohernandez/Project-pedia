from datetime import date
from .student import Student
from .adress import Adress
from .professor import Professor

date = date.today

class Project(object):
    """
    Class used to represent a project
    """

    def __init__(self, id_project: int, author: str, submissionDate: date = date, name: str = 'Name', state: str = 'State', description: str = 'Description', background: str = 'Img'):
        """ project constructor abstract.
        :param id_project: id of the project.
        :type id_project: int
        :param name: name of the project.
        :type name: str
        :param submissionDate: date the project was submitted gets the current date when using the system
        :type submissionDate: Date
        :param author: author of the project (who did it)
        :type author: Student
        :param state: represents the current state of the project
        :type state: str
        :param description: small description of what the project is about
        :type description: str
        :returns: Project object
        :rtype: object
        """
        self._id_project = id_project
        self._name = name
        self._submissionDate = submissionDate
        self._author = author
        self._state = state
        self.description = description
        self.background = background

    @property
    def id_project(self) -> int:
        """ Returns id of the project.
          :returns: id of the project.
          :rtype: int
        """
        return self._id_project

    @id_project.setter
    def id_project(self, id_project: int):
        """ The id of the project.
        :param id_project: id of project.
        :type: int
        """
        self._id_project = id_project

    @property
    def name(self) -> str:
        """ Returns the name of the project.
          :returns: name of the project.
          :rtype: str
        """
        return self._name
    
    @name.setter
    def name(self, name: str):
        """ The name of the project.
        :param name: name of the project.
        :type: str
        """
        self._name = name
    
    @property
    def submissionDate(self) -> date:
        """ Returns the submissionDate of the project.
          :returns: submissionDate of the project.
          :rtype: Date
        """
        return self._submissionDate
    
    @submissionDate.setter
    def submissionDate(self, submissionDate: date):
        """ The submissionDate of the project.
        :param submissionDate: submission date of the project.
        :type: Date
        """
        self._submissionDate = submissionDate
    
    @property
    def author(self) -> str:
        """ Returns the author of the project.
          :returns: author of the project.
          :rtype: Student
        """
        return self._author
    
    @author.setter
    def author(self, author: str):
        """ The author of the project.
        :param author: author of the project.
        :type: str
        """
        self._author = author
    
    @property
    def state(self) -> str:
        """ Returns the state of the project.
          :returns: state of the project.
          :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str):
        """ The state of the project.
        :param state: state of the project.
        :type: str
        """
        self._state = state
    
    @property
    def description(self) -> str:
        """ Returns the description of the project.
          :returns: description of the project.
          :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """ The description of the project.
        :param description: description of the project.
        :type: str
        """
        self._description = description

    @property
    def background(self) -> str:
        """ Returns the URL of the background
          :returns: URL of the background
          :rtype: str
        """
        return self._background

    @background.setter
    def background(self, background: str):
        """ The URL of the background
        :param description: URL of the background.
        :type: str
        """
        self._background = background


    def __str__(self):
        """ Returns str of the project.
          :returns: string project
          :rtype: str
        """
        return '{0._id_project!s}, {0._state!s}, {0._name!s}, {0._submissionDate!s}, {0._description}, {0._background}, {0._author._name!s} {0._author._last_name!s}'.format(self)

