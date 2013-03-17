/*
 * Question
 *
 *      If the node is in the middle of a singly linked list, can the delete
 *      operation be implemented with an O(1) algorithm?
 *
 * Solution
 * 
 *      Yes, to do so only the node to be deleted is required. Its next node is
 *      copied into a temporarly variable and the data is copied into the
 *      current node. Then the pointer to the next node is set to the node
 *      after the next node. Hence, the node is used to inherit the data from
 *      the following node instead of touch the other nodes.
 * 
 */
#include "linked_list.h"

void delete_from_middle(node* node)
{
    struct node* temp = node->next;
    node->data = node->next->data;
    node->next = temp->next;
    free(temp);
}
