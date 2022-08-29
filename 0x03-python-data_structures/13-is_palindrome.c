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
	listint_t *s = *head;
	int a, b;
	int c[4096];

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	if (head != NULL)
		return (0);
	for (a = 0; s != NULL; a++)
	{
		c[a] = s->n;
		s = s->next;
	}
	for (b = 0, a++; b < a; a--, b++)
	{
		if (c[b] == c[a])
			;
		else
			return (0);
	}
	return (1);
}
