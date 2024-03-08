//file name:CS112_A1_T5_game3_ 20231117.cpp
//author: Anan Hamdi Ali
//Id:20231117
//data: 1/3/2024
//purpose: subtract a square in this game.you play with another player you select number of coins.
//than every player enter a square number until the number of coins become zero.then the winner is the last blayer
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

int main() {
    // Seed the random number generator
    srand(time(0));

    // starting the game
    cout << "press enter to start" << endl;
    cin.get();

    // Game description
    cout << "Welcome to the game of subtracting a square.\n"
         << "In this game, you have a number of coins.\n"
         << "You can select them manually or randomly. There are two players.\n"
         << "Each player subtracts a square number from the coins they have,\n"
         << "and the last player who takes the last coins is the winner.\n"
         << "Rules:\n"
         << "1. You have to select a number of coins.\n"
         << "2. Each player has to subtract a square number from the coins they have.\n"
         << "3. The last player is the winner.\n";

    // Determine the number of coins
    int remain;
    string choice;
    
    while (true) {
        cout << "if you want to select the number of coins enter ( select ) \nif you want to make it randomly enter (random): ";
        cin >> choice;
        if (choice == "select") {
            cout << "Please enter the number of coins: ";
            cin >> remain;
            break ;
        } else if(choice == "random") {
            int numbers_random[] = {29, 33, 37, 40, 43, 85, 48};
            remain = numbers_random[rand() % 7]; // تغيير الرقم 6 إلى 7 لأنه يجب أن يكون الحد الأقصى 7 لأنه يتم استخدام 7 قيم
            cout << "The number of coins is " << remain << endl;
            break ;
        } else {
            cout << "invalid input please enter ( select / random)" << endl;
            continue ;
        }
    }    
    // initial value to current player
    int current_player = 1;

    // While loop to repeat the turns until remain = 0
    while (remain >= 1) {
        // Determine current player
        string player_name = (current_player == 1) ? "Player 1" : "Player 2";

        // Player select the number of move
        int move;
        cout << player_name << ": select a square num 1-16: ";
        while (!(cin >> move) || move <= 0 || move > 16 || sqrt(move) != floor(sqrt(move))) {
            cout << "Invalid input. Please select a square number between 1 and 16." << endl;
            cin.clear(); // Clear the error flag
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Discard incorrect input
        }
         // the number of coins must be less than moving 
        if (remain < move) {
            cout << "Invalid number." << endl;
            continue;
        }

        remain -= move;
        cout << "Now the number of coins is " << remain << endl;

        if (remain == 0) {
            cout << player_name << " is the winner." << endl;
            cout << "End game." << endl;
            break;
        }

        // Switch player
        current_player = (current_player == 1) ? 2 : 1;
    }

    return 0;
}
    