import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

class q2{

    public static void printString(String input){
        ArrayList<String> list = new ArrayList<String>();
        int len = input.length();
        for(int i =0; i< len; ++i){
            for(int j=i; j < len ; ++j){
                list.add(input.substring(i, j+1));
            }
        }
        Collections.sort(list);
        int listSize = list.size();
        System.out.print("[");
        for(int i =0 ; i < listSize - 1 ; ++i){
            System.out.print(list.get(i) + ",");
        }
        System.out.print(list.get(listSize -1 ) + "]");
    }

    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        printString(input);
    }
}