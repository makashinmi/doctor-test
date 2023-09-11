class TooManyArgumentsError(Exception):
    pass

class NotEnoughArgumentsError(Exception):
    pass

class Validator:
    def __init__(self):
        self.commandsToAmountOfArgs = {command: numOfArgs for command, numOfArgs in (
                                                                                ('SET', 2), 
                                                                                ('GET', 1), 
                                                                                ('UNSET', 1), 
                                                                                ('FIND', 1), 
                                                                                ('COUNTS', 1), 
                                                                                ('END', 0), 
                                                                                ('BEGIN', 0), 
                                                                                ('COMMIT', 0), 
                                                                                ('ROLLBACK', 0),
                                                                              ) 
                                 }

    def validate(self, command, *args):
        if command not in self.commandsToAmountOfArgs.keys():
            pass
        else:
            requiredAmountOfArgs = self.commandsToAmountOfArgs[command]
            providedAmountOfArgs = len(args)

            if providedAmountOfArgs != requiredAmountOfArgs:
                message = f'Command "{command}" takes {requiredAmountOfArgs} arguments, but {providedAmountOfArgs} {"was" if providedAmountOfArgs == 1 else "were"} given.'
                
                if providedAmountOfArgs > requiredAmountOfArgs:
                    raise TooManyArgumentsError(f'{message}\nDid you mean "{" ".join([command, *args[:requiredAmountOfArgs]])}"?')
                else:
                    raise NotEnoughArgumentsError(message)

