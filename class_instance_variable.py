class School:
    school_name="BSI"

    def __init__(self,name):
        self.student_name=name

sch1=School("Rumy")
sch2=School("Ehsan")
print(sch1.school_name)
print(sch1.student_name)
print(sch2.school_name,sch2.student_name)
School.school_name="BISC"
print(sch1.school_name)
print(sch1.student_name)
print(sch2.school_name,sch2.student_name)