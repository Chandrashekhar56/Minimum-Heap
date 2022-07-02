#include<iostream>
using namespace std;
int ArrayOfHeap[100];
int size;
int Size_Of_Maximum;
void MaximumHeapFunction(int n)
{

		Size_Of_Maximum = n;
		size = 0;
}
int Node_Parent(int position) { return (position - 1) / 2; }
int Node_leftChild(int position) { return (2 * position) + 1; }
int Node_rightChild(int position){ return (2 * position) + 2; }

bool CheckLeafFunction(int position)
{
    if (position > (size / 2) && position <= size)
        {
			return true;
		}
		return false;
}

void SwapFunction(int FirstPosition, int SecondPosition)
{
		int a;
		a = ArrayOfHeap[FirstPosition];
		ArrayOfHeap[FirstPosition] = ArrayOfHeap[SecondPosition];
		ArrayOfHeap[SecondPosition] = a;
}

void FindMaxHeap(int position)
{
		if (CheckLeafFunction(position))
			return;
		if (ArrayOfHeap[position] < ArrayOfHeap[Node_leftChild(position)] || ArrayOfHeap[position] < ArrayOfHeap[Node_rightChild(position)])
        {

			if (ArrayOfHeap[Node_leftChild(position)]> ArrayOfHeap[Node_rightChild(position)])
            {
				SwapFunction(position, Node_leftChild(position));
				FindMaxHeap(Node_leftChild(position));
			}
			else
			{
				SwapFunction(position, Node_rightChild(position));
				FindMaxHeap(Node_rightChild(position));
			}
		}
}
void ElementInsert(int value)
{
		ArrayOfHeap[size] = value;

		int current = size;
		while (ArrayOfHeap[current] < ArrayOfHeap[Node_Parent(current)])
        {
			SwapFunction(current, Node_Parent(current));
			current = Node_Parent(current);
		}
		size++;
}

void DisplayFunction()
{
	for(int i=0;i<size/2;i++)
    {

			cout<<"Node_Parent Node : "<<ArrayOfHeap[i]<<"\n";

			if(Node_leftChild(i)<size)
			cout<<" Left Child Node: " <<ArrayOfHeap[Node_leftChild(i)]<<"\n";

			if(Node_rightChild(i)<size)
				cout<<" Right Child Node: "<<ArrayOfHeap[Node_rightChild(i)]<<"\n";

				cout<<"\n";

    }

}
int extractMaximuHeap()
{
		int remove = ArrayOfHeap[0];
		ArrayOfHeap[0] = ArrayOfHeap[--size];
		FindMaxHeap(0);
		return remove;
}

main()
{

        MaximumHeapFunction(15);
        ElementInsert(1);
		ElementInsert(2);
		ElementInsert(3);
		ElementInsert(4);
		ElementInsert(5);
		ElementInsert(6);
		ElementInsert(7);
		ElementInsert(8);
		ElementInsert(9);
		DisplayFunction();
		cout<<"The maximum  value in heap "<<extractMaximuHeap()<<"\n";
}
