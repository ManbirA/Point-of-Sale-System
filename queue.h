#include <iostream>
#include <string>
#include "stack.h"
#ifndef QUEUE_H
#define QUEUE_H
class queue{
    private:
        struct Node{
            int size;
            stack order;
            Node* next;
            Node* prev;  
        };
        Node* front;
        Node* back;

    public:
        queue();
        bool is_empty();
        int size();
        void pop();
        void push(stack new_order, int size);
        stack get_top_order();
        stack get_bottom_order();
        int get_top_size();
        int get_bottom_size();


};
#endif