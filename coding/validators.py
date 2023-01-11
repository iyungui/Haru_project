import string
from django.core.exceptions import ValidationError


# 닉네임에 특수문자를 포함시키지 않도록 유효성 검사
def contains_special_character(value):
    for char in value:
        if char in string.punctuation:
            return True
    return False


# 문자열에 영문 대문자가 있는지
def contains_uppercase_letter(value):
    for char in value:
        if char.isupper(): # char가 대문자라면
            return True
    # 영문 대문자가 하나도 없다면
    return False


# 문자열에 영문 소문자가 있는지
def contains_lowercase_letter(value):
    for char in value:
        if char.islower():
            return True
    return False


# 숫자를 포함하는지
def contains_number(value):
    for char in value:
        if char.isdigit():
            return True
    return False


# 비밀번호 유효성 검사
class CustomPasswordValidator:
    def validate(self, password, user=None):
        if (
                len(password) < 8 or
                not contains_uppercase_letter(password) or
                not contains_lowercase_letter(password) or
                not contains_number(password) or
                not contains_special_character(password)
        ):
            raise ValidationError("8자 이상의 영문 대/소문자, 숫자, 특수문자 조합이어야 합니다.")

    def get_help_text(self):
        return "8자 이상의 영문 대/소문자, 숫자, 특수문자 조합을 입력해 주세요."


def validate_no_special_characters(value):
    if contains_special_character(value):
        raise ValidationError("특수문자를 포함할 수 없습니다.")