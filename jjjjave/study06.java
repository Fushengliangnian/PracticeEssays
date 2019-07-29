import java.io.*;

public class Study06 {

    public static void main(String[] args) {
        Study05 s_1 = new Study05("name");
        Study05 s_2 = new Study05("name2");
        s_1.setAge(5);
        s_1.empSalary(999);
        s_1.set_des("sddfadvsfbv");
        s_1.printEmployee();

        s_2.setAge(51);
        s_2.empSalary(55555);
        s_2.set_des("sfdgsdghfzxas");
        s_2.printEmployee();

    }
    
}
