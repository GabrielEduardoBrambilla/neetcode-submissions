class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> ver = new HashSet<Integer>();
        for(int num : nums ){
            if(ver.contains(num)){
                return true;
            }else{
                ver.add(num);
            }
        }
        return false;
    }
}