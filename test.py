from pydantic import BaseModel, Field, ValidationError, validator, root_validator


class Tag(BaseModel):
    id: int
    tag: str


class City(BaseModel):
    city_id: int
    name: str = Field(alias='cityFullName')
    # population: int
    # tags: list[Tag]

    @validator('name')
    def name_should_be_spb(cls, v: str) -> str:
        if 'spb' not in v.lower():
            raise ValueError('Work with SPB!')
        return v

    @root_validator
    def print_values(cls, values):
        print('values', values)
        return values


class UserWithoutPassword(BaseModel):
    name: str
    email: str


class User(UserWithoutPassword):
    password: str


input_json = """
{
    "city_id": "12wrerw",
    "name": "Kyiv",
    "population": "2341223"
}
"""

input_json = """
{
    "city_id": "12",
    "name": "Kyiv",
    "tags": [
        {
            "id": 1,
            "tag": "capital"
        },
        {
            "id": 2,
            "tag": "big city"
        }
    ]
}
"""

input_json = """
{
    "city_id": 123,
    "cityFullName": "SpbKyiv"
}
"""

try:
    city = City.parse_raw(input_json)
except ValidationError as e:
    print('Exception', e.json())
else:
    print(city)
    # print(city.name)
    # print(city.tags)
    # print(city.tags[0].tag)
    # print(city.tags[1].tag)
    # print(city.tags[0].json())
    print(city.json(by_alias=True,
                    exclude={'city_id'}))
