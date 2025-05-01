FROM python:3.13-alpine
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
# Run tests if TEST_MODE environment variable is set
RUN if [ "$TEST_MODE" = "true" ] ; then pytest ; fi
CMD ["python", "run-docker.py"]