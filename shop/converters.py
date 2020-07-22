class FourDigitYearConverter:
    regex = '\d{4}"
    def to_python(self, value): # url로부터추출한문자열을뷰에넘겨주기전에변환
        return int(value)

    def to_url(self, value): # url reverse시에호출
        return "%04d" % value