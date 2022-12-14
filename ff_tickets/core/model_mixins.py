from enum import Enum


class StrFromFieldsMixin:
    str_fields = ()

    def __str__(self):
        fields = [(str_field, getattr(self, str_field, None)) for str_field in self.str_fields]
        return ', '.join(f'{name}={value}' for (name, value) in fields)


class ChoicesEnumMixin:
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())


class ChoicesEnum(Enum):
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class StoresName(ChoicesEnum):
    F01 = "F01"
    F02 = "F02"
    F03 = "F03"
    F04 = "F04"
    F05 = "F05"
    F06 = "F06"
    F07 = "F07"
    F08 = "F08"
    F09 = "F09"
    F10 = "F10"


class ProblemType(ChoicesEnum):
    scale = 'Везна'
    cash_place = 'Каса'
    cash_place_scale = 'Везна - каса'
    HHT = 'Хенди'
    other = 'Друго'


class ProblemStatusChoice(ChoicesEnum):
    a_posted = 'Подаден'
    b_confirmed = 'Приет'
    c_solved = 'Разрешен'
    d_completed = 'Приключен'
