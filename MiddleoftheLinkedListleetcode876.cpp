
#include <iostream>
using namespace std;
struct ListNode
{
    int val;
    ListNode*next;
    ListNode*head;
    ListNode():val(0),next(nullptr){}
    ListNode(int x): val(x),next(nullptr){}
    ListNode(int x, ListNode*next):val(x),next(next){}
};
class Linkedlist{
    ListNode*head;
    public:
    Linkedlist() : head(NULL) {}
    void insertbegining(int value){
        ListNode*newNode=new ListNode;
        newNode->val=value;
        newNode->next = head;
        head = newNode;
    }
    void display(){
        if(!head){
            std::cout << "List is empy"<<std::endl;
            return;
        }
        ListNode*temp=head;
        while (temp)
        {
            std::cout<<temp->val<<"->";
            temp=temp->next;
        }
        std::cout<<"NULL"<<std::endl;
        
    };
};
class Solution {
    ListNode*head;
    public:
        //Solution() : head(NULL) {}
        void insertbegining(int value){
            ListNode*newNode=new ListNode;
            newNode->val=value;
            newNode->next = head;
            head = newNode;
        }
        void display(){
            if(!head){
                std::cout << "List is empy"<<std::endl;
                return;
            }
            ListNode*temp=head;
            while (temp)
            {
                std::cout<<temp->val<<"->";
                temp=temp->next;
            }
            std::cout<<"NULL"<<std::endl;
            
        };
        ListNode* middleNode(ListNode* head) {
            ListNode* slow = head;
            ListNode* fast = head;
            while (fast != NULL && fast->next != NULL) {
                slow = slow->next;
                fast = fast->next->next;
            }
            return slow;
            std::cout<<slow<<std::endl;
        }
    };
// void insertAtBegining(int value){
//     ListNode*newnode = new ListNode;
//     newnode->val = value;
// };
int main(){
    Solution List1;
    List1.insertbegining(10);
    List1.insertbegining(13);
    List1.insertbegining(15);
    List1.insertbegining(17);
    List1.display();
    Solution::middleNode;
};