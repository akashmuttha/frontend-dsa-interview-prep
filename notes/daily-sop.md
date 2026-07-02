# Daily SOP

This is the daily operating procedure for keeping study, practice and GitHub progress connected.

## Daily Goal

Make one small, real improvement.

The repo should grow through solved problems, notes, utilities, frontend exercises or project work. Do not commit noise only to keep activity alive.

## Morning Flow

### 1. Start With Status

```bash
git status
```

Purpose:

- Check whether yesterday left unfinished changes.
- Avoid starting new work on top of unknown files.

### 2. Pick One Primary Task

Choose only one main task:

- Solve one DSA problem
- Revise one DSA pattern
- Implement one JavaScript utility
- Write one TypeScript concept example
- Build one React component or hook
- Improve one machine-coding/project folder

### 3. Work In The Correct Folder

DSA:

```text
dsa/leetcode-inbox/                 New LeetCode extension files
dsa/00-foundations/                 Foundation pattern problems
dsa/01-data-structures/             Data-structure problems
dsa/02-dp-backtracking/             DP and backtracking
dsa/03-interview-revision/          Revision and timed practice
```

Frontend:

```text
frontend/00-javascript/             JS concepts and utilities
frontend/01-typescript/             TS concepts and typed examples
frontend/02-react/                  React concepts, hooks and patterns
frontend/03-machine-coding/         Interview-style frontend exercises
frontend/04-projects/               Larger projects
```

### 4. Produce A Small Artifact

Every session should create or improve at least one of these:

- `solution.py`
- `notes.md`
- concept note
- utility implementation
- component example
- project README
- test case
- progress update

### 5. Write Notes Before Moving On

For DSA, answer:

- What pattern is this?
- What was the mental trigger?
- What edge case mattered?
- What mistake should be avoided next time?

For frontend, answer:

- What concept did this practice?
- What was tricky?
- What would make this production-ready?

### 6. Check Changes

```bash
git status
git diff
```

Purpose:

- See what changed.
- Avoid committing accidental files.

### 7. Commit Only Meaningful Work

```bash
git add <files>
git commit -m "Clear message"
git push
```

Good commit messages:

```text
Add two sum notes
Solve running sum in Python
Implement debounce utility
Add typed form example
Build autocomplete input shell
Update frontend progress
```

Avoid vague messages:

```text
update
changes
work
misc
```

## LeetCode Workflow

1. Open problem using the LeetCode extension.
2. Solve in `dsa/leetcode-inbox/`.
3. After solving, create or update the polished folder under the right pattern.
4. Commit the polished folder.
5. Do not commit empty starter files unless they are part of active work.

Example:

```text
dsa/leetcode-inbox/1-two-sum.py
```

Becomes:

```text
dsa/00-foundations/hashmaps/two-sum/
  problem.md
  solution.py
  notes.md
```

## Minimum Day

When time or energy is low:

- Re-read one old note.
- Re-solve one easy problem or one utility.
- Commit only if something meaningful changed.

No fake commits.

## Weekly Review

At the end of the week, update:

```text
dsa/progress.md
frontend/progress.md
notes/weekly-reviews/
```

Review:

- What was solved?
- What was learned?
- What pattern or concept is still weak?
- What should be repeated next week?
