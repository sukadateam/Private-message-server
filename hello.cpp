#include <iostream>
using namespace std;
//Translate inputs into an opposite value
extern "C" int not_gate(int input) {
    if ( input == 1 ) {
        return 0;
    }
    else if ( input == 0 ) {
        return 1;
    }
    else {
        //Return 2 if a value cannot be desided.
        return 2;
    }
}
//Method Failed as python uses True instead of true.
#ifdef __cplusplus
extern "C" const char not_gateBool(string input) {
    if ( input == "False" ) {
        return "True";
    }
    else if ( input == "True") {
        return "False";
    }
    else {
        return "False";
    }
}
#endif
extern "C" int xor_gate(int input, int input1) {
    bool match;
    match = false;
    if (input == 0) {
        if (input1 == 1) {
            match=true;
            return 1;
        }
    }
    if (input == 1) {
        if (input1 == 0) {
            match=true;
            return 1;
        }
    }
    if (match == false) {
        return 0;
    }
    //Exiting Value. c++ compiler.
    return 2;
}
extern "C" int and_gate(int input, int input1) {
    if (input == 1) {
        if (input1 == 1){
            return 1;
        }
    }
    return 0;
}
//Compile as a shared library: ----
//g++ -c -o library.o hello.cpp
//g++ -shared -o libfoo.so library.o