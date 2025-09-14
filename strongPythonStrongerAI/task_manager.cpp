#include<iostream>
#include<random>
#include<string>
#include<vector>
using namespace std;

class TASK {
public:
    string name;
    int deadline;

    TASK() {
        cout <<"Describe your task: ";
        cin.ignore();
        getline(cin, name);
        cout <<"Enter deadline(days): ";
        cin >> deadline;
    }
};

vector<TASK> TASK_SORTING(vector<TASK> &T) {
    for(int i = 0; i < T.size() - 1; i++) {
        for(int j = 0; j < T.size() - i - 1; j++) {
            if(T[j].deadline > T[j+1].deadline) {
                swap(T[j], T[j+1]);
            }
        }
    }
    return T;
}

void MOST_PRIOR_TASK(vector<TASK> &T) {
    cout <<"\nMost prior task:\n";
    cout <<"Task: " << T[0].name << " | Deadline: " << T[0].deadline << " days\n";
}

void LEAST_PRIOR_TASK(vector<TASK> &T) {
    cout <<"\nLeast prior task:\n";
    cout <<"Task: " << T[T.size()-1].name << " | Deadline: " << T[T.size()-1].deadline << " days\n";
}

void RANDOM_TASK(vector<TASK> &T) {
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dist(0, T.size() - 1);

    int randomIndex = dist(gen);
    cout <<"\nRandom task:\n";
    cout <<"Task: " << T[randomIndex].name << " | Deadline: " << T[randomIndex].deadline << " days\n";
}

int main() {
    vector<TASK> tm;
    char ch;
    char num;

    // Input tasks
    while(true) {
        cout <<"Do you want to add a new task? (y/n): ";
        cin >> ch;
        if(ch == 'n' || ch=='N')
            break;
        TASK t;
        tm.push_back(t);
    }

    // Sort once
    TASK_SORTING(tm);

    // Menu
    while(true) {
        cout <<"\nEnter following number to perform operations:\n";
        cout <<"1: Most Prior task\n";
        cout <<"2: Least Prior task\n";
        cout <<"3: Random task\n";
        cout <<"0: Exit\n";
        cout <<"Your choice: ";
        cin >> num;

        switch(num) {
            case '1': MOST_PRIOR_TASK(tm); break;
            case '2': LEAST_PRIOR_TASK(tm); break;
            case '3': RANDOM_TASK(tm); break;
            case '0': return 0;
            default: cout <<"Invalid input!\n"; break;
        }
    }
}
