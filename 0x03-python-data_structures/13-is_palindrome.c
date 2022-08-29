#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - function in C that checks if a singly
 * linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *s = *head;
	char b[1000];
	int m = 0;
	size_t p = 0;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	while (s != NULL)
	{
		p++;
		s = s->next;
	}
	p--;
	while (m < p)
	{
		if (b[m] == b[p])
		{
			m++;
			p--;
		}
		else
		{
			return (0);
		}
	}
	return (1);

