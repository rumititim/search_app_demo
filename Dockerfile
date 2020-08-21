FROM python:3.6
RUN python -m venv env
ENV PATH /env/bin:$PATH

COPY config/requirements /app/requirements
RUN /env/bin/pip install --upgrade pip && /env/bin/pip install -r /app/requirements
ADD . /app
