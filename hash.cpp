#include <iostream>
#include <string>
#include "hash.h"


int hash::get_hash(std::string key)
{
    return key.length() % table_size;
}

hash::hash()
{
    for(int i = 0; i < table_size; i++){
        hash_table[i] = new item;
        hash_table[i]->product = "TestProduct";
        hash_table[i]->inventory = 2;
        hash_table[i]->next = NULL;

    } 
}
void hash::add_item(std::string item_name, int inventory_val, float price_val)
{
    int index = get_hash(item_name);

    if (hash_table[index]->product == "TestProduct")
    {
        hash_table[index]->product = item_name;
        hash_table[index]->inventory = inventory_val;
        hash_table[index]->price = price_val;
    }else
    {
        item* ptr = hash_table[index];
        item* new_ptr = new item;
        new_ptr->product = item_name;
        new_ptr->inventory = inventory_val;
        new_ptr->price = price_val;
        new_ptr->next = NULL;
        while(ptr->next != NULL)
        {
            ptr = ptr->next;
        }
        ptr->next = new_ptr;
    }

}

int hash::num_items_bucket(int index)
{
    int count = 0;
    item* ptr = hash_table[index];
    while(ptr->next != NULL)
    {
        ptr = ptr->next;
        count++;
    }
    return count + 1;
}

int hash::get_product_inventory(std::string product_val)
{
    int index = get_hash(product_val);
    item* ptr = hash_table[index];
    while (ptr->next != NULL)
    {
        if (ptr->product == product_val)
        {
           return ptr->inventory; 
        }
        ptr = ptr->next;
    }
    
    if (ptr->product == product_val)
    {
        return ptr->inventory;
    }
    else
    {
        return -1;
    }
    

}

float hash::get_product_price(std::string product_val)
{
    int index = get_hash(product_val);
    item* ptr = hash_table[index];
    while (ptr->next != NULL)
    {
        if (ptr->product == product_val)
        {
           return ptr->inventory; 
        }
        ptr = ptr->next;
    }
    
    if (ptr->product == product_val)
    {
        return ptr->price;
    }
    else
    {
        return -1;
    }
    

}