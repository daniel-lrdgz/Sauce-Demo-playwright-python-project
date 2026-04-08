# 🧪 SauceDemo Playwright Automation Framework

## 📌 Project Overview

This project is an end-to-end test automation framework built using **Playwright + Python + Pytest**, designed to validate core user flows of the SauceDemo application.

It follows industry best practices such as:

* Page Object Model (POM)
* Reusable fixtures with Pytest
* CI/CD integration with GitHub Actions
* Automated reporting with Allure and HTML reports

---

## 🚀 Tech Stack

* Python 3.12
* Playwright
* Pytest
* Allure Reports
* Pytest-HTML
* GitHub Actions (CI/CD)

---

## 📂 Project Structure

```
playwright-python-project/
│
├── pages/              # Page Object Model classes
├── tests/              # Test cases
├── conftest.py         # Fixtures (setup, login, browser)
├── pytest.ini          # Pytest configuration
├── requirements.txt    # Dependencies
├── .github/workflows/  # CI/CD pipeline
```

---

## 🧪 Test Coverage

The framework automates key user scenarios such as:

* Login (valid & invalid users)
* Add items to cart
* Remove items from cart
* Checkout flow
* Locked user validation

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/daniel-lrdgz/Sauce-Demo-playwright-python-project.git
cd Sauce-Demo-playwright-python-project
```

Install dependencies:

```
pip install -r requirements.txt
playwright install
```

---

## ▶️ Run Tests

```
pytest
```

Run with HTML report:

```
pytest --html=report.html --self-contained-html
```

---

## 📊 Reports

### 🔹 HTML Report

Generated after execution:

```
report.html
```

### 🔹 CI/CD Reports

* Automatically generated in GitHub Actions
* Available as downloadable artifacts

---

## 🔁 CI/CD Integration

This project includes a GitHub Actions pipeline that:

* Installs dependencies
* Runs automated tests
* Generates reports
* Stores artifacts

---

## 💡 Key Features

* Clean Page Object Model architecture
* Reusable and scalable test structure
* Automated execution on every commit
* Integrated reporting for test results

---

## 👨‍💻 Author

Daniel Lepe
QA Automation Engineer (Aspiring)

---

## 📌 Notes

This project was built as part of a hands-on learning roadmap focused on becoming a QA Automation Engineer using modern tools and real-world practices.
