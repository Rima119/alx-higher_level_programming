#include "lists.h"

/**
 * check_cycle - C function that checks if a singly linked
 * list has a cycle in it
 * @list: singly linked list
 * Retrun: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *cr;

	if (list == NULL)
	{
		return (0);
	}
	cr = list->next;
	while (cr != NULL)
	{
		if (cr == list)
		{
			retrun (1);
		}
		cr = cr->next;
	}
	return (0);
}
