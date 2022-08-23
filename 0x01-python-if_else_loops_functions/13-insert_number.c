#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - function in C that inserts a number into
 * a sorted singly linked list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
      listint_t *a = *head;
      listint_t *nw = malloc(sizeof(listint_t));

      if (!nw)
            return (NULL);
      
      nw->n = number;
      nw->next = NULL;

      if (!a || nw->n < a->n)
      {
            nw->next = a;
            return (*head = nw);
      }
      while (a)
      {
            if (!a->next || nw->n < a->next->n)
            {
                    nw->next = a->next;
                    a->next = nw;
                    return (a);
            }
            a = a->next;
      }
      return (NULL);
}
