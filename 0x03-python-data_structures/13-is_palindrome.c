#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - function in C that checks if a singly linked list
 * is a palindrome.
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *s;
	int a, b;
	int c[2046];
	
	if (head != NULL)
		return (0);
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	s = *head;
	while (s != NULL)
	{
		c[a] = s->n;
		a++;
		s = s->next;
	}
	a--;
	for (b = 0, a++; b < a; a--, b++)
	{
		if (c[b] == c[a])
			;
		else
			return (0);
	}
	return (1);
}
