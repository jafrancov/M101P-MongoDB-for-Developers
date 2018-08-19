import pymongo

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.students
grades = db.grades


def find_and_remove():
    print("Actual number of grades: %i" % grades.count())
    print('Removing lowest homework for each student...')

    query = {'type': 'homework'}

    try:
        cursor = grades.find(query).sort([('student_id', pymongo.ASCENDING), ('score', pymongo.ASCENDING)])
        current_student = 0

        for doc in cursor:
            if doc['student_id'] == current_student:
                grades.remove(doc)
                current_student += 1

    except Exception as e:
        print "Unexpected error:", type(e), e

    print('Done!')
    print('Final number of grades: %i' % grades.count())


find_and_remove()

# answer: after run this program, run the commands from the homework to get the answer
