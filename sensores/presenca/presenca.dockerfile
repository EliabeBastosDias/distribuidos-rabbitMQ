FROM python:3.10

WORKDIR /app

COPY . /app

RUN python -m venv myenv
RUN /bin/bash -c "source myenv/bin/activate"

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python3", "main.py"]
