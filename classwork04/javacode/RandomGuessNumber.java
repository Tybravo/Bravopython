import java.util.Random;

public class ReverseAnyInteger{


	public static void main(String[] args){
	Scanner scanner = new Scanner(System.in);

	rightRandom rand = new Random(1, 5);
	
System.out.print("Guess my number between 1 and 5: ");
int isNumber = rand.nextInt();
		
while(isnumber  != -1){
	if(isNumber < 1 or isNumber > 5){
		System.out.print("The number is too high or low, try again");
		isNumber = rand.nextInt();
	}
	else{
	 if(isNumber == rightRandom){
		System.out.print("Congratulation!!");
		isNumber = rand.nextInt();
	}
	}
	else{
		if(isNumber != rightRandom){
		print("Wrong guess!!")
		isNumber = System.out.print("Guess my number between 1 and 5 or -1 to quit: ");
		}
		}


	if(isNumber == -1){
		System.out.print("Thank you for playing the guess game!");
		}


      }

   }

}