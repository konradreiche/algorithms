/*
 * Question 1
 *
 *      Implement the data structure singly linked list with the operations
 *      add, delete, find and length in C.
 *
 * Solution
 *
 *      The list is implemented with a struct node. The next pointer of the
 *      last node will be NULL, empty lists are represented by a NULL head
 *      pointer and all nodes will be allocated in the heap.
 *      
 */
#include <assert.h>
#include "linked_list.h"

void add(node* head, int data)
{
    node* current;
    node* node = malloc(sizeof(node));
    node->data = data;

    if (head == NULL)
    {
        head = node;
    }
    else
    {
        current = head;
        while (current->next != NULL)
        {
            current = current->next;
        }
        current->next = node;
    }
}

node* delete(node* head, int data)
{
    node* current = head;
    node* previous = current;
    while (current != NULL)
    {
        if (current->data == data)
        {
            previous->next = current->next;
            if (current == head)
            {
                head = current->next;
            }
            else
            {
                free(current);
            }
            return head;
        }
        previous = current;
        current = current->next;
    }
    return head;
}

/**
 * Question 2
 *
 *      Improve the delete function by implementing it without using a previous
 *      variable to store the last node.
 *
 * Solution
 *
 *      The key to the solution is to use pointers to pointers instead. The
 *      function signature is changed to take a node** as head parameter. This
 *      implementation also yields the advantage, that it does not need to
 *      return the head.
 */
void delete2(node** head, int data)
{
    node** current = head;
    while (*current != NULL)
    {
        node *entry = *current;
        if (entry->data == data)
        {
            *current = entry->next;
            free(entry);
            break;
        }
        else
        {
            current = &entry->next;
        }
    }
}

node* find(node* head, int data)
{
    node* current = head;
    if (current != NULL)
    {
        while (current != NULL)
        {
            if (current->data == data)
            {
                return current;
            }
            current = current->next;
        }
    }
    return NULL;
}

void print_list(node* head)
{
    node* current = head;
    if (current != NULL)
    {        
        while (current->next != NULL)
        {
            printf("%d, ", current->data);
            current = current->next;
        }
        printf("%d\n", current->data);
    }
}
