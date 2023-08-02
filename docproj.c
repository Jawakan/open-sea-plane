#include <stdio.h>
#include <stdbool.h>
#include <type.h>

/*
- Use a combination of the input values to select from a range of pre-defined conditions
Ex: Male, 18, etc. = possibly Ligma or Sugma
*/

int main() {

    char str[2] gender;
    bool M, F;
    float age;
    
    //gender = printf("Please input patient Gender.\nM for Male / F for Female\nGender: ");
    age = printf("Please input patient Age: ");
    //scanf("%d", &age);

// divide  use age input as float by some value, use result to get age range
    int marv = 0;

    while (marv == 0) {
        switch(age) {
            case age/22 < 1:
            printf("18-21"); // These are all placeholders until a clear structure is defined
            marv = 1;
            break;

            case age/30 < 1:
            printf("22-29");
            marv = 1;
            break;

            case age/40 < 1:
            printf("30-39");
            marv = 1;
            break;

            case age/50 < 1:
            printf("40-49");
            marv = 1;
            break;

            case age/60 < 1:
            printf("50-59");
            marv = 1;
            break;

            case age/70 < 1:
            printf("60-69");
            marv = 1;
            break;

            case age/80 < 1:
            printf("70-79");
            marv = 1;
            break;

            case age/90 < 1:
            printf("80-89");
            marv = 1;
            break;

            case age/101 < 1:
            printf("90-100");
            marv = 1;
            break;

            default:
            printf("Placeholder"); // Make loop if default value is triggered 
            break;                 // (👉ﾟヮﾟ)👉 ⫹⫺ *Need these done before you head out
        }                          // -Bossman
    }
} // <remove this bracket after adding "gender" section
/*
    if(toupper(gender) = "M" ) {
        M = true
    }
    else {
        F = true
    }

    return 0;
}
*/
