#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
assingment#.py
Created on Thu Aug 22 11:51:30 2019
@author: SPSjroseboom
"""


import sqlite3 as lite
import sys


def main():

    try:
        # Connect to DB
        db = lite.connect('pets.db')
        cursor = db.cursor()

        while True:
            try:
                user_input = int(raw_input('\n--- Welcome to the Pets Database ---'
                                           '\nPlease enter an ID #'
                                           '\n-1 will exit the program: '))
                if user_input == -1:
                    print '\n\n***Exiting Pets Database***\n\n'
                    sys.exit()

                elif isinstance(user_input, int) and user_input != -1:
                    cursor.execute(
                        '''
                            SELECT person.first_name, person.last_name, person.age, pet.name, pet.breed, pet.age, pet.dead
                            FROM person_pet, person, pet
                            WHERE person_pet.person_id = {0}
                            AND person_pet.person_id = person.id
                            AND person_pet.pet_id = pet.id
                        '''.format(user_input))

                    # Raise exception if there is no match.
                    requested_data = cursor.fetchall()
                    print '''\n{} {} is {} years old.\n\nPETS:
                    '''.format(
                        requested_data[0][0],
                        requested_data[0][1],
                        requested_data[0][2]
                    )
                    for row in requested_data:
                        if row[6] == 1:
                            print '{} was a {} who died at the age of {}.'.format(
                                row[3], row[4], row[5])
                        elif row[6] == 0:
                            print '{} is a {} year old {}.'.format(
                                row[3], row[5], row[4])

            except Exception:
                print 'ERROR: Enter a valid ID.'

        db.close()

    except Exception:
        print 'ERROR: The database could not be queried.'


if __name__ == '__main__':
    main()