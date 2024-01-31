#include <iostream>

using namespace std;

class Node
{
public:
    int data;
    Node *next;

    Node(int data)
    {
        this->data = data;
        next = NULL;
    }
};

void Insert(Node **head, int data)
{
    Node *newNode = new Node(data);
    newNode->next = *head;
    *head = newNode;
}
int main()
{
    Node *node1 = new Node(10);
    cout << node1->data << endl;
    cout << node1->next << endl;
}