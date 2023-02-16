class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_integer = {'I': 1, 'V': 5, 'X': 10, 
        'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        answer = 0
        for i, v in enumerate(s):
            answer += roman_to_integer[v]
            if (v == 'V' or v == 'X') and s[i-1] == 'I':
                answer -= 2
            elif (v == 'L' or v == 'C') and s[i-1] == 'X':
                answer -= 20
            elif (v == 'D' or v == 'M') and s[i-1] == 'C':
                answer -= 200
        return answer