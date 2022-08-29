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
	int a = 0, b;
	char c[1000];

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	s = *head;
	while (s != NULL)
	{
		c[a] = s->n;
		a++;
		s = s->next;
	}
	for (b = 0; b < a; b++)
	{
		if (c[b] == c[a])
		{
			a--;
		}
		else
			return (0);
	}
	return (1);
}
