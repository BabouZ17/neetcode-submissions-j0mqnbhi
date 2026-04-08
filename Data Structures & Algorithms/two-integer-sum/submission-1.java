class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> remainers = new HashMap<Integer, Integer>();
        List<Integer> result = new ArrayList<Integer>();
        int outputOne = 0;
        int outputTwo = 0;

        for (int i = 0; i < nums.length; i++) {
            int remainer = target - nums[i];
            if (remainers.containsKey(remainer)) {
                outputOne = remainers.get(remainer);
                outputTwo = i;
            }
            remainers.put(nums[i], i);
        }
        int[] res = {outputOne, outputTwo};
        return res;
    }
}
