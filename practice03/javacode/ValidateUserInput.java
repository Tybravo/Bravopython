//Quuestion 3.1

import java.util.Scanner;
public class ValidateUserInput{

	static public void main(String...args){


	Scanner input = new Scanner(System.in);

System.out.print("Collect student score or enter 1 to stop iput: ");
int isNumber = input.nextInt();

int totalPassed = 0;
int currentFailed = 0;
int totalFailed = 0;
int totalPassed = 0;
int counter = 0;
int firstCounter = 0;
int secondCounter = 0;

while(isnumber != 1){
		if(isNumber >= 40 && isnumber <= 100){
			firstCounter = 1;
			System.out.print("The student passed with a score of ", isNumber);
			System.out.print("Current number of student passed is ", firstCounter);

			totalPassed = totalPassed + firstCounter;
			
			System.out.print("Total number of student passed is ", totalPassed);
			int isNumber = input.nextInt();
			}

		else{ if(isNumber > 0 && isNumber < 40){
			secondCounter = 1;
			System.out.print("The student failed with a score of ", isNumber);
			System.out.print("Current number of student failed is ", secondCounter);

			totalFailed = totalFailed + secondCounter;
			
			System.out.print("Total number of student failed is ", totalFailed);
			int isNumber = input.nextInt();
			}
			}
		else {if(isNumber > 100){
			System.out.print("You have entered a score out of range");
			int isNumber = input.nextInt();
			}
			}
		else
			System.out.print("Application Ended");
			//break;



