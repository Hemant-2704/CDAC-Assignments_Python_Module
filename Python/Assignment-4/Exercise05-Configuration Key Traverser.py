"""
Scenario Configuration files loaded from JSON databases consist of nested dictionary hierarchies. 
Checking key existence at every level using nested conditions (if key in dictionary) leads to complex and verbose code. 
You need to write a clean traverser utility that navigates nested dictionaries using exceptions. 

Problem Description:
Write a function traverse_nested_config(config_dict, path_str, default=None): 
config_dict is a nested dictionary configuration tree. 
path_str is a string specifying the configuration path using dot notation (e.g., "server.database.port"). 
The function should split the path_str on . characters and traverse down config_dict. 

Implementation Constraint: 
You must attempt to traverse keys directly. Do not use key-existence checks (like if key in dict) or class-checks (like if isinstance(sub_dict, dict)). 
Instead, handle the lookup path directly inside a try block and catch the following exceptions to return the default value: 
- Catch KeyError if any key in the path does not exist. 
- Catch TypeError or AttributeError if you try to index a primitive, non-dictionary value (e.g., trying to access a key like "port" on a configuration value that resolved to a string or number). 
- If path_str is empty or config_dict is not a valid dictionary, return the default value. 

Test Data & Test Cases:
config = { 
    "server": { 
        "host": "127.0.0.1", 
        "port": 8080, 
        "ssl": { 
            "enabled": True, 
            "cert_path": "/etc/ssl/certs" 
        } 
    }, 
    "database": "postgresql://localhost:5432"
}

# Test Case 1: Valid Path
print(traverse_nested_config(config, "server.ssl.cert_path"))
# Output: /etc/ssl/certs

# Test Case 2: Missing Key (Triggers KeyError)
print(traverse_nested_config(config, "server.database.username", "guest"))
# Output: guest

# Test Case 3: Indexing Non-Dictionary value (Triggers TypeError)
# Here config["database"] is a string, which cannot be indexed with "host"
print(traverse_nested_config(config, "database.host", "localhost"))
# Output: localhost
"""

from pprint import pprint

def line():
    pprint("_"*90)
    return()


config = {
    "server": {
        "host": "127.0.0.1",
        "port": 8080,
        "ssl": {
            "enabled": True,
            "cert_path": "/etc/ssl/certs"    }
    },
    "database": "postgresql://localhost:5432"
}

def traverse_nested_config(config_dict, path_str, default=None):

    try:
        path=path_str.split(".")
    except:
        print("Something Went Wrong!!")

    current=config

    for i in path:
        try:
            # Checking inside each time with help of list called path
            current=current[i]

        # If error is caused then    
        except(KeyError):
            print(f"Key {i} Not Found !")
            return(f"Output= {default}")

        except(TypeError):
            print(f"Key is string not dictionary !")
            return(f"Output= {default}")


    return(current)

# [server,ssl,cert_path]

line()
print("Test Case 1: Valid Path")
print(f"output={traverse_nested_config(config, "server.ssl.cert_path")}")
# Output: /etc/ssl/certs

line()
print("Test Case 2: Missing Key (Triggers KeyError)")
print(traverse_nested_config(config, "server.database.username", "guest"))
# Output: guest

line()
print("Test Case 3: Indexing Non-Dictionary value (Triggers TypeError)")
# Here config["database"] is a string, which cannot be indexed with "host"
print(traverse_nested_config(config, "database.host", "localhost"))
# Output: localhost

