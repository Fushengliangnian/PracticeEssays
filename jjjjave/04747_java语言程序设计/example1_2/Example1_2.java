import java.applet.Applet;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Paint;

/**
 * Example1_2
 */
public class Example1_2 extends Applet {

    public void paint(Graphics g) {
        g.setColor(Color.blue);
        g.drawString("欢迎你学习java语言", 30, 20);
        g.setColor(Color.red);
        g.drawString("只要认真学习多上机，一定可以学好", 30, 50);
    }
}