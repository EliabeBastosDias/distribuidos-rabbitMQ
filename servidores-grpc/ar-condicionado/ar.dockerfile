FROM python:3.10

WORKDIR /app

COPY . /app

RUN rm -rf myenv __pycache__ && \
    python -m venv myenv && \
    /bin/bash -c "source myenv/bin/activate" && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["python3", "main.py"]
