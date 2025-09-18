🛠️ What You'll Do In The Long Run 

    Bu### Git Workflow & Commit Management
- **Commit After Features**: After completing any feature implementation or significant patch, ask user if they want to generate commit messages and make commits when necessary
- **Granular Commits**: Break changes into logical sections - commit related changes together, not everything at once
- **Short & Precise Messages**: Commit messages should be concise but not hide important details
- **Section-Based Commits**: Group commits by patches/sections made, so commit messages only reference relevant changes
- **Conventional Commits**: Use conventional commit format when generating commit messages:
  - `feat:` for new features
  - `fix:` for bug fixes  
  - `docs:` for documentation changes
  - `style:` for formatting changes
  - `refactor:` for code refactoring
  - `test:` for adding tests
  - `chore:` for maintenance tasks
  - `config:` for configuration changes
- **AI-Generated Labels**: When AI helps with implementation, include that context in commit messages
- **Clear Descriptions**: Commit messages should clearly describe what was changed and whyures
    Implement the features outlined in your plan. Let AI help with:
        Scaffolding boilerplate or logic
        Writing tests
        Writing docstrings and comments
        Fixing bugs or errors

    Review and Iterate
    Use AI-powered IDE assistants (e.g., CodeRabbit, Cursor, Zed) to:
        Suggest code improvements
        Generate changelogs
        Review code before commits or PRs
        Rewrite unclear logic or comments

    Use Version Control Thoughtfully
        Commit frequently with clear messages
        Label or describe which parts were AI-generated
        Optionally submit one PR using AI-generated summaries

    Final Touches
        Clean up any redundant code
        Add README instructions, usage examples, and screenshots
        Add a short reflection on how AI supported or challenged you

---

## 🎯 SMART CEDI DEVELOPMENT RULES

### Senior Developer Mentoring Approach
- **No Implementation Without Explanation**: Every code decision must be justified with clear reasoning
- **Step-by-Step Learning**: Walk through each implementation with educational context  
- **One Step at a Time**: Complete one todo item fully before moving to the next
- **Feedback-Driven Development**: All major decisions require review and approval before implementation
- **Quality Over Speed**: Take time to understand and explain rather than rushing to completion

### Implementation Process
1. **Proposal Phase**: Present the implementation idea with clear reasoning, explain the problem it solves, justify the chosen approach over alternatives, wait for feedback and approval
2. **Educational Implementation**: Explain each piece of code as it's written, discuss design patterns and best practices, highlight potential pitfalls
3. **Review and Iteration**: Code review with explanation of choices, discuss improvements and alternatives, refactor based on feedback
4. **Git Workflow**: After every feature implementation or patch, ask whether to generate commit messages and make commits when necessary

### Git Workflow & Commit Management
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
