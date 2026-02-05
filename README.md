🚀 Playwright Automation Framework
A high-performance automated testing suite leveraging Python, Playwright, and Docker. This project demonstrates a unified approach to testing by combining UI and API validation within a single, scalable architecture.

🏗️ Architecture & Design Patterns
The framework is built with scalability and maintainability in mind, utilizing two core design patterns:

Page Object Model (POM): For UI testing, ensuring that page elements and actions are decoupled from the test logic.

Service Object Model: For API testing, wrapping endpoints into reusable service classes to handle requests and schema validation efficiently.

🛠️ Tech Stack
Language: Python 3.x

Test Runner: Pytest

Automation: Playwright

Containerization: Docker

Reporting: Allure / Playwright HTML Report

🐳 Getting Started with Docker
The easiest way to run the tests without worrying about local dependencies or browser binaries is via Docker.

1. Build the Image
Bash
docker build -t playwright-tests .
2. Run All Tests
Bash
docker run --rm playwright-tests
3. Run Specific Test Suites
Bash
# Run only UI tests
docker run --rm playwright-tests pytest tests/ui

# Run only API tests
docker run --rm playwright-tests pytest tests/api
📊 Reporting
After the test execution, the framework generates a comprehensive HTML Report. These reports provide:

Step-by-step execution logs.

Visual Traces: Detailed snapshots of the UI at every action.

Video Recordings: (Optional) Captured for failed test cases.

API Payloads: Full request/response visibility for debugging.

Note: To view the report locally after a Docker run, ensure you mount a volume to your host machine: docker run --rm -v $(pwd)/reports:/app/playwright-report playwright-tests

📁 Project Structure
Plaintext
├── src/
│   ├── pages/          # Page Object classes
│   └── services/       # API Service Object classes
├── tests/
│   ├── ui/             # UI test scripts
│   └── api/            # API test scripts
├── playwright-report/  # Generated HTML reports
├── Dockerfile
└── pytest.ini