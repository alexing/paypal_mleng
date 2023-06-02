"""
3. CountZeroSumSlices

Write a function solution that, given an array A consisting of N integers, returns the number of fragments of A whose
sum equals 0 (that is, pairs (P, Q) such that P ≤ Q and the sum A[P] + A[P+1] + ... + A[Q] is 0).
The function should return −1 if this number exceeds 1,000,000,000.

Examples:
    Given A = [2, −2, 3, 0, 4, −7], the function should return 4, as explained on this picture:
    Intervals with sum 0: [2, -2], [3, 0, 4, -7], [0], [2, -2, 3, 0, 4, -7]
    Given A = [0, 0, ..., 0] of length 100,000, the function should return −1.

Write an efficient algorithm for the following assumptions:
    N is an integer within the range [1..100,000];
    each element of array A is an integer within the range [−10,000..10,000].
"""


    public static int countZeroSumSlices(List<Integer> A) {
        /* Some details on efficiency:
            - Time complexity:
                The algorithm scans the array once. This operation is O(n).
                For each array element, it performs operations on a HashMap (put, get, containsKey) which are 
                generally considered O(1) operations.
                Therefore, the total time complexity of the algorithm is O(n).
            - Space complexity:
                A HashMap is used to keep track of the prefix sum frequencies. 
                In the worst case, each prefix sum is unique and the size of the HashMap is equal to 
                the size of the array, which is O(n).
                Therefore, the total space complexity of the algorithm is O(n).
        */
        final int limit = 1000000000;
        long prefixSum = 0;  
        int countZeroSum = 0;
        Map<Long, Integer> frequencyMap = new HashMap<>();
        frequencyMap.put(0L, 1);

        for (int value : A) {
            prefixSum += value;

            if (frequencyMap.containsKey(prefixSum)) {
                countZeroSum += frequencyMap.get(prefixSum);
            }

            frequencyMap.put(prefixSum, frequencyMap.getOrDefault(prefixSum, 0) + 1);

            if (countZeroSum > limit) {
                return -1;
            }
        }

        return countZeroSum;
    }