class Solution {
    public boolean hasDuplicate(int[] nums) {
        boolean dupe = false;
        for (int i = 0; i<nums.length; i++){
            for (int j = i+1; j<nums.length;j++ ){
                if (j>nums.length){
                    break;
                }else{
                    if (nums[i]==nums[j]){
                        dupe = true;
                        break;
                    }
                }

            }
        }
        return dupe;
            

    }
}