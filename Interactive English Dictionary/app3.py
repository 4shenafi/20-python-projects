import mysql.connector
from difflib import get_close_matches


def get_definition(host, user, password, database_name, table_name, word):
    try:
        mydb = mysql.connector.connect(
            host=host, user=user, password=password, database=database_name
        )
        mycursor = mydb.cursor()

        word = word.lower()
        mycursor.execute(
            f"SELECT Definition FROM {table_name} WHERE LOWER(Expression) = %s", (word,),
        )
        result = mycursor.fetchall()

        if result:
            definitions = [row[0] for row in result]
            return definitions

        # Check title case
        mycursor.execute(
            f"SELECT Definition FROM {table_name} WHERE Expression = %s",
            (word.title(),),
        )
        result = mycursor.fetchall()

        if result:
            definitions = [row[0] for row in result]
            return definitions

        # Check upper case
        mycursor.execute(
            f"SELECT Definition FROM {table_name} WHERE Expression = %s",
            (word.upper(),),
        )
        result = mycursor.fetchall()

        if result:
            definitions = [row[0] for row in result]
            return definitions

        # Check for close matches
        mycursor.execute(f"SELECT Expression FROM {table_name}")
        all_words = [row[0].lower() for row in mycursor.fetchall()]
        close_matches = get_close_matches(word, all_words)

        if close_matches:
            close_match = close_matches[0]
            mycursor.execute(
                f"SELECT Definition FROM {table_name} WHERE LOWER(Expression) = %s",
                (close_match,),
            )
            result = mycursor.fetchall()
            if result:
                close_match_definition = [row[0] for row in result]
                response = input(f"Did you mean {close_match}? Enter Y if yes, or N if no: ")
                if response.lower() == "y":
                    return close_match_definition
                elif response.lower() == "n":
                    return "The word doesn't exist. Please double check it."
                else:
                    return "We didn't understand your entry."

        return "The word doesn't exist. Please double check it."

    except mysql.connector.Error as err:
        return f"Error: {err}"
    finally:
        if 'mydb' in locals() and mydb.is_connected():
            mycursor.close()
            mydb.close()


if __name__ == "__main__":
    host = "localhost"
    user = "root"
    password = ""
    database_name = "dictionary"
    table_name = "dictionary_table"

    while True:
        word = input("Enter a word ('/x' to exit): ")
        if word == "/x":
            break
        output = get_definition(
            host, user, password, database_name, table_name, word
        )
        if isinstance(output, list):
            for item in output:
                print(item)
        else:
            print(output)