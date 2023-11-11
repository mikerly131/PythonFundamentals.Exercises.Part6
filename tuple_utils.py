from typing import Iterable, Tuple, List, Union
TicTacToeRow = List[str]
TicTacToeBoard = Tuple[TicTacToeRow, TicTacToeRow, TicTacToeRow]


def tic_tac_toe_finish(board: TicTacToeBoard, pos_y: int, pos_x: int, symbol: str) -> None:
    """
    This function takes in a TicTacToeBoard and applies the finishing move based on the provided parameters pos_y,
    pos_x, and symbol.

    :param board: A tuple containing 3 TicTacToeRows. Each TicTacToeRow in turn is a list containing 3 strings
    :param pos_y: The position of the TicTacToeRow that needs to be modified
    :param pos_x: The position of the column within a TicTacToeRow that needs to be modified
    :param symbol: The symbol that should be placed in the column (X, or O)
    :return: None
    """

    # Put winning symbol in correct spot on the board.  Position on board is in list, inside tuple
    board[pos_y][pos_x] = symbol
    


    # remove pass statement and implement me


def count_instances(collection: Tuple, instance: Union[int, str]) -> int:
    """
    This function counts the number of occurrences of the instance value within the collection parameter.

    :param collection: A tuple containing 0 or more instances
    :param instance: An item in the collection parameter
    :return: An integer.
    """

    """
    instance_count = 0
    for i in range(len(collection)):
        if instance == collection[i]:
            instance_count = instance_count + 1

    return instance_count
    """
    return collection.count(instance)
     # remove pass statement and implement me


def print_indexes_and_entries(indexes: Iterable, entries: Iterable) -> None:
    """
    This function iterates through the given parameters and prints the items formatted according to the following rules:
    The index of the indexes iterable correspond to the index of the entries iterable.
    The index takes 10 places even if it doesn't need all 10 places.

    :param indexes: A list or tuple
    :param entries: A list or tuple
    :return: None
    """

    # zip the tuples or lists together
    zipped_list = list(zip(indexes, entries))

    # write a for loop to print each pair
    for index, entry in zipped_list:

        #  use a string formatter, make index a string so numbers left align and pass test
        print(f'Index: {str(index):10} Entry: {entry}')         
        
    # remove pass statement and implement me


def print_items_with_index(items: Iterable):
    """
    This function iterates through the items parameter and prints the item formatted according to the following rules:
    Each item printed received the index 1-N where N is the size of the items parameter.
    Indexes start at 1.
    Each index and item are separated by a colon and a space.
    :param items: A tuple or a list
    :return: None
    """
    
    # the book helps a lot, tuple & dictionary chapters, make items a list, get length
    # zip items with range of its length, put that in dictionary, index will start at 0 for each item, as tuples

    t_list = list(items)
    t_len = len(t_list)
    d = dict(zip(items, range(0, t_len)))
    
    # print index must start at 1, print each item, which is a tuple, from the dictionary formatted

    for i in d:
        print(f'{(d[i]+1)}: {i}')

    """
    More efficient alt -- 
    for x in range(len(items)):
        print(f'{x+1}: {items[x]}')
    """
    
    
    
    
    # remove pass statement and implement me

