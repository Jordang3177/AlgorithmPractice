class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int answer = 0;
        while (left < right) {
            int smaller = Math.min(height[left], height[right]);
            int area = (right - left) * smaller;
            answer = Math.max(answer, area);
            if (smaller == height[left]) {
                left += 1;
            }
            else {
                right -= 1;
            }
        }
        return answer;
    }
}