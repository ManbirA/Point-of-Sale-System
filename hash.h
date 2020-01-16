#include <iostream>
#include <string>


class hash{
    private:
        static const int table_size = 10;
        struct item
        {
            std::string product;
            int inventory;
            float price;
            item* next;
        };
        item* hash_table[table_size];
        
    public:
        hash();
        int get_hash(std::string key);
        void add_item(std::string item_name, int inventory_val, float price);
        int num_items_bucket(int index);
        int get_product_inventory(std::string product_val);
        float get_product_price(std::string product_val);
        
};

