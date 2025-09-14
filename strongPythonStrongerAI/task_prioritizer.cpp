#include <iostream>
#include<string>
#include <vector>
#include <algorithm>
using namespace std;

// Structure to store task details
struct Task {
    string name;
    int deadline; // in days
};

// Function to sort tasks based on priority (lower deadline = higher priority)
void sortTasksByPriority(vector<Task> &tasks) {
    sort(tasks.begin(), tasks.end(), [](const Task &a, const Task &b) {
        return a.deadline < b.deadline;
    });
}

// Function to get the highest priority task (smallest deadline)
Task getHighestPriorityTask(const vector<Task> &tasks) {
    if (tasks.empty()) {
        return {"No Task", -1}; // return dummy task if empty
    }
    return tasks[0]; // after sorting, first task is highest priority
}

int main() {
    vector<Task> tasks;
    char choice;

    while (true) {
        Task t;
        cout << "Enter task name: ";
        cin.ignore(); // clear buffer before getline
        getline(cin, t.name);

        cout << "Enter deadline in days: ";
        cin >> t.deadline;

        tasks.push_back(t);

        cout << "Do you want to add another task? (y/n): ";
        cin >> choice;
        if (choice == 'n' || choice == 'N') {
            break;
        }
    }

    // Sort tasks by priority
    sortTasksByPriority(tasks);

    cout << "\nTasks sorted by priority:\n";
    for (const auto &t : tasks) {
        cout << "Task: " << t.name << " | Deadline: " << t.deadline << " days\n";
    }

    // Get the highest priority task
    Task topTask = getHighestPriorityTask(tasks);
    cout << "\nHighest Priority Task:\n";
    cout << "Task: " << topTask.name << " | Deadline: " << topTask.deadline << " days\n";

    return 0;
}
