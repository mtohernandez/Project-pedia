from tkinter import X
from flask import Flask, jsonify, request
from flask_cors import CORS
from difflib import SequenceMatcher

from logic.project import Project
from logic.student import Student
from logic.adress import Adress
from logic.professor import Professor
from logic.manager import Manager
from logic.person import Person
from logic.company import Company

import random as rd


app = Flask(__name__)
students = []
managers = []
people = [] 
companies = []
projects = []
active = [] 

CORS(app)


@app.route('/signUp<type>', methods=['POST'])
def createUser(type):

    id = rd.randint(1000,5000)
    name = request.json['name']
    lastname = request.json['lastname']
    email = request.json['email']
    password = request.json['password']
    addressZipCode = request.json['addressZipCode']
    addressStreet = request.json['addressStreet']
    addressCity = request.json['addressCity']
    addressCountry = request.json['addressCountry']
    addressDeparment = request.json['addressDeparment']
    studentCode = request.json['studentCode']
    coursenumber = request.json['coursenumber']
    professor = request.json['professor']
    nitnumber = request.json['nitnumber']

    a = Adress(zip_code = addressZipCode, street = addressStreet, city = addressCity, country = addressCountry, department = addressDeparment)
    a = a.__dict__

    if type == 'student':
        p = Student(id_user = id,adress = a, courseNumber = coursenumber,studentCode = studentCode, assignedProfessor = professor, projects = [], name = name, last_name = lastname,email = email,password = password)
    
    elif type == 'company':
        p = Company(id_user = id,nitNumber = nitnumber, adress = a,name = name,email = email,password = password)
        
    elif type == 'professor':
        p = Professor(id_user = id,adress = a, courseNumber = coursenumber,name = name,last_name = lastname,email = email,password = password)
        
    elif type == 'person':
        p = Person(id_user = id,adress = a,name = name,last_name = lastname,email = email,password = password)
    elif type == 'manager':
        p = Manager(id_user=id, adress=a, name=name,last_name= lastname, email=email,password=password)
    
    p = p.__dict__
    people.append(p)

    return jsonify(people)

#? Sirve para despues
@app.route('/signUp', methods=['GET'])
def sendPeople():
    peoples = []
    for person in people:
        peoples.append({
            'id': person['id'],
            'name': person['name'],
            'lastname': person['lastname'],
            'email': person['email'],
            'password': person['password'],
            'address': person['address'],  
        })
    return jsonify(peoples)
    

@app.route('/signIn/<email>/<password>', methods=['GET'])
def getActive(email, password):

    found = False
    print(people)

    for x in people:
        if x['_email'] == email and x['_password'] == password:
            found = True   
            user = x                
        else:
            continue

    if found:
        active.append(user)
        return jsonify({'message': 'OK'})
    else:
        return jsonify({'message': 'NO'})

@app.route('/searchProfessor<cnumber>', methods=['GET'])
def searchProfessor(cnumber):
    for x in people:
        try:
            if x['_courseNumber'] == cnumber:
                return jsonify({'professor': '{} {}'.format(x['_name'],x['_last_name'])})
        except:
            continue
    
    return jsonify({'professor': 'Not assigned yet'})


@app.route('/getUser', methods=['GET'])
def getUser():
    print(people)
    return jsonify(active[0])

@app.route('/deleteActive', methods=['DELETE'])
def deleteActive():
    active.clear()
    print(active)
    return jsonify({'message': 'active clear'})

@app.route('/getProjects', methods=['GET'])
def getProject():
    for x in people:
        if x['_typeu'] == 'student':
            for y in x['_projects']:
                if not y in projects:
                    projects.append(y)

    print(projects)
    return jsonify(projects)

@app.route('/searchProjects<title>', methods=['GET'])
def searchProject(title):
    search = []
    if len(projects) > 0:
        for x in projects:
            if SequenceMatcher(None, x['_name'], title).ratio() > 0.4:
                search.append(x)

    return jsonify(search)

@app.route('/createP', methods=['POST'])
def createProject():

    id = rd.randint(1,9999)
    author = '{} {}'.format(active[0]['_name'],active[0]['_last_name'])
    submissionDate = request.json['submissionDate']
    name = request.json['name']
    state = 'IN REVIEW'
    description = request.json['description']
    background = request.json['background']

    p = Project(id,author,submissionDate,name,state,description,background)
    p = p.__dict__

    active[0]['_projects'].append(p)
    projects.append(p)
    print(active)
    print(projects)

    return jsonify({'message': 'OK'})

@app.route('/findProject<id>', methods=['GET'])
def findProject(id):
    for x in projects:
        try:
            if str(x['_id_project']) == id:
                print(jsonify(X))
                return jsonify(x)
        except:
            continue

    return jsonify({'message': 'not found'})

@app.route('/publishProject<id>', methods=['GET'])
def publishProject(id):
    for x in projects:
        try:
            if str(x['_id_project']) == id:
                x['_state'] = 'PROGRESS'
        except:
            continue

    return jsonify({'Project': 'published'})

@app.route('/deleteProject<id>', methods=['DELETE'])
def deleteProject(id):
    for x in projects:
        try:
            if str(x['_id_project']) == id:
                projects.remove(x)
        except:
            continue

    for x in people:
        if x['_typeu'] == 'student':
            for y in x['_projects']:
                if str(y['_id_project']) == id:
                    x['_projects'].remove(y)
        

    return jsonify({'Project': 'discarded'})


if __name__ == '__main__':
    app.run(debug = True)