#include <iostream>
#include <string>
#include "stack.h"


stack::stack(){
    top = NULL;
}


bool stack::is_empty()
{
    if(top == NULL)
    {
        return true;
    }
    else
    {
        return false;
    }

}

void stack::push(std::string product, int quantity_val, float price_val)
{
    Node* new_ptr = new Node();
    new_ptr->product_name = product;
    new_ptr->quantity = quantity_val;
    new_ptr->price = price_val;
    new_ptr->next = top;
    top = new_ptr;


}

void stack::pop()
{
    if(top != NULL){
        Node* del_ptr = top;
        top = top->next;
        delete(del_ptr);
    }

}

int stack::get_top_quantity()
{
    if(top != NULL)
    {
        return top->quantity;
    }
    else
    {
        return -1;
    }
}
float stack::get_top_price()
{
    if(top != NULL)
    {
        return top->price;
    }
    else
    {
        return -1;
    }
}
std::string stack::get_top_product()
{
    if(top != NULL)
    {
        return top->product_name;
    }
    else
    {
        return NULL;
    }
}

int stack::size()
{
    Node* count_ptr = top;
    int count = 0;
    while(count_ptr != NULL)
    {
        count++;
        count_ptr = count_ptr->next; 
    }
    return count;

}


void stack::print_stack()
{
    Node* count_ptr = top;
    int count = 0;
    while(count_ptr != NULL)
    {
        std::cout << count_ptr->product_name << "\n";
        count_ptr = count_ptr->next; 
    }


}