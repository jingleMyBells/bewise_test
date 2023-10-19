# bewise_test

alembic upgrade head


хелсчек

  db:
    image: postgres:15
    ports:
      - "5432:5432"
    volumes:
      - database:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5