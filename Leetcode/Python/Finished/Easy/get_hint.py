class Solution:
    def getHint(self, secret, guess):
        """
        prints the number of bulls and cows from the guess to the secret.
        Bulls are the numbers in guess who are also in secret and have the same index.
        Cows are the numbers in guess who are also in secret but not the same index
        :param secret: string
        :param guess: string
        :return: string
        """
        bulls = 0
        secret_char_map = {}
        guess_char_array = []
        cows = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1 # 1
            elif secret[i] in secret_char_map:
                secret_char_map[secret[i]] += 1
                guess_char_array.append(guess[i])
            else:
                secret_char_map[secret[i]] = 1
                guess_char_array.append(guess[i])
        for char in guess_char_array:
            if char in secret_char_map and secret_char_map[char] != 0:
                cows += 1
                secret_char_map[char] -= 1
        answer = str(bulls) + 'A' + str(cows) + 'B'
        return answer