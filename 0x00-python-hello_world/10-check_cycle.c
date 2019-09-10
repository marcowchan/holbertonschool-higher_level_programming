#include "lists.h"

/**
 * check_cycle - checks if a linked list is circular
 * @list: linked list to check
 * Return: Circular(1) or Not(0)
 */
int check_cycle(listint_t *list)
{
	listint_t *runner = list;

	if (!list)
		return (0);
	while (runner->next && runner->next->next)
	{
		list = list->next;
		runner = runner->next->next;
		if (list == runner)
			return (1);
	}
	return (0);
}
