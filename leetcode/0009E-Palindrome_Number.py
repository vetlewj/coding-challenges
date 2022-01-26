class Solution:
    def isPalindrome(self, x: int) -> bool:
        list_of_int = [c for c in str(x)]
        c_list = list_of_int.copy()
        list_of_int.reverse()
        if c_list == list_of_int:
            return True
        else: 
            return False