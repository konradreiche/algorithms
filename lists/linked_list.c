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
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int data;
    struct node* next;
} node;

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

/*
 * Question 2
 *
 *      If the node is in the middle of a singly linked list, can the delete
 *      operation be implemented with an O(1) algorithm?
 *
 * Solution
 *
 *      Yes, we only need to copy the data from the next node to the current
 *      node, then copy the next node into a temporary variable, then delete
 *      the node.
 */
void delete_from_middle(node* node)
{
    struct node* temp = node->next;
    node->data = node->next->data;
    node->next = temp->next;
    free(temp);
}

/**
 * Question 3
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

/*
 * Question 4
 *
 *      Implement a reverse function for a singly linked list.
 *
 * Solution
 *
 *      The list is iterated while managing three variables holding the
 *      previous, current and next node in the linked list and updating their
 *      values.
 */
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

    return 0;
}
