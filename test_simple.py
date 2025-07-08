# def add(a:int, b:int) -> int:
#     return a+b
#
# def test_add() -> None:
#     # Given 무언가 주어졌을 때
#     # 버그는 "경계"를 좋아한다. int의 경우 -1,0,1
#     a, b = 1, 1
#
#     # When : 테스트 대상이 되는 함수 호출
#     result = add(a, b) # result의 타입은 int
#
#     # Then : 테스트의 결과값을 반환
#     assert result == 2

# - 택배는 2영업일 이후에 도착합니다. 월요일부터 토요일까지가 영업일입니다.
# - 단순화를 위해 “도서산간지역”은 고려하지 않습니다.
# - 단순화를 위해 설날, 추석 등의 공휴일은 고려하지 않습니다.

# from datetime import datetime, timedelta
#
# DELIVERY_DAYS = 2
#
# def _is_holiday(day:datetime) -> bool:
#     return day.weekday() > 5
#
# def get_eta(purchase_date: datetime) -> datetime:
#     current_date = purchase_date
#     remaining_date = DELIVERY_DAYS
#
#     while remaining_date > 0:
#         current_date += timedelta(days=1)
#         if not _is_holiday(current_date):
#             remaining_date -= 1
#
#     return current_date
#
#
# def test_get_eta_2023_12_01() -> None:
#     result = get_eta(datetime(2023,12,1))
#     assert result == datetime(2023,12,4)
#
#
# def test_get_eta_2023_12_31() -> None:
#     result = get_eta(datetime(2024, 12, 31))
#     assert result == datetime(2025, 1, 2)
#
#
# def test_get_eta_2024_02_28() -> None:
#     result = get_eta(datetime(2024, 2, 28))
#     assert result == datetime(2024, 3, 1)
#
# def test_get_eta_2023_02_28() -> None:
#     result = get_eta(datetime(2023, 2, 28))
#     assert result == datetime(2023, 3, 2)
#
# def test_get_eta_2024_01_12() -> None:
#     result = get_eta(datetime(2024, 1, 12))
#     assert result == datetime(2024, 1, 15)
