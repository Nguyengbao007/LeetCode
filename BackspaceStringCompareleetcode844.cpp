// Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

// Note that after backspacing an empty text, the text will continue empty.

// Example 1:

// Input: s = "ab#c", t = "ad#c"
// Output: true
// Explanation: Both s and t become "ac".
// Example 2:

// Input: s = "ab##", t = "c#d#"
// Output: true
// Explanation: Both s and t become "".
// Example 3:

// Input: s = "a#c", t = "b"
// Output: false
// Explanation: s becomes "c" while t becomes "b".
 
// Constraints:

// 1 <= s.length, t.length <= 200
// s and t only contain lowercase letters and '#' characters.
#include <iostream>
#include <stack>
#include <string>
using namespace std;
class Solution1 {
    public:
        bool backspaceCompare(string s, string t) {
            stack<char>st1,st2;
            for (int i=0;i<s.size();i++){
                if(s[i]!='#'){
                    st1.push(s[i]);
                }else if (!st1.empty())
                {
                    st1.pop();
                };
                
            };
            for (int i=0;i<t.size();i++){
                if(t[i]!='#'){
                    st2.push(t[i]);
                }else if (!st2.empty())
                {
                    st2.pop();
                };
                
            };
            return st1==st2 ? true : false;
        }
    };// time complexity is O(n+m) and space complexity is O(n+m)
//solution 2
class Solution2 {
    public:
        bool backspaceCompare(string s, string t) {
            string s2=stringbuilder(s);
            string t2=stringbuilder(t);
            return s2==t2 ? true:false;
        }
    private:
         string stringbuilder(string str){
            string res;
            int skip=0;
            for (int i = str.length();i>=0;i--){
                if(str[i]=='#'){
                    skip++;
                }else if (skip>0){
                    skip--;
                }else{
                    str+=str[i];
                }
            }
            return res;
        }//time complexity O(n) and space complexity O(n)
    };
int main(){
    Solution1 compare1;
    Solution2 compare2;
    cout<<"Solution 1"<<endl;
    cout<<compare1.backspaceCompare("ab#c","ad#c")<<endl;
    cout<<"Solution 2"<<endl;
    cout<<compare2.backspaceCompare("ab#c","ad#c")<<endl;
};