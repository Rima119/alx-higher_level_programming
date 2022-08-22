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
	listint_t *cr;
	listint_t *tl;

	if (list == NULL)
	{
		return (0);
	}

	cr = list;
	tl = list;
	while (tl != NULL && tl->next != NULL)
	{
		cr = cr->next;
		tl = tl->next->next;

		if (cr == list)
		{
			return (1);
		}
	}
	return (0);
}
