class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        substitution_table = {}
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        index = 0

        for char in key:
            if char != ' ' and char not in substitution_table:
                substitution_table[char] = alphabet[index]
                index += 1
            if index == 26:  
                break

  
        decoded_message = ''
        for char in message:
            if char == ' ':
                decoded_message += ' '
            else:
                decoded_message += substitution_table[char]

        return decoded_message
#https://leetcode.com/problems/decode-the-message/