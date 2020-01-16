
#include <iostream>
#include <string>
#ifndef STACK_H
#define STACK_H
class stack
{
    private:
        struct Node
        {
            std::string product_name;
            int quantity;
            float price;
            Node* next;
        };
        Node* top;
    public:
        stack();
        bool is_empty();
        int size();
        void pop();
        void push(std::string product, int quantity, float price);
        std::string get_top_product();
        int get_top_quantity();
        float get_top_price();
        void print_stack();
        
};
#endif