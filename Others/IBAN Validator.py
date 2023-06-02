
class IBANValidator:
    def __init__(self, use_nordea_extensions=False, include_countries=None):
        iban = input("Enter IBAN: ")
        self.__iban = iban.replace(" ", "")
        self.__country_code = self.__iban[:2]
        self.__iban_length = {'AL': 28,  # Albania
                            'AD': 24,  # Andorra
                            'AE': 23,  # United Arab Emirates
                            'AT': 20,  # Austria
                            'AZ': 28,  # Azerbaijan
                            'BA': 20,  # Bosnia and Herzegovina
                            'BE': 16,  # Belgium
                            'BG': 22,  # Bulgaria
                            'BH': 22,  # Bahrain
                            'BR': 29,  # Brazil
                            'CH': 21,  # Switzerland
                            'CR': 21,  # Costa Rica
                            'CY': 28,  # Cyprus
                            'CZ': 24,  # Czech Republic
                            'DE': 22,  # Germany
                            'DK': 18,  # Denmark
                            'DO': 28,  # Dominican Republic
                            'EE': 20,  # Estonia
                            'ES': 24,  # Spain
                            'FI': 18,  # Finland
                            'FO': 18,  # Faroe Islands
                            'FR': 27,  # France
                            'GB': 22,  # United Kingdom + Guernsey, Isle of Man, Jersey
                            'GE': 22,  # Georgia
                            'GI': 23,  # Gibraltar
                            'GL': 18,  # Greenland
                            'GR': 27,  # Greece
                            'GT': 28,  # Guatemala
                            'HR': 21,  # Croatia
                            'HU': 28,  # Hungary
                            'IE': 22,  # Ireland
                            'IL': 23,  # Israel
                            'IS': 26,  # Iceland
                            'IT': 27,  # Italy
                            'JO': 30,  # Jordan
                            'KZ': 20,  # Kazakhstan
                            'KW': 30,  # Kuwait
                            'LB': 28,  # Lebanon
                            'LI': 21,  # Liechtenstein
                            'LT': 20,  # Lithuania
                            'LU': 20,  # Luxembourg
                            'LV': 21,  # Latvia
                            'MC': 27,  # Monaco
                            'MD': 24,  # Moldova
                            'ME': 22,  # Montenegro
                            'MK': 19,  # Macedonia
                            'MT': 31,  # Malta
                            'MR': 27,  # Mauritania
                            'MU': 30,  # Mauritius
                            'NL': 18,  # Netherlands
                            'NO': 15,  # Norway
                            'PS': 29,  # Palestine
                            'PK': 24,  # Pakistan
                            'PL': 28,  # Poland
                            'PT': 25,  # Portugal + Sao Tome and Principe
                            'QA': 29,  # Qatar
                            'RO': 24,  # Romania
                            'RS': 22,  # Serbia
                            'SA': 24,  # Saudi Arabia
                            'SE': 24,  # Sweden
                            'SI': 19,  # Slovenia
                            'SK': 24,  # Slovakia
                            'SM': 27,  # San Marino
                            'TN': 24,  # Tunisia
                            'TR': 26,  # Turkey
                            'VG': 24}  # British Virgin Islands
      
        if use_nordea_extensions:
            self.__iban_length.update({'AO': 25,  # Angola
                                       'BJ': 28,  # Benin
                                       'BF': 27,  # Burkina Faso
                                       'BI': 16,  # Burundi
                                       'CI': 28,  # Ivory Coast
                                       'CG': 27,  # Congo
                                       'CM': 27,  # Cameroon
                                       'CV': 25,  # Cape Verde
                                       'DZ': 24,  # Algeria
                                       'EG': 27,  # Egypt
                                       'GA': 27,  # Gabon
                                       'IR': 26,  # Iran
                                       'MG': 27,  # Madagascar
                                       'ML': 28,  # Mali
                                       'MZ': 25,  # Mozambique
                                       'UA': 29,  # Ukraine
                                       'SN': 28}  # Senegal
                                       )
        self.__include_countries = include_countries
        if self.__include_countries:
            for country_code in include_countries:
                if country_code not in self.__iban_length:
                    raise ValueError(f'Explicitly requested country code {country_code} is not part of the configured IBAN validation set.')

    def __is_valid(self):
        if not self.__iban.isalnum():
            return False, "You have entered invalid characters."
        elif self.__country_code not in self.__iban_length:
            return False, "Invalid country code."
        elif len(self.__iban) != self.__iban_length[self.__country_code]:
            return False, f"Invalid IBAN length for {self.__country_code}."
        else:
            iban = (self.__iban[4:] + self.__iban[0:4]).upper()
            iban2 = ""
            for ch in iban:
                if ch.isdigit():
                    iban2 += ch
                else:
                    iban2 += str(10 + ord(ch) - ord('A'))
            iban = int(iban2)
            if iban % 97 == 1:
                return True, "IBAN entered is valid."
            else:
                return False, "IBAN entered is invalid."

    def is_valid(self):
        return self.__is_valid()

    def __run(self):
        is_valid, message = self.__is_valid()
        print(message)

    def run(self):
        return self.__run()


