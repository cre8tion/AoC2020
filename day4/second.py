import re

def validate_passports_with_data():
    with open('input.txt') as fin:
        input_list = fin.readlines()
        text_lst = [i.replace("\n", "") for i in input_list]

        required_fields = ["byr","iyr","eyr","hgt","hcl", "ecl","pid"]
        
        passport_list = []
        temp_list = []

        for i in range(len(text_lst)):
            if text_lst[i] != "":
                temp_list.append(text_lst[i])
            else:
                if len(temp_list) > 0:
                    passport_list.append(temp_list)
                    temp_list = []
        
        passport_field_list = []

        for i in range(len(passport_list)):
            temp_field_list = []
            for j in range(len(passport_list[i])):
                temp_list = passport_list[i][j].split(" ")
                temp_field_list += temp_list
            passport_field_list.append(temp_field_list)
        
        valid_passports = 0

        for i in range(len(passport_field_list)):
            count = 0
            for j in range(len(passport_field_list[i])):
                lst = passport_field_list[i][j].split(":")
                validate = data_validation(lst[0], lst[1])
                if validate:
                    count += 1
            if count == 7:
                valid_passports += 1
        
        return valid_passports

def data_validation(key, value):
    if key == "byr":
        if value.isdigit() and int(value) >= 1920 and int(value) <= 2020:
            return True
        else:
            return False
    elif key == "iyr":
        if value.isdigit() and int(value) >= 2010 and int(value) <= 2020:
            return True
        else:
            return False
    elif key == "eyr":
        if value.isdigit() and int(value) >= 2020 and int(value) <= 2030:
            return True
        else:
            return False
    elif key == "hgt":
        if len(value) < 4:
            return False
        if value[-2:] == "cm":
            height_value = value[:-2]
            if height_value.isdigit() and int(height_value) >= 150 and int(height_value) <= 193:
                return True
            else:
                return False
        elif value[-2:] == "in":
            height_value = value[:-2]
            if height_value.isdigit() and int(height_value) >= 59 and int(height_value) <= 76:
                return True
            else:
                return False
        else:
            return False
    elif key == "hcl":
        if re.match("#[0-9a-f]{6}", value):
            return True
        else:
            return False
    elif key == "ecl":
        if value in ["amb","blu","brn","gry","grn","hzl","oth"]:
            return True
        else:
            return False
    elif key == "pid":
        if len(value) == 9 and value.isdigit():
            return True
        else:
            return False
    else:
        return False


total_validated_passports = validate_passports_with_data()
print(total_validated_passports)