#include <iostream>
#include <string>
#include "queue.h"
#include "stack.h"

queue::queue(){
    front = NULL;
    back = NULL;
}

int queue::size()
{
    Node* count_ptr = back;
    int count = 0;
    while(count_ptr != NULL)
    {
        count++;
        count_ptr = count_ptr->next; 
    }
    return count;
}

void queue::push(stack new_order, int size)
{
    Node* new_ptr = new Node();
    new_ptr->size = size;
    new_ptr->order = new_order;
    new_ptr->prev = NULL;
    if (this->size() == 0)
    {
        new_ptr->next = front;
        back = new_ptr;
        

    }
    else if(this->size() == 1)
    {
        back->prev = new_ptr;
        new_ptr->next = back;
        front = back;
        back = new_ptr;
    }
    else
    {
        back->prev = new_ptr;
        new_ptr->next = back;
        back = new_ptr;
    }
    

}

void queue::pop()
{

    if(front != NULL)
    {
        Node* del_ptr = front;
        
        if(back->next != front)
        {
            front = front->prev;
            front->next = NULL;
        }
        else
        {
            front = NULL;
            back->next = NULL;
        }
        delete(del_ptr);
    }
    else if(back != NULL)
    {
        delete(back);
        back = NULL;
        

    }
}

int queue::get_top_size()
{
    if(front != NULL)
    {
        return front->size;
    }
    else
    {
        return 0;
    }
    
}
int queue::get_bottom_size()
{
    if(back != NULL)
    {
        return back->size;
    }
    else
    {
        return 0;
    }
}

stack queue::get_top_order()
{
    if(front != NULL)
    {
        return front->order;
    }
}
stack queue::get_bottom_order()
{
    if(back != NULL)
    {
        return back->order;
    }
}

