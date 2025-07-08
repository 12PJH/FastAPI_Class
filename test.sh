set -eo pipefail  # 코드를 실행하다 실패하면 더 이상 밑으로 진행되지 않고 정지한다.

COLOR_GREEN=$(tput setaf 2) # 터미널 결과 색깔
COLOR_NC=$(tput sgr0) # No color

# Black 실행 후 완료 시 OK 출력
echo "Starting Black"
poetry run black .
echo "OK"

# Ruff 실행 후 완료 시 OK 출력
echo "Starting Ruff"
poetry run ruff check --select I --fix # import 알파벳 순 정렬 실행, I = isort
poetry run ruff check --fix # linter 실행
echo "OK"

# Mypy 실행 후 완료 시 OK 출력
echo "Starting Mypy"
poetry run mypy .
echo "OK"

# Coverage 실행 후 완료 시 OK 출력
echo "Starting Coverage"
poetry run coverage run -m pytest
poetry run coverage report -m
poetry run coverage html
echo "OK"

echo "${COLOR_GREEN}ALL tests passed successfully!!${COLOR_NC}"