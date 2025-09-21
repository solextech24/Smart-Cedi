# SMART CEDI DEVELOPMENT RULES

## Core Principles
- No implementation without explanation and approval
- One step at a time - complete current todo before next
- Explain reasoning behind every code decision
- Quality over speed

## Implementation Flow
1. Propose solution with reasoning
2. Get approval before coding
3. Implement with educational explanations
4. Ask for commit after each logical section

## Git Workflow & AI Role
- Granular commits by logical sections
- Short, precise commit messages
- Use conventional commits: feat/fix/docs/config/chore
- create feature branches for each task
- **AI Role**: Push feature branches for review only - NO merging
- **Review Authority**: Human developer reviews and merges via GitHub
- Ask before committing after each feature/patch

## Django Standards
- Fat models, thin views
- DRY principle
- Single responsibility
- Clear, documented code

## Communication Style
- Write natural, professional commit messages and documentation
- Avoid AI-generated language patterns
- Sound like an experienced developer, not a bot
- Keep project flow instructions internal - never commit them

1. **Proposal Phase**: Present the implementation idea with clear reasoning, explain the problem it solves, justify the chosen approach over alternatives, wait for feedback and approval
2. **Educational Implementation**: Explain each piece of code as it's written, discuss design patterns and best practices, highlight potential pitfalls
3. **Review and Iteration**: Code review with explanation of choices, discuss improvements and alternatives, refactor based on feedback
4. **Git Workflow**: After every feature implementation or patch, ask whether to generate commit messages and make commits when necessary

### Git Workflow & Commit Management

- **AI Workflow Boundaries**: AI creates feature branches and pushes for review. Human developer has full authority over merging decisions via GitHub pull requests
- **No AI Merging**: AI never merges branches - only commits to feature branches and pushes for review
- **Review Process**: All merges happen through GitHub after human code review and approval
- **Commit After Features**: After completing any feature implementation or significant patch, ask user if they want to generate commit messages and make commits
- **Focused Commits**: Keep commits focused on single features or logical changes
- **Conventional Commits**: Use conventional commit format when generating commit messages:
  - `feat:` for new features
  - `fix:` for bug fixes
  - `docs:` for documentation changes
  - `style:` for formatting changes
  - `refactor:` for code refactoring
  - `test:` for adding tests
  - `chore:` for maintenance tasks
- **AI-Generated Labels**: When AI helps with implementation, include that context in commit messages
- **Clear Descriptions**: Commit messages should clearly describe what was changed and why

### Django Best Practices

- **Fat Models, Thin Views**: Business logic belongs in models
- **DRY Principle**: Don't Repeat Yourself - extract common functionality
- **Single Responsibility**: Each class/function should have one clear purpose
- **Explicit is Better Than Implicit**: Code should be self-documenting

### Learning Objectives

- **Django Fundamentals**: Understanding MVT pattern and Django ORM
- **REST API Design**: Creating well-designed API endpoints
- **Database Design**: Proper relational database modeling
- **Testing Practices**: Writing effective tests
- **AI Integration**: Incorporating AI features effectively
- **Version Control**: Proper Git workflow and commit practices

**Remember**: The goal is not just to build software, but to build understanding and expertise along the way. Every line of code is a learning opportunity.
