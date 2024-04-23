FROM python:3.11-bullseye AS build

WORKDIR /backend

COPY requirements.txt /backend/requirements.txt
RUN python -m pip install -r requirements.txt
COPY . /backend
RUN chmod +x /backend/docker-entrypoint.sh /backend/docker-cmd.sh

FROM python:3.11.9-slim-bullseye

WORKDIR /backend

COPY --from=build --chown=nonroot:nonroot /backend /backend
COPY --from=build --chown=nonroot:nonroot /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=build --chown=nonroot:nonroot /usr/local/bin /usr/local/bin

ENV PYTHONPATH=/usr/local/lib/python3.11/site-packages
ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["/backend/docker-entrypoint.sh"]
CMD ["/backend/docker-cmd.sh"]