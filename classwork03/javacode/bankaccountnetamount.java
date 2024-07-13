import java.util.Scanner;

public class bankaccountnetamount{

	static public void main(String...args){


	Scanner bravo = new Scanner(System.in);

	System.out.print("Enter 1 to deposit , 2 to widthraw or -1 to quit: ");
	double entry = bravo.nextDouble();
	
	double totalbalance = 0;	
		
	while(entry != -1){
	if(entry ==1){
		System.out.print("Enter amount to deposit or -1 to quit: ");
		double deposit = bravo.nextDouble();

		totalbalance += deposit;

		System.out.printf("Total balance is %.2f%n",totalbalance);
		System.out.print("Enter 1 to deposit , 2 to widthraw or -1 to quit: ");
		entry = bravo.nextDouble();
		}
	else{
	if(entry ==2){
		System.out.print("Enter amount to widthraw or -1 to quit: ");
		double widthraw = bravo.nextDouble();

		totalbalance -= widthraw;

		System.out.printf("Total balance is %.2f %n",totalbalance);
		System.out.print("Enter 1 to deposit , 2 to widthraw or -1 to quit: ");
		entry = bravo.nextDouble();
	}
	}
	//else{
	if(entry != 1 && entry != 2){
		System.out.println("Invalid input");

		System.out.println("Enter 1 to deposit , 2 to widthraw or -1 to quit: ");
	}
	


	}


    }

}





