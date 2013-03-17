#include <assert.h>
#include "linked_list.h"

node* reverse(node* head);
void delete_from_middle(node* node);

int main(int argc, char** argv)
{
    node* head;
    head->data = 1;

    add(head, 2);
    add(head, 3);
    add(head, 4);
    add(head, 5);
    add(head, 6);
    add(head, 7);
    add(head, 8);
    add(head, 9);

    print_list(head);

    assert(find(head, 1)->data == 1);
    assert(find(head, 5)->data == 5);
    assert(find(head, 9)->data == 9);
    assert(find(head, 10) == NULL);

    head = delete(head, 1);
    print_list(head);

    head = delete(head, 5);
    print_list(head);
    
    head = delete(head, 9);
    print_list(head);

    delete2(&head, 2);
    print_list(head);
    
    delete2(&head, 6);
    print_list(head);

    delete2(&head, 8);
    print_list(head);

    head = reverse(head);
    print_list(head);

    delete_from_middle(head->next);
    print_list(head);

    return 0;
}
