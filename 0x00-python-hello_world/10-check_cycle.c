#include "lists.h"
#include <stdio.h>

/**
  * check_cycle - Checks if a singly linked list has a cycle in it
  * @list: input the singly linked list to check
  *
  * Return: 1 if has a cycle in it or 0 if not
  */
int check_cycle(listint_t *list)
{
	listint_t *doub = list;
	listint_t *reg = list;

	if (list == NULL)
	{
		return (0);
	}
	while (doub && doub->next)
	{
		reg = reg->next;
		doub = doub->next->next;

		if (reg == doub)
		{
			return (1);
		}
	}
	return (0);
}
