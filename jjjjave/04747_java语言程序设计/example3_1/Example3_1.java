/**
 * Example3_1
 */
public class Example3_1 {

    public static void main(String[] args) {
        Point p1, p2, p3;
        p1 = new Point();
        p2 = new Point(40, 50);
        p3 = new Point(p1.getX() + p2.getX(), p1.getY() + p2.getY());
        System.out.println("p3.x = " + p3.x + "p3.y = " + p3.getY());
        Point p4 = new Point(p1.x,p1.y); 
        System.out.println("p4.x="+p4.x+",p4.y="+p4.y);
    }
}


class Point {

    int x, y; 
    
    Point() {
        x=10;y=20; 
    }

    Point(int x, int y) { 
        this.x=x;
        this.y=y; 
    }

    int getX() {return x;}

    int getY() {return y;};
}
