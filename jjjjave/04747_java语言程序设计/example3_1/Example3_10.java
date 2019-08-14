/**
 * Example3_10
 */
public class Example3_10 {
    public static void main(String argc[]){
        Daughter girl = new Daughter();
        girl.cat = "漂亮的帽子";
        girl.weight = 35.0f;
        girl.height =120.0f;
        System.out.println(girl.speak("“我是女儿”")); 
        System.out.println(girl.speak("“我像母亲一样很会说话”")); 
        System.out.println(girl.speak("“我重”" + girl.weight + "“公斤”")); 
        System.out.println(girl.speak("“我高”"+ girl.height + "“公分”")); 
        System.out.println(girl.speak("“我还比母亲多一顶”"+girl.cat)); 
        System.out.println(girl.sing("“我还能唱歌”")); 
        System.out.println(girl.dance());
    }
    
}


class Mother{

    private int money;
    float weight, height;

    String speak(String s){return s;} 
    
    float getWeitht(){return weight;} 
    
    float getHeight(){return height;} 
    
    String dance(){return "我会跳舞";}
}


class Daughter extends Mother{ String cat;

    String sing(String s){return s;}

    String dance(){return "我是小舞蹈演员";} 
}




