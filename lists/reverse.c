/*
 * Question
 *
 *      Implement a reverse function for a singly linked list.
 *
 * Solution
 *
 *      The list is iterated while managing three variables holding the
 *      previous, current and next node in the linked list and updating their
 *      values.
 */
#include "linked_list.h"

node* reverse(node* head)
{
    node* new_head = NULL;
    while (head != NULL)
    {
        node* next = head->next;
        head->next = new_head;
        new_head = head;
        head = next;
    }
    return new_head;
}
