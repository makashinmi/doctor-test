from database import Database, Transaction

runtime = True
db = Database() 

while runtime:
    print(db.debug())
    command = input('> ').split()
    match command[0]: 
        case 'GET':
            result = db.get(command[1])
            print(result)
        case 'SET':
            db.set(command[1], command[2])
        case 'UNSET':
            db.unset(command[1])
        case 'FIND':
            result = db.find(command[1])
            print(result)
        case 'COUNTS':
            result = db.counts(command[1])
            print(result)
        case 'END':
            runtime = False
        case 'BEGIN':
            db = Transaction(db)
        case 'COMMIT' | 'ROLLBACK':
            if db.__class__ is Transaction:
                if command[0] == 'COMMIT':
                    db.commit()
                db = db.parent
            else:
                print(f"There's no active transcation to {command[0].lower()}.")
