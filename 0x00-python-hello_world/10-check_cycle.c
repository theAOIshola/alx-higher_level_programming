#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list hasa cycle
 * @list: linked list to be checked
 * Return: 1 if list has a cycle, otherwise 0
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = slow;

	if(!list)
		return (0);

	while(slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
