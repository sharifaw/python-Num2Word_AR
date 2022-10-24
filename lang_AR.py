def process_arabic_group(self, group_number, group_level,
                             remaining_number):
        tens = Decimal(group_number) % Decimal(100)
        hundreds = Decimal(group_number) / Decimal(100)
        ret_val = ""

        if int(hundreds) > 0:
            if tens == 0 and int(hundreds) == 2:
                ret_val = "{}".format(self.arabicAppendedTwos[0])
            else:
                ret_val = "{}".format(self.arabicHundreds[int(hundreds)]) + " و "  # add missing "و"

        if tens > 0:
            if tens < 20:
                if tens == 2 and int(hundreds) == 0 and group_level > 0:
                    if self.integer_value in [2000, 2000000, 2000000000,
                                              2000000000000, 2000000000000000,
                                              2000000000000000000]:
                        ret_val = "{}".format(
                            self.arabicAppendedTwos[int(group_level)])
                    else:
                        ret_val = "{}".format(
                            self.arabicTwos[int(group_level)])
                else:
                    if ret_val != "":
                        ret_val += " و "

                    if tens == 1 and group_level > 0 and hundreds == 0:
                        ret_val += ""
                    elif (tens == 1 or tens == 2) and (
                            group_level == 0 or group_level == -1) and \
                            hundreds == 0 and remaining_number == 0:
                        ret_val += ""
                    else:
                        ret_val += self.digit_feminine_status(int(tens),
                                                              group_level)
            else:
                ones = tens % 10
                tens = (tens / 10) - 2
                if ones > 0:
                    if ret_val != "" and tens < 4:
                        ret_val += " و "

                    ret_val += self.digit_feminine_status(ones, group_level)
                if ret_val != "" and ones != 0:
                    ret_val += " و "

                ret_val += self.arabicTens[int(tens)]

        return ret_val