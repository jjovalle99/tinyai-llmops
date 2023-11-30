FROM python:3.11-slim
RUN useradd -m tinyai
USER tinyai
ENV HOME=/home/tinyai \
    PATH=/home/tinyai/.local/bin:$PATH \
    POETRY_VIRTUALENVS_IN_PROJECT=true
WORKDIR /app
COPY --chown=tinyai ./ ./
RUN pip install poetry --no-cache-dir && \
poetry install --only main --no-root --no-cache --no-interaction \
--no-ansi --no-cache
EXPOSE 7860
CMD [ "poetry", "run", "chainlit", "run", "app.py", "--port", "7860"]