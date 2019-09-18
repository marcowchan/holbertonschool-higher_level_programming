#include "lists.h"

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: pointer to the head of a linked list
 * Return: Palindrome(1) or Not(0)
 */
int is_palindrome(listint_t **head)
{
	listint_t *node = *head, *rev, *tmp;

	if (!node)
		return (1);
	for (rev = NULL; node; node = node->next)
	{
		tmp = malloc(sizeof(*tmp));
		tmp->n = node->n;
		tmp->next = rev;
		rev = tmp;
	}
	for (node = *head, tmp = rev; node; node = node->next, rev = rev->next)
	{
		if (node->n != rev->n)
		{
			free(tmp);
			return (0);
		}
	}
	return (1);

}

