# Two Sum

## Pattern

Hash map lookup.

## Mental Trigger

Need to find a pair where current value plus some previous value equals the target.

## Approach

For each number, calculate the complement needed to reach the target.
If the complement was already seen, return its index and the current index.
Otherwise store the current number and index.

## Complexity

Time: `O(n)`

Space: `O(n)`

## Mistakes To Avoid

- Do not use the same index twice.
- Check the complement before storing the current number.
- Store index as the value, not just the number.
