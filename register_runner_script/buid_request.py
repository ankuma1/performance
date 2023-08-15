# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = welcome9_from_dict(json.loads(json_string))

from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class register:
    city_id: int
    first_name: str
    hiring_source: str
    last_name: str
    phone: str

    def __init__(self, city_id: int, first_name: str, hiring_source: str, last_name: str, phone: str) -> None:
        self.city_id = city_id
        self.first_name = first_name
        self.hiring_source = hiring_source
        self.last_name = last_name
        self.phone = phone

    @staticmethod
    def from_dict(obj: Any) -> 'register':
        assert isinstance(obj, dict)
        city_id = from_int(obj.get("city_id"))
        first_name = from_str(obj.get("first_name"))
        hiring_source = from_str(obj.get("hiringSource"))
        last_name = from_str(obj.get("last_name"))
        phone = from_str(obj.get("phone"))
        return register(city_id, first_name, hiring_source, last_name, phone)

    def to_dict(self) -> dict:
        result: dict = {}
        result["city_id"] = from_int(self.city_id)
        result["first_name"] = from_str(self.first_name)
        result["hiringSource"] = from_str(self.hiring_source)
        result["last_name"] = from_str(self.last_name)
        result["phone"] = from_str(self.phone)
        return result


def register_from_dict(s: Any) -> register:
    return register.from_dict(s)


def register_to_dict(x: register) -> Any:
    return to_class(register, x)
