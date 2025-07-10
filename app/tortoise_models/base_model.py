from tortoise import fields


class BaseModel:
    id = fields.BigIntField(primary_key=True)
    created_at = fields.DatetimeField(auto_now_add=True)


# MySQL = primary key 정할 때 주의사항
# MySQL version 8 이상이라면 innodb 가 default engine 이다.
# innodb의 특징 중 하나가 clustering index 라는 기능이 있는데
# primary key 값이 비슷한 row들끼리 Disk(하드디스크) 에서도 모여있다.

# HDD => 랜덤 IO가 느리고, 순차 IO가 빠르다
