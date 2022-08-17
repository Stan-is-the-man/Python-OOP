class Validator:

    @staticmethod
    def raise_if_num_is_not_in_range(number, min_number, max_number, message):
        if number < min_number or number > max_number:
            raise ValueError(message)
