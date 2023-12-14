import validators


def is_valid_phone_number(match: str) -> bool:
    pass


def is_valid_id_number(match: str) -> bool:
    """All Turkish IDs are even, and the sum of the first 10 digits mod 10 is the 11th digit.

    DISCLAIMER: Only checks a given id number's possibility to be a valid one. As it is impossible for this program
    to perform checks for validity using a legit and legal database of Turkish ID numbers.


    Args:
        match (str): a matched string for one of the corresponding patterns of regex

    Returns:
        bool: whether or not the id adheres to the implemented rules
    """
    # check for foreign ids starting with "99"
    if match[:2] == "99":
        return True
    sum_ = 0
    for digit in match[:10]:
        sum_ += int(digit)

    if sum_ % 10 == int(match[10]) and int(match[10]) % 2 == 0:
        return True


def is_valid_cc_number(match: str) -> bool:
    """Checks a sequence of 14+ digits with the Luhn's algorithm for validity. MasterCard,
    American Express (AMEX), Visa and all credit cards use Luhn. It is intended as a protection
    against accidental errors, not malicious attacks.
    A side note, the algorithm does not allow the detection of certain permutations of digits.
    (i.e. any number containing a 0 replaced by a 9 and a 9 replaced by a 0 has an identical checksum and more...)

    Args:
        match (str): a matched string for one of the corresponding patterns of regex

    Returns:
        bool: whether or not the cc adheres to the implemented rules
    """
    match = match[::-1]
    sum_ = 0
    for i in range(len(match)):
        # double each odd ranked digit (by index)
        if i % 2 == 1:
            temp = int(match[i]) * 2
            if len(str(temp)) > 1:
                temp_list = list(map(int, str(temp)))
                temp = sum(temp_list)
        else:
            temp = int(match[i])

        sum_ += temp

    if sum_ % 10 == 0:
        return True
    else:
        return False


def is_valid_plate_id(match: str) -> bool:
    """
    Checks if a captured possible plate id is of the exact forms below:
    "99 X 9999", "99 X 99999"
    "99 XX 999", "99 XX 9999"
    "99 XXX 99", "99 XXX 999"

    DISCLAIMER: Does not check if the plate id actually exists. Only checks if the plate id is of appropriate form,
    according to Turkish standards.

    Args:
        match (str): a matched string for one of the corresponding patterns of regex

    Returns:
        bool: whether or not the plate id is of the appropriate form
    """
    masks = [
        [True, True, False, True, True, True, True],
        [True, True, False, True, True, True, True, True],
        [True, True, False, False, True, True, True],
        [True, True, False, False, True, True, True, True],
        [True, True, False, False, False, True, True],
        [True, True, False, False, False, True, True, True],
    ]
    # remove any hyphens, dots or spaces from the match
    new_match_list = list(match.replace("-", "").replace(".", "").replace(" ", ""))

    match_mask = [ch.isnumeric() for ch in new_match_list]

    if match_mask in masks:
        return True
    else:
        return False


def is_valid_email(match: str) -> bool:
    return validators.email(match)


def is_valid_domain(match: str) -> bool:
    return validators.domain(match)


def is_valid_url(match: str) -> bool:
    return validators.url
