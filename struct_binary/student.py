import struct

with open('student.data', 'rb') as student_file:
    student = student_file.read()
    print(student)
    name, age, avg_score = struct.unpack('10sif', student)

    name = name.decode().rstrip('\x00')
    avg_score = round(avg_score, 2)
    print(name, age, avg_score)
