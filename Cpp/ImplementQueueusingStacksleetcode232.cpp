// Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

// Implement the MyQueue class:

// void push(int x) Pushes element x to the back of the queue.
// int pop() Removes the element from the front of the queue and returns it.
// int peek() Returns the element at the front of the queue.
// boolean empty() Returns true if the queue is empty, false otherwise.
// Notes:

// You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
// Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 
// Example 1:

// Input
// ["MyQueue", "push", "push", "peek", "pop", "empty"]
// [[], [1], [2], [], [], []]
// Output
// [null, null, null, 1, 1, false]

// Explanation
// MyQueue myQueue = new MyQueue();
// myQueue.push(1); // queue is: [1]
// myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
// myQueue.peek(); // return 1
// myQueue.pop(); // return 1, queue is [2]
// myQueue.empty(); // return false
#include <stack>
#include<iostream>
using std::stack;
class MyQueue {
    public:
        MyQueue() {

        }
        
        void push(int x) {
            inputStack.push(x);
        }
        
        int pop() {
            prepareOutputStack();
            int element = outputStack.top();
            outputStack.pop();
            return element;
        }
        
        int peek() {
            prepareOutputStack();
            return outputStack.top();
        }
        
        bool empty() {
            return inputStack.empty() && outputStack.empty();
        }
    private:
        stack<int>inputStack;
        stack<int>outputStack;
        void prepareOutputStack(){
            if(outputStack.empty()){
                while (!inputStack.empty())
                {
                    outputStack.push(inputStack.top());
                    inputStack.pop();
                }
                
            }
        }
    };
int main(){
    MyQueue* obj=new MyQueue();
    obj->push(1);
    obj->push(2);
    int ele1=obj->pop();
    int ele2=obj->peek();
    bool empty = obj->empty();
    std::cout<<ele1<<std::endl;
    std::cout<<ele2<<std::endl;
}