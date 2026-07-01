export function runningSum(nums: number[]): number[] {
  const result: number[] = [];
  let currentSum = 0;

  for (const num of nums) {
    currentSum += num;
    result.push(currentSum);
  }

  return result;
}
