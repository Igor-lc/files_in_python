using namespace std;

struct Student {
    char name[10];
    int age;
    float avg_score;
};

int main()
{
    Student student;
    strcpy(student.name, "Guido");
    student.age = 21;
    student.avg_score = 8.83;

    ofstream output_file("student.data", ios::binary);

    output_file.write((char*)&student, sizeof(student));
    output_file.close();

    return 0;
};