if __name__ == "__main__":
    iban_check = IBANValidator()
    iban_check.run()




# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# An IBAN-compliant account number consists of:
#   • a two-letter country code taken from the ISO 3166-1 standard (e.g., FR for France, GB for Great Britain, DE for Germany, and so on)
#   • two check digits used to perform the validity checks - fast and simple, but not fully reliable, tests, showing whether a number is invalid
#     (distorted by a typo) or seems to be good;
#   • the actual account number (up to 30 alphanumeric characters - the length of that part depends on the country)

# The standard says that validation requires the following steps (according to Wikipedia):
#   • (step 1) Check that the total IBAN length is correct as per the country (this program won't do that, but you can modify the code to meet
#     this requirement if you wish; note: you have to teach the code all the lengths used in Europe)
#   • (step 2) Move the four initial characters to the end of the string (i.e., the country code and the check digits)
#   • (step 3) Replace each letter in the string with two digits, thereby expanding the string, where A = 10, B = 11 ... Z = 35;
#   • (step 4) Interpret the string as a decimal integer and compute the remainder of that number on division by 97; If the remainder is 1,
#     the check digit test is passed and the IBAN might be valid.


iban = input("Enter IBAN, please: ")    # ask the user to enter the IBAN (the number can contain spaces, as they significantly improve number readability...
iban = iban.replace(" ","")             # ...but remove them immediately)

if not iban.isalnum():                              # the entered IBAN must consist of digits and letters only - if it doesn't...
    print("You have entered invalid characters.")   # ...output the message;
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:                                         # start the actual processing;
    iban = (iban[4:] + iban[0:4]).upper()     # move the four initial characters to the number's end, and convert all letters to upper case (step 02 of the algorithm)
    iban2 = ""                                # Variable to store a modified version of the IBAN string in which certain characters will later be replaced with numbers.
    for ch in iban:         # iterate through the IBAN;
        if ch.isdigit():    # if the character is a digit...
            iban2 += ch     # just copy it;
        else:
            iban2 += str(10 + ord(ch) - ord('A'))   # The ord function returns the Unicode code point of a single character, so ord(ch) returns the code point of ch. Subtracting the code point of 'A' (the ASCII code point of 'A' is 65) from this result gives the number of characters between 'A' and ch. Adding 10 to this result gives a unique two-digit number for each character in the range of 'A' to 'Z'. Finally, the resulting number is converted to a string using str and appended to the iban2 string.
    iban = int(iban2)                               # the converted form of the IBAN is ready - make an integer out of it;
    if iban % 97 == 1:                              # is the remainder of the division of iban2 by 97 equal to 1?
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")


# Let's add some test data (all these numbers are valid - you can invalidate them by changing any character).
# • British: GB72 HBZU 7006 7212 1253 00
# • French: FR76 30003 03620 00020216907 50
# • German: DE02100100100152517108
# If you are an EU resident, you can use you own account number for tests.
