# Flask Teaching App - CI/CD Pipeline

This is a simple Flask application designed for teaching Git, Docker, and CI/CD concepts with GitHub Actions.

## Application Structure

- `app.py` - Main Flask application with simple endpoints
- `test_app.py` - PyTest test suite for the application
- `dockerfile` - Docker container configuration
- `requierments.txt` - Python dependencies
- `.github/workflows/ci.yml` - CI/CD pipeline configuration

## Endpoints

- `/` - Hello endpoint
- `/bye` - Goodbye endpoint  
- `/hau` - How are you endpoint

## Basic CI Pipeline

Our GitHub Actions workflow includes 1 simple job:

### Testing (`test`)
- Checks out the code
- Sets up Python 3.11
- Installs dependencies (Flask + pytest)
- Runs the test suite

## Workflow Triggers

The CI pipeline runs on:
- **All pushes** to any branch
- **All pull requests**

## Running Locally

### Prerequisites
- Python 3.9+
- Docker (optional)

### Setup
```bash
pip install -r requierments.txt
```

### Run the application
```bash
python app.py
```

### Run tests
```bash
pip install pytest pytest-cov
pytest
```



### Build and run with Docker
```bash
docker build -t flask-teaching-app .
docker run -p 5000:5000 flask-teaching-app
```

## Teaching Concepts Demonstrated

1. **Basic CI**: Automated testing on every code change
2. **GitHub Actions**: Workflow syntax and basic steps  
3. **Testing**: Unit tests with pytest
4. **Git Integration**: Triggering builds on push/PR

## Core CI Concepts Taught

- **What is CI?**: Continuous Integration = automatic testing
- **When does it run?**: On every push and pull request
- **What does it do?**: Checkout → Setup → Install → Test
- **Why is it useful?**: Catch bugs early, ensure code quality

## Next Steps for Students

1. **Add more tests** - increase test coverage
2. **Add linting** - code quality checks (flake8, black)
3. **Add multiple Python versions** - matrix builds
4. **Add Docker testing** - test containerized app
5. **Add deployment** - deploy to staging/production
6. **Add security scanning** - check for vulnerabilities
