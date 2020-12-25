/* Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/
*/

var search = function(nums, target) {
    let sortedNums = [...nums].sort(function(a, b){return a-b})
    let left = 0
    let right = sortedNums.length-1
    
    while (left <= right){
        let mid = Math.floor((left + right)/2)

        if (target < sortedNums[mid]){
            right = mid-1
        }
        else if (target > sortedNums[mid]){
            left = mid + 1
        }
        else if (target == sortedNums[mid]){
            return nums.indexOf(sortedNums[mid])
        }
    }
    return -1
};

/* Find the Duplicate Number 
https://leetcode.com/problems/find-the-duplicate-number/
*/

