# consultree
Draw tree of key/value pairs from HashiCorp Consul.  The script makes assumptions about how the keys are formatted
and likely only works for the very specific case I encounted at the time of writing.
## Example
### Create a virtual environment and activate (optional)
```
$ virtualenv -p ~/.pyenv/versions/3.6.1/bin/python ~/venv_consultree
$ . ~/venv_consultree/bin/activate
```
## Install requirements
```
$ pip install -r requirements.txt
```
## Draw a tree given a Consul address and a top-level key
```
(venv_consultree) $ python consultree.py myconsulserver.com my_root
my_root
 +-- my_folder
 |   +-- my_subfolder
 |       +-- my_value
 +-- my_other_folder
     +-- my_other_subfolder
         +-- my_other_value
```