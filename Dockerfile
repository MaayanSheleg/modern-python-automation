# 1.We will use Playwright's ready-made infrastructure (including Python and browsers)
FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

# 2. We will define the working folder inside the container
WORKDIR /app

# 3. We will copy the requirements file and install them.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. We will copy all our code into the container.
COPY . .

# 5. The command that will run when the container starts - running the tests!
CMD ["pytest"]