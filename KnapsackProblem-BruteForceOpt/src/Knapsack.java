import java.util.Arrays;

public class Knapsack {
    public int[] weights = {3,1,6,10,1,4,9,1,7,2,6,1,6,2,2,4,8,1,7,3,6,2,9,5,3,3,4,7,3,5};
    public int[] value = {7,4,9,18,9,15,4,2,6,13,18,12,12,16,19,19,10,16,14,3,14,4,15,7,5,10,10,13,19,9};
    public Integer[]  outputVector = new Integer[weights.length];
    public int maxWeight = 40;

    public Knapsack() {
        Arrays.fill(this.outputVector, 0);
    }

    public void findBestCombination() {
        String bestCombination = "";
        int bestValue = 0;
        int finalWeight = 0;

        int arrLength = weights.length;
        int N = (int) Math.pow(2d, Double.valueOf(arrLength));
        for (int i = 1; i < N; i++) {
            String code = Integer.toBinaryString(N|i).substring(1);
            int outputWeight = 0;
            int outputValue = 0;
            for (int j = 0; j < arrLength; j++) {
                if (code.charAt(j) == '1') {
                    outputWeight += this.weights[j];
                    outputValue += this.value[j];
                }
            }
            if(outputWeight <= this.maxWeight && outputValue > bestValue){
                bestCombination = code;
                bestValue = outputValue;
                finalWeight = outputWeight;
            }
        }
        System.out.println("Best combiation: " + bestCombination);
        System.out.println("Best value: " + bestValue);
        System.out.println("Final weight: " + finalWeight);
    }
}

