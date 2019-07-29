
public class Dog {

    int age;
    String name;

    public Dog(String sex) {
        System.out.println("The dog is " + sex);
    }

    public void setAge(int dog_age) {
        age = dog_age;
    }

    public int getAge() {
        return age;
    }

    public static void main(String[] args) {
        Dog myDog = new Dog("man");
        myDog.setAge(10);
        System.out.println(myDog.age);
        System.out.println(myDog.getAge());
    }

}