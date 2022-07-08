// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

var twoSum = function(nums, target) {
    
    let comp = new Map();
    let len = nums.length;
    
    for(let i=0; i< len; i++){
        let num1= nums[i];
        let num2= target - num1;
        if(comp.has(num2)){
            return[i,comp.get(num2)];
        }
        comp.set(num1,i);

    }
    
};

let nums = [2,7,11,15];
let target = 9;
console.log(twoSum(nums,target));
