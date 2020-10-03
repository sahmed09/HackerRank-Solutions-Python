"""Not supported in Python.. Though currently python also supports Generics"""

# Solution in java:
"""
import java.util. *;

class Printer < T > {
    / **
    * Method Name: printArray
    * Print each element of the generic array on a new line.Do not return anything.
    * @ param A generic array
    ** /
    // Write your code here
    public static < E > void printArray(E[] generic){
        for (E element: generic) {
            System.out.println(element);
        }
    }

}

public class Generics {

    public static void main(String args[]){
        Scanner scanner = new Scanner(System.in );
        int n = scanner.nextInt();
        Integer[] intArray = new Integer[n];
        for (int i = 0; i < n; i++) {
            intArray[i] = scanner.nextInt();
        }

        n = scanner.nextInt();
        String[] stringArray = new String[n];
        for (int i = 0; i < n; i++) {
            stringArray[i] = scanner.next();
        }

        Printer < Integer > intPrinter = new Printer < Integer > ();
        Printer < String > stringPrinter = new Printer < String > ();
        intPrinter.printArray( intArray  );
        stringPrinter.printArray( stringArray );
        if (Printer.class.getDeclaredMethods().length > 1){
            System.out.println("The Printer class should only have 1 method named printArray.");
        }
    }
}
"""

# Solution in c++:
"""
#include <iostream>
#include <vector>
#include <string>

using namespace std;

/**
*    Name: printArray
*    Print each element of the generic vector on a new line. Do not return anything.
*    @param A generic vector
**/

// Write your code here
template<typename T> 
void printArray(vector<T> array) {
     for(T i : array){
          cout << i << endl;
     }
}

int main() {
    int n;

    cin >> n;
    vector<int> int_vector(n);
    for (int i = 0; i < n; i++) {
        int value;
        cin >> value;
        int_vector[i] = value;
    }

    cin >> n;
    vector<string> string_vector(n);
    for (int i = 0; i < n; i++) {
        string value;
        cin >> value;
        string_vector[i] = value;
    }

    printArray<int>(int_vector);
    printArray<string>(string_vector);

    return 0;
}
"""
