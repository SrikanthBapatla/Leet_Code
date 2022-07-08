// Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.

let nums = [1,1,2,1,2];
let expectedNums = nums.filter((item,index)=> nums.indexOf(item) === index);
console.log(expectedNums);