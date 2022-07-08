// Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

let nums = [3,1,1,2,1,2];
let target = 3;
let expectedNums = nums.filter((item)=> item !== target);
console.log(expectedNums);