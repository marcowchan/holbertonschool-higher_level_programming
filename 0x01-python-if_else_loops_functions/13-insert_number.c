#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a node into a linked list
 * @head: head of the linked list
 * @number: number to insert
 *
 * Return: pointer to inserted node, or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	if (!head)
		return NULL;

	new = malloc(sizeof(*new));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

        current = *head;
	if (*head == NULL)
		*head = new;
	else if (number < current->n)
	{
		new->next = current;
		*head = new;
	}
	else
	{
		while (current->next)
		{
			if (number > current->next->n)
				current = current->next;
			else
				break;
		}
		new->next = current->next;
		current->next = new;
	}

	return (new);
}
