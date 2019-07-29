import java.io.*;


/**
 * study05
 */
public class Study05 {

    String name;
    int age;
    String des;
    double salary;

    public study05(String name) {
        this.name = name;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public void set_des(String des) {
        this.des = des;
    }

    public void empSalary(double empSalary){
        salary = empSalary;
    }
     /* 打印信息 */
    public void printEmployee(){
        System.out.println("名字:"+ name );
        System.out.println("年龄:" + age );
        System.out.println("职位:" + des );
        System.out.println("薪水:" + salary);
    }

}
