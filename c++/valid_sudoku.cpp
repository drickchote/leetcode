// Neetcode link: https://neetcode.io/problems/valid-sudoku/question

#include <unordered_map>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<int, unordered_map<char, int>> line;
        unordered_map<int, unordered_map<char, int>> column;
        unordered_map<int, unordered_map<char, int>> square;
        for(int l=0; l<9; l++){
            for(int c=0; c<9; c++){
                char current = board[l][c];
                if(current == '.')
                    continue;
                    
                int s = ((int)(l/3)) * 3 + (int)c/3;
                if(line[l].find(current) != line[l].end()){
                    return false;
                }

                if(column[c].find(current) != column[c].end()){
                    return false;
                }

                if(square[s].find(current) != square[s].end()){
                    return false;
                }

                line[l][current] = 1;
                column[c][current] = 1;
                square[s][current] = 1;
            }
        }

        return true;
    }
};
