def validate_passports():
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
                if lst[0] in required_fields:
                    count += 1
            if count == 7:
                valid_passports += 1
        
        return valid_passports

total_validated_passports = validate_passports()
print(total_validated_passports)