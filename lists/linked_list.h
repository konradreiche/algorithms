#ifndef LINKED_LIST_H
#define LINKED_LIST

#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    struct node* next;
} node;

void add(node* head, int data);
node* delete(node* head, int data);
void delete2(node** head, int data);
node* find(node* head, int data);
void print_list(node* head);

#endif
