#include <iostream>

using namespace std;

int main()
{
    string letters;
    cin >> letters;
    int lettersLength = letters.length();
    int i, j;
    char a, b;
    string str;
    str = "Unique";
    
    for(i = 0; i < lettersLength; i++){
        a = letters[i];
        for(j = i + 1; j < lettersLength; j++){
            b = letters[j];
            if(a == b){
                str = "Deja Vu";
            }
        }
    }
    cout << str;

    return 0;
}
