#include "hash_tables.h"

/**
 * hash_djb2 - Hash func implementing the djb2 algorithm in the prog.
 * @str: The str to hash.
 *
 * Return: The calculated hash in the prog.
 */
unsigned long int hash_djb2(const unsigned char *str)
{
	unsigned long int hash;
	int c;

	hash = 5381;
	while ((c = *str++))
		hash = ((hash << 5) + hash) + c;

	return (hash);
}
