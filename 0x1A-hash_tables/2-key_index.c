#include "hash_tables.h"

/**
 * key_index - Get the indx at which a key/val pair should
 *             be stored in arr of a hash table.
 * @key: The key to get the index of.
 * @size: The size of the arr of the hash table.
 *
 * Return: The index of the key in the program.
 *
 * Description: Uses the djb2 algorithm.
 */
unsigned long int key_index(const unsigned char *key, unsigned long int size)
{
	return (hash_djb2(key) % size);
}
