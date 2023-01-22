import java.util.Calendar;
import java.util.Scanner;

public class FixedWindow {
    
        public static void main(String[] args) throws Exception {
            Scanner scanner = new Scanner(System.in);
            Calendar calendar = Calendar.getInstance();
            final int HOUR_LIMIT = 1;
            final int MINUTE_LIMIT = 59;
            int callsLeft = 10;
            String choice;
            int startHour = calendar.get(Calendar.HOUR_OF_DAY);
            int startMinute = calendar.get(Calendar.MINUTE);
            int endHour = (startHour + HOUR_LIMIT) % 24;
            int endMinute = (startMinute + MINUTE_LIMIT) % 60;
            
            System.out.println("Your fixed window of use has been declared with " + HOUR_LIMIT + " hours and " + MINUTE_LIMIT + " minutes of use.");
            System.out.println("You can get 10 requests within the said amount of time.");
            System.out.println("Your time starts at " + startHour + " hours and " + startMinute + " minutes. It will end at " + endHour + " hours and " + endMinute + "minutes.");
            
            while (calendar.get(Calendar.HOUR_OF_DAY) <= endHour || calendar.get(Calendar.MINUTE) <= endMinute) {
                System.out.println("Would you like to make a call? Respond in 'y' or 'n'.");
                choice = scanner.next();
                if (choice.equals("y")) {
                    callsLeft --;
                    System.out.println("Request succesful. Requests available: " + callsLeft);
                } else {
                    System.out.println("Request not made.");
                }
                if (callsLeft <= 0) {
                    System.out.println("Quota limit reached.");
                    System.exit(0);
                }
                Thread.sleep(2000);
            }
            scanner.close();
        } 
}
