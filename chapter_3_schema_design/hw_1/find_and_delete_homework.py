import pymongo

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.school
students = db.students


def find_and_remove():
    print('Removing lowest homework for each student...')

    query = {}

    try:
        students_docs = students.find(query)

        for student in students_docs:
            student['scores'].sort()
            for score in student['scores']:
                if score['type'] == 'homework':
                    students.update({'_id': student['_id']}, {'$pull': {'scores': score}})
                    break

    except Exception as e:
        print "Unexpected error:", type(e), e

    print('Done!')


find_and_remove()

# answer: after run this program, run the commands from the homework to get the answer
