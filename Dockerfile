FROM python:3.6
WORKDIR /flask_unit_test
COPY . /flask_unit_test
RUN pip install --trusted-host pypi.python.org -r req.txt
CMD ["python", "flask_unit_test.py"]
