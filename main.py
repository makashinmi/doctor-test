from database import Database, Transaction
from validator import Validator, TooManyArgumentsError, NotEnoughArgumentsError

runtime = True
db = Database() 
val = Validator()

while runtime:
    command, *args = input('> ').split()
    command = command.upper()

    try:
        val.validate(command, *args)
    except (TooManyArgumentsError, NotEnoughArgumentsError) as e:
        print(e)
    else:
        match command: 
            case 'GET':
                result = db.get(*args)
                print(result)
            case 'SET':
                db.set(*args)
            case 'UNSET':
                db.unset(*args)
            case 'FIND':
                result = db.find(*args)
                print(result)
            case 'COUNTS':
                result = db.counts(*args)
                print(result)
            case 'END':
                runtime = False
            case 'BEGIN':
                db = Transaction(db)
            case 'COMMIT' | 'ROLLBACK':
                if db.__class__ is Transaction:
                    if command == 'COMMIT':
                        db.commit()
                    db = db.parent
                else:
                    print(f"There's no active transcation to {command[0].lower()}.")
