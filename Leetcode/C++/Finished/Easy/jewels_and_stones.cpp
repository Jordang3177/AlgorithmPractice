class Solution {
public:
    int numJewelsInStones(string J, string S) {
        int answer = 0;
        for (int i = 0; i < J.length(); i++) {
            for (int j = 0; j < S.length(); j++) {
                if (J.at(i) == S.at(j)) {
                    answer += 1;
                }
            }
        }
        return answer;
    }
};