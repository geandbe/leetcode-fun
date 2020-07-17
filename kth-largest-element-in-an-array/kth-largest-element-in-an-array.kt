class Solution {
    fun findKthLargest(nums: IntArray, k: Int): Int {
        return nums.sortedArrayDescending()[k - 1];
    }
}