#include<iostream>

using namespace std;

struct node{
  int data;
  node *next;
};

class linked_list{
private:
  node *head, *tail;
public:
  linked_list(){
    head = NULL;
    tail = NULL;
  }
  node* get_head(){
    return head;
  }
  void add_node_at_end(int value){
    node *tmp = new node;
    tmp->data = value;
    tmp->next = NULL;
    if(head == NULL && tail == NULL){
      head = tmp;
      tail = tmp;
    }
    else{
      tail->next = tmp;
      tail = tail->next;
    }
  }
  void print_list(){
    node *tmp = head;
    while(tmp != NULL){
      cout<<tmp->data<<"\t";
      tmp = tmp->next;
    }
    cout<<"NULL";
  }
};

int main(){
  linked_list l;
  l.add_node_at_end(1);
  l.add_node_at_end(2);
  l.print_list();
  return 0;
}
