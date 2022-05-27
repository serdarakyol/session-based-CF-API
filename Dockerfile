FROM python:3.9.7

COPY ./requirements.txt /api/requirements.txt
COPY ./cf_api /api/cf_api
COPY ./.env /api/.env

WORKDIR /api

RUN python -m venv /api/venv
# Enable venv
ENV PATH="/api/venv/bin:$PATH"

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uvicorn", "cf_api.main:app", "--host", "0.0.0.0", "--port", "1234"]