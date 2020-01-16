#include <iostream>
#include <string>
#include "hash.h"
#include "stack.h"
#include "queue.h"
#include "Connector C++ 8.0\include\mysqlx\xdevapi.h"
#include "MySQL\MySQL Server 8.0\include\mysql.h"

int main()
{   
    stack order;
    stack order_two;
    stack order_three;
    stack order_four;
    hash products;
    queue orders_list;
    
    products.add_item("Fries", 10, 5.25);
    products.add_item("Burger", 10, 7.25);
    products.add_item("Drink", 10, 5.25);
    products.add_item("Pepper", 10, 7.25);
    products.add_item("Coffee", 10, 7.25);

    order.push("Fries", 2, products.get_product_price("Fries"));
    order.push("Burger", 2, products.get_product_price("Burger"));
    orders_list.pop();
    orders_list.push(order, order.size());
    
    orders_list.get_top_order().print_stack();
    std::cout << "\n";
    orders_list.get_bottom_order().print_stack();
    std::cout << "\n";

    order_two.push("Drink", 2, products.get_product_price("Drink"));
    order_two.push("Pepper", 2, products.get_product_price("Pepper"));
    order_two.push("Fries", 2, products.get_product_price("Fries"));
    //order_two.push("Burger", 2, products.get_product_price("Burger"));

    orders_list.push(order_two, order_two.size());

    orders_list.get_top_order().print_stack();
    std::cout << "\n";
    orders_list.get_bottom_order().print_stack();
    std::cout << "\n";

    order_three.push("Drink", 2, products.get_product_price("Drink"));
    order_three.push("Pepper", 2, products.get_product_price("Pepper"));
    order_three.push("Fries", 2, products.get_product_price("Fries"));
    order_three.push("Coffee", 2, products.get_product_price("Coffee"));
    
    orders_list.push(order_three, order_three.size());
    orders_list.pop();
    orders_list.pop();
    orders_list.pop();
    orders_list.push(order_two, order_three.size());
    orders_list.get_top_order().print_stack();
    std::cout << "\n";
    orders_list.get_bottom_order().print_stack();
    // std::cout << "\n";

    mysqlx::Session sess("localhost", 3306, "root", "password");

    
  }


