from pydantic import ConfigDict

# frozen -> 얼어 있다. / 얼어있는 객체 -> 생성 이후 변경할 수 없는 객체
# immutable
FROZEN_CONFIG = ConfigDict(frozen=True)
