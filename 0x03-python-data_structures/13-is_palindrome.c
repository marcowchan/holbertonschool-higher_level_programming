#include "lists.h"

/**
 * recurse - recursively checks if a linked list is a palindrome
 * @start: node to compare to end
 * @end: node to compare to start
 * Return: Palindrome(1) or Not(0)
 */
int recurse(listint_t **start, listint_t *end)
{
	int result;

	if (!end)
		return (1);
	result = recurse(start, end->next) && ((*start)->n == end->n);
	*start = (*start)->next;
	return result;
}

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: pointer to the head of a linked list
 * Return: Palindrome(1) or Not(0)
 */
int is_palindrome(listint_t **head)
{
	listint_t *node = *head;

	return (recurse(&node, node));
}

