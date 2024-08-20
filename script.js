nums=[1,2,1,3]
var containsDuplicate = function(nums) {
    var s = new Set(nums);
    console.log(s);
    
    if (s.size !== nums.length) {
        return true;
    } else {
        return false;
    }
}

console.log(containsDuplicate(nums));



