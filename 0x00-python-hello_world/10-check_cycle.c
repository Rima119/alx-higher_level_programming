#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - C function that checks if a singly linked
 * list has a cycle in it
 * @list: singly linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *cr = list;
	listint_t *tl = list;

	if (list == NULL)
	{
		return (0);
	}

	while (cr != NULL && tl != NULL && tl->next != NULL)
	{
		cr = cr->next;
		tl = tl->next->next;

		if (cr == tl)
		{
			return (1);
		}
	}
	return (0);
}
