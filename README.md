# 💰 Smart Cedi – AI-Powered Personal Finance Tracker

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-v3.9+-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/django-v4.0+-green.svg)](https://djangoproject.com/)

## 🚀 Project Overview

### 🔖 Project Title & Description

**Smart Cedi** is an intelligent personal finance tracker that empowers individuals to take control of their financial future. Beyond traditional expense tracking, Smart Cedi leverages AI to provide personalized investment recommendations, smart savings plans, and predictive financial insights.

**Target Audience:** Young professionals, students, and anyone looking to improve their financial literacy and make data-driven financial decisions.

**Why It Matters:** Financial literacy is crucial for long-term wealth building, yet many people struggle with budgeting and investment decisions. Smart Cedi democratizes financial planning by making AI-powered insights accessible to everyone, regardless of their financial background or experience level.

### ✨ Key Features

- 💳 **Expense & Income Tracking** - Log and categorize all financial transactions
- 📊 **Budget Management** - Set and monitor budgets with real-time alerts
- 🤖 **AI Investment Tips** - Personalized investment recommendations based on your financial profile
- 📈 **Smart Analytics** - Predictive insights into spending patterns and trends
- 💡 **Financial Education** - AI-powered chatbot for financial Q&A
- 🔒 **Secure & Private** - Your financial data stays protected

### 🎯 Planned Features (Roadmap)

- [ ] 📈 Predictive analytics for spending habits
- [ ] 🤖 Advanced chatbot-style financial Q&A
- [ ] 🏦 Bank/API integrations for automated transaction syncing
- [ ] 📱 Mobile app (React Native)
- [ ] 📧 Smart notifications and alerts
- [ ] 🔄 Multi-currency support
- [ ] 📊 Advanced reporting and exports

---

## 🛠️ Tech Stack

### Backend
- **Framework:** Django 4.2+ (Python)
- **Database:** PostgreSQL
- **API:** Django REST Framework
- **Authentication:** Django Auth + JWT

### Frontend
- **Phase 1:** Django Templates + Bootstrap
- **Phase 2:** React.js (planned)

### AI & Machine Learning
- **AI Platform:** OpenAI API / Hugging Face
- **Analytics:** Pandas, NumPy
- **Charts:** Chart.js / D3.js

### DevOps & Deployment
- **Version Control:** Git + GitHub
- **CI/CD:** GitHub Actions
- **Deployment:** Docker + Render/Railway
- **Monitoring:** Sentry (planned)

---

## 🤖 AI-Powered Features (Product-Level)

### 1. **Smart Investment Recommendations**
- Analyze user spending patterns and income to suggest optimal investment strategies
- Provide personalized investment suggestions based on risk tolerance and financial goals
- Risk assessment and portfolio optimization recommendations

### 2. **Predictive Analytics**
- Forecast future expenses based on historical spending data
- Identify spending trends, seasonal patterns, and anomalies
- Budget optimization and cash flow predictions

### 3. **Financial Education Chatbot**
- Interactive AI assistant to answer personal finance questions
- Provide educational content and personalized financial tips
- Guide users through financial planning processes

### 4. **Automated Transaction Categorization**
- AI-powered automatic categorization of expenses and income
- Machine learning from user corrections to improve accuracy
- Smart tagging and transaction organization

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- PostgreSQL 12+
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/solextech24/Smart-Penny.git
   cd Smart-Penny
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment setup**
   ```bash
   cp .env.example .env
   # Edit .env with your database and API keys
   ```

5. **Database setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

Visit `http://localhost:8000` to access Smart Cedi!

---

## 📁 Project Structure

```
Smart-Penny/
├── apps/
│   ├── accounts/          # User authentication & profiles
│   ├── transactions/      # Income & expense tracking
│   ├── budgets/          # Budget management
│   ├── ai_insights/      # AI recommendations & tips
│   └── analytics/        # Reports & analytics
├── config/               # Django settings
├── static/              # CSS, JS, images
├── templates/           # HTML templates
├── requirements.txt     # Python dependencies
├── manage.py           # Django management script
└── README.md           # This file
```

---

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

Run with coverage:
```bash
coverage run --source='.' manage.py test
coverage report
coverage html  # Generate HTML coverage report
```

---

## � AI Integration Strategy

This project leverages AI tools throughout the entire development lifecycle to enhance productivity, code quality, and feature development. Here's our comprehensive AI-powered development approach:

### 🔧 Code Generation & Scaffolding

**IDE Integration:**
- **Cursor AI & GitHub Copilot:** Used for intelligent code completion, function generation, and boilerplate scaffolding
- **ChatGPT/Claude:** For architectural decisions and complex feature planning

**Scaffolding Strategy:**
```
Prompt Example: "Generate a complete Django app structure for expense tracking with:
- Models: Transaction, Category, Budget
- Views: CRUD operations with proper permissions
- Serializers: DRF serializers with validation
- URLs: RESTful routing patterns
- Tests: Unit tests for all components"
```

**Feature Development Workflow:**
1. **Requirements Analysis:** Use AI to break down user stories into technical tasks
2. **Model Design:** Generate Django models with proper relationships and validations
3. **API Development:** Auto-generate DRF viewsets, serializers, and URL patterns
4. **Frontend Components:** Scaffold React components and Django templates
5. **Business Logic:** Generate utility functions and service classes

### 🧪 Testing Strategy

**AI-Powered Test Generation:**

**Unit Testing:**
```
Prompt: "Generate comprehensive unit tests for the Budget model including:
- Field validation tests (negative amounts, required fields)
- Method testing (budget_remaining, is_over_budget)
- Edge cases (zero budget, null categories)
- Database constraint testing"
```

**Integration Testing:**
```
Prompt: "Create integration tests for the expense tracking workflow:
- User authentication flow
- Creating expense with category assignment
- Budget update after expense creation
- API response validation
- Error handling scenarios"
```

**Test Automation Tools:**
- **Pytest-Django:** AI-generated test fixtures and parameterized tests
- **Factory Boy:** AI-assisted factory creation for test data
- **Coverage.py:** AI analysis of coverage reports for test gap identification

### � Documentation Strategy

**AI-Powered Documentation:**

**Code Documentation:**
```
Prompt: "Generate comprehensive docstrings for this Django view class following Google style:
- Class description with purpose and usage
- Method descriptions with parameters and return types
- Example usage and error conditions
- API endpoint documentation"
```

**README & Wiki Maintenance:**
- **Automated Updates:** AI reviews code changes and suggests README updates
- **API Documentation:** Auto-generate OpenAPI specs from Django REST Framework
- **Tutorial Creation:** AI-generated step-by-step guides for common workflows

**Documentation Workflow:**
1. **Code Comments:** AI generates inline comments for complex logic
2. **Function Docstrings:** Comprehensive parameter and return value documentation
3. **Module Documentation:** High-level overview and usage examples
4. **API Docs:** Auto-generated from code annotations and comments

### 🔍 Context-Aware Development Techniques

**Feeding Context to AI:**

**1. API Specification Integration:**
```bash
# Example workflow for external API integration
curl -s https://api.example.com/openapi.json | \
jq . > external_api_spec.json

# AI Prompt:
"Based on this OpenAPI specification, generate Django service classes 
to integrate with the external banking API, including error handling, 
authentication, and response parsing."
```

**2. File Tree Analysis:**
```
# Generate project structure context
tree -I '__pycache__|*.pyc|venv' > project_structure.txt

# AI Prompt:
"Based on this Django project structure, suggest where to implement 
the new AI recommendation engine and what files need to be created 
or modified."
```

**3. Git Diff Integration:**
```bash
# Get recent changes for context
git diff HEAD~5..HEAD > recent_changes.diff

# AI Prompt:
"Analyze these recent changes and generate appropriate unit tests 
for the modified functions, ensuring compatibility with existing code."
```

**4. Database Schema Context:**
```bash
# Export current schema
python manage.py inspectdb > current_schema.py

# AI Prompt:
"Based on this Django model schema, generate migration scripts to add 
AI recommendation fields while maintaining data integrity."
```

**Advanced Context Techniques:**

**Codebase Understanding:**
- **Semantic Search:** Use AI to understand code relationships across files
- **Architecture Analysis:** AI reviews entire codebase for patterns and anti-patterns
- **Dependency Mapping:** AI tracks how changes affect related components

**Real-time Development:**
```
Workflow Example:
1. Developer modifies Transaction model
2. AI analyzes the change and its impact
3. AI suggests necessary updates to:
   - Related serializers
   - Test files
   - API documentation
   - Migration scripts
4. AI generates the required code changes
```

**AI Development Tools Used:**
- **GitHub Copilot Labs:** Advanced code explanation and test generation
- **Cursor AI:** Context-aware code completion and refactoring
- **CodeRabbit:** AI-powered code reviews with security and performance insights
- **ChatGPT Code Interpreter:** Complex algorithm development and optimization
- **Claude:** Architecture decisions and system design discussions

**Quality Assurance with AI:**
- **Code Review:** AI analyzes pull requests for bugs, security issues, and best practices
- **Performance Analysis:** AI identifies potential bottlenecks and optimization opportunities
- **Security Scanning:** AI reviews code for common vulnerabilities and suggests fixes
- **Refactoring Suggestions:** AI recommends code improvements and modernization

This comprehensive AI integration strategy ensures rapid development while maintaining high code quality, thorough testing, and excellent documentation throughout the project lifecycle.

---

## 📊 API Documentation

### Authentication
All API endpoints require authentication using JWT tokens.

### Endpoints

**Transactions**
- `GET /api/transactions/` - List all transactions
- `POST /api/transactions/` - Create new transaction
- `GET /api/transactions/{id}/` - Get transaction details
- `PUT/PATCH /api/transactions/{id}/` - Update transaction
- `DELETE /api/transactions/{id}/` - Delete transaction

**Budgets**
- `GET /api/budgets/` - List all budgets
- `POST /api/budgets/` - Create new budget
- `GET /api/budgets/{id}/status/` - Get budget status

**AI Insights**
- `GET /api/ai/investment-tips/` - Get personalized investment tips
- `GET /api/ai/spending-analysis/` - Get spending pattern analysis
- `POST /api/ai/chat/` - Chat with financial advisor bot

---

## 🚀 Deployment

### Using Docker

1. **Build the image**
   ```bash
   docker build -t smart-penny .
   ```

2. **Run with docker-compose**
   ```bash
   docker-compose up -d
   ```

### Environment Variables

```env
DEBUG=False
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:password@localhost/smartpenny
OPENAI_API_KEY=your-openai-api-key
ALLOWED_HOSTS=your-domain.com
```

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

### Code Style

- Follow PEP 8 for Python code
- Use Black for code formatting: `black .`
- Run flake8 for linting: `flake8 .`
- Write meaningful commit messages

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Support & Contact

- **GitHub Issues:** [Report bugs or request features](https://github.com/solextech24/Smart-Penny/issues)
- **Email:** support@smartpenny.app
- **Documentation:** [Wiki](https://github.com/solextech24/Smart-Penny/wiki)

---

## 🙏 Acknowledgments

- Thanks to all contributors who help make Smart Cedi better
- OpenAI for providing AI capabilities
- Django community for the amazing framework
- All users who provide feedback and suggestions

---

**Made with ❤️ by the Smart Cedi Team**
