#include <stdio.h>
#include <stdbool.h>

/*
- Use a combination of the input values to select from a range of pre-defined conditions
Ex: Male, 18, etc. = possibly Ligma or Sugma
*/

int main() {

    bool gender, M, m, F, f;
    int age;
    
    //gender = printf("Please input patient Gender.\nM for Male / F for Female\nGender: ");
    age = printf("Please input patient Age: ");
    scanf("%d", &age);


    switch(age) {
        case 18:
        case 19:
        case 20:
        case 21:
        printf("18-21");
        break;

        case 22:
        case 23:
        case 24:
        case 25:
        case 26:
        case 27:
        case 28:
        case 29:
        printf("22-29");
        break;

        case 30:
        case 31:
        case 32:
        case 33:
        case 34:
        case 35:
        case 36:
        case 37:
        case 38:
        case 39:
        printf("30-39");
        break;

        case 40:
        case 41:
        case 42:
        case 43:
        case 44:
        case 45:
        case 46:
        case 47:
        case 48:
        case 49:
        printf("40-49");
        break;

        case 50:
        case 51:
        case 52:
        case 53:
        case 54:
        case 55:
        case 56:
        case 57:
        case 58:
        case 59:
        printf("50-59");
        break;

        case 60:
        case 61:
        case 62:
        case 63:
        case 64:
        case 65:
        case 66:
        case 67:
        case 68:
        case 69:
        printf("60-69");
        break;

        case 70:
        case 71:
        case 72:
        case 73:
        case 74:
        case 75:
        case 76:
        case 77:
        case 78:
        case 79:
        printf("70-79");
        break;

        case 80:
        case 81:
        case 82:
        case 83:
        case 84:
        case 85:
        case 86:
        case 87:
        case 88:
        case 89:
        printf("80-89");
        break;

        case 90:
        case 91:
        case 92:
        case 93:
        case 94:
        case 95:
        case 96:
        case 97:
        case 98:
        case 99:
        case 100:
        printf("90-100");
        break;

        default:
        printf("Placeholder"); // Make loop is default value is triggered 
        break;                 // (👉ﾟヮﾟ)👉 ⫹⫺ *Need these done before you head out
    }                          // -Bossman
} // remove this bracket after adding "gender" section  
/*
    if(gender = M || m) {
        switch(age) {
            case 1:

        }
    }
    else(gender = F || f) {

    }

    return 0;
}
*/
