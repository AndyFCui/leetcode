class Solution:
    def intToRoman(self, num: int) -> str:
        """
        This is for basic num operate.
        :param num: input
        :return: a string for roman number.
        """
        ones: list[str] = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens: list[str] = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hundreds: list[str] = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thousands: list[str] = ["", "M", "MM", "MMM"]

        return thousands[num // 1000] + hundreds[(num % 1000) // 100] + tens[(num % 100) // 10] + ones[num % 10]