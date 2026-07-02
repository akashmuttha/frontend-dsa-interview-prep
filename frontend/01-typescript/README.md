# TypeScript Track

TypeScript practice is applied directly to JavaScript exercises, React components and project code.

## Rules

- Keep strict mode in mind.
- Prefer inference when the type is obvious.
- Avoid unnecessary `any`.
- Avoid unnecessary type assertions and non-null assertions.
- Type public boundaries clearly.

## Focus Areas

- Primitives and inference
- Function parameters and return types
- Object types, aliases and interfaces
- Unions, literals and narrowing
- Typed React props, state, events and refs
- Discriminated unions for UI states
- Generics for helpers, hooks and components
- Domain models and API boundaries
- `keyof`, indexed access, mapped types and utility types
- Safe `unknown` error handling

## Practice Outputs

- `concepts/` for type explanations and small examples
- `practice/` for typed implementations and React typing exercises

## Notes Standard

Each TypeScript note should answer:

- What type problem is being solved?
- Where should inference be used?
- Where should explicit types be used?
- How does this prevent invalid states?
- What unsafe types or assertions were avoided?
