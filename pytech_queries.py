find()
docs = db.students.find({})
print(doc)
doc = db.students_find_one({"student_id": "1007"})
print(doc["student_id"])