/**
 * Student
 */

/**
 * Student
 */
public class Student {

    public static void main(String[] args) {
        StudentObj student = new StudentObj();
        student.setStudent("n", "s", "o");
    }
}

class StudentObj {

    float height, weight;
    String name, sex, no;

    void setStudent(String n, String s, String o) {
        name = n; sex = s; no = o;
        System.out.println("name: "+ name);
        System.out.println("sex: "+ sex);
        System.out.println("no: "+ no);
    }

    void setWH(float h, float w) {
        height = h; weight = w;
        System.out.println("height: "+ height);
        System.out.println("weight: "+ weight);
    }
}
