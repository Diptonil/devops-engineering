import java.util.Scanner;

class LeakyBucket {

    public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int bucketSize;
		int leakRate;
		int simulationSeconds;
		int i;
		int[] packetSize;
		int totalPackets;
		int counter;
		int packetArrived;
		int packetLeft;
		int packetSent;
		int packetDropped;
		int packetRecieved;
		
		System.out.print("Enter bucket size: ");
		bucketSize = scanner.nextInt();
		System.out.print("Enter operation rate: ");
		leakRate = scanner.nextInt();
		System.out.print("Enter seconds to simulate: ");
		simulationSeconds = scanner.nextInt();
		packetSize = new int[simulationSeconds];
		totalPackets = 0;
		counter = 0;
		packetDropped = 0;
		packetArrived = 0;
		packetLeft = 0;
		packetSent = 0;
		packetRecieved = 0;
		
		for(i = 0; i < simulationSeconds; i ++) {
		    System.out.print("Enter size of packets to simulate in second " + (i + 1) + ": ");
		    packetSize[i] = scanner.nextInt();
		    totalPackets += packetSize[i];
		}
		scanner.close();
		
		System.out.println("Second\tPacket Arrived\tPacket Sent\tPacket Left\tPacket Dropped");
		while (totalPackets > 0) {
		    packetRecieved = (counter < packetSize.length)? packetSize[counter] : 0;
		    packetArrived += (counter < packetSize.length)? packetSize[counter] : 0;
		    if (packetArrived > bucketSize) {
		        packetDropped = packetArrived - bucketSize;
		    } else {
		        packetDropped = 0;
		    }
		    packetSent = (packetArrived > leakRate)? 2 : packetArrived;
		    packetLeft = (packetArrived > bucketSize)? bucketSize - packetSent : packetArrived - packetSent;
		    System.out.println(counter + 1 + "\t" + packetRecieved + "\t" + packetSent + "\t" + packetLeft + "\t" + packetDropped);
		    counter ++;
		    packetArrived = packetLeft;
		    totalPackets = packetArrived;
		}
	}
}