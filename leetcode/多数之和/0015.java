import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
// import java.util.stream.Collectors;

// 执行用时 : 97 ms , 在所有 Java 提交中击败了 12.82% 的用户
// 内存消耗 : 43.9 MB , 在所有 Java 提交中击败了 98.11% 的用户
class Solution {
  public List<List<Integer>> threeSum(int[] nums) {
    int target = 0;
    List<List<Integer>> ans = new ArrayList<List<Integer>>();
    Map<Integer, Integer> countHash = new HashMap<Integer, Integer>();
    Arrays.sort(nums); // 排序整理
    for (int i = 0; i < nums.length; i++) {
      Integer lastC = countHash.get(nums[i]);
      countHash.put(nums[i], (Objects.equals(lastC, null) ? 0 : lastC) + 1); // 每个元素计数
    }
    Integer lastI = null;
    for (int i = 0; i < nums.length; i++) {
      if (Objects.equals(nums[i], lastI))
        continue; // 去重
      lastI = nums[i];
      Integer lastJ = null;
      for (int j = i + 1; j < nums.length; j++) { // 两层循环 两两比对
        if (Objects.equals(nums[j], lastJ))
          continue; // 去重
        lastJ = nums[j];
        int left = target - (nums[i] + nums[j]);
        if (left < nums[i] || left < nums[j])
          continue; // 去重
        if (countHash.get(left) != null) { // 如果第三个数存在
          int remaining = countHash.get(left);
          if (nums[i] == left)
            remaining--;
          if (nums[j] == left)
            remaining--;
          if (remaining > 0) {
            List<Integer> list = Arrays.asList(nums[i], nums[j], left);
            ans.add(list);
          }
        }
      }
    }
    return ans;
  }
}
