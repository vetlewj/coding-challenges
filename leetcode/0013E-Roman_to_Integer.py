class Solution:
    def romanToInt(self, s: str) -> int:
        s_list = [c for c in s]
        roman_dict = {
            "I": 1,
            "V": 5, 
            "X": 10, 
            "L": 50, 
            "C": 100, 
            "D": 500,
            "M": 1000
        }
        res_num = 0
        for i, j in enumerate(s_list[:-1]): 
            if s_list[i] != "": 
                if j == "I" and (s_list[i+1] == "V" or s_list[i+1] == "X"):
                    res_num += roman_dict.get(s_list[i+1]) - roman_dict.get(s_list[i])
                    s_list[i+1] = ""
                elif j == "X" and (s_list[i+1] == "L" or s_list[i+1] == "C"): 
                    res_num += roman_dict.get(s_list[i+1]) - roman_dict.get(s_list[i])
                    s_list[i+1] = ""
                elif j == "C" and (s_list[i+1] == "D" or s_list[i+1] == "M"): 
                    res_num += roman_dict.get(s_list[i+1]) - roman_dict.get(s_list[i])
                    s_list[i+1] = ""
                elif i == len(s_list)-2: 
                    res_num += roman_dict.get(s_list[i])
                    res_num += roman_dict.get(s_list[i+1])
                else: 
                    res_num += roman_dict.get(s_list[i])
            elif i == len(s_list)-2: 
                res_num += roman_dict.get(s_list[i+1])
        if len(s_list) == 1: 
            res_num += roman_dict.get(s_list[0])
                
        return res_num