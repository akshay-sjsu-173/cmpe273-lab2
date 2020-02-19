from flask import Flask, escape, request, json
app = Flask(__name__)
#f = open(data_file,'r')
students = []
student_id = 0
class_id = 0
classes = []

def updateClass(id,data): #Update student list for class
    #print([x for x in students],data)
    student = [x for x in students if x['id']==data['student_id']]
    if len(student)<=0:
        return "Invalid student ID."
    for c in classes:
        if c['id']==id:
            c['students'].append(student[0])
            return c #"Added student "+str(id)+" to class "+str(id)
    return "No class found for ID "+str(id)

@app.route('/students', methods=['POST'])  #Admit new students to school
def addNewSudent():
    global student_id
    parameters = request.args #.get('p1')
    new_student = {"id": student_id+1, "name": parameters.get('name')}
    student_id += 1
    students.append(new_student)
    return new_student

@app.route('/students/<int:id>', methods=['GET']) #Get data for an existing student
def studentDetails(id):
    result = [x for x in students if x['id']==id]
    #next(x for x in students if x['id']==id)
    return {"result":result}

@app.route('/classes/<int:id>', methods=['GET','PATCH']) #Enroll existing student to class
def classDetails(id):
    if request.method == 'GET':
        result = [x for x in classes if x['id']==id]
        return {"result":result}
    elif request.method == 'PATCH':
        return updateClass(id, request.json)


@app.route('/classes', methods=['POST']) #Create a new class
def addNewClass():
    global class_id
    parameters = request.args
    new_class = {"id": class_id+1, "name": parameters.get('name'), "students":[]}
    class_id += 1
    classes.append(new_class)
    return new_class
