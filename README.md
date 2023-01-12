# Log Component 
Simple Logger Module


## Install

```
pipenv shell
pipenv install
```

# Run
## Main script
```
python main.py
```

## Tests:
```
python -m unittest -v tests/test.py
```

# Comments

The main application should run in the main script. The LogComponent instance is initiated before the application is run, and is called within the application whenever needed. 

The implementation of a utility worker class in LogComponent is used to ensure that the logged messages and other LogComponent functionalities can be run in a separate thread, so that the execution of the main application is not hindered.

The stop behaviour described in the task is incomplete. There needs to be logic implemented for both cases of the `Stop` enum. 

Below are a rough ideas of how that could be done:

- `INSTANT`:  instantly shut down all tasks (and, by extension, threads) assigned to the worker.

- `Wait`: simply let all threads finish writing. 
